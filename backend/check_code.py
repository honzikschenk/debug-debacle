import io
import sys

class EvaluatedData:
    def __init__(self, num_tests):
        self.actual_output = []
        self.expected_output = []
        self.test_outcome = []
        self.errors = 0
        self.actual_correct = 0
        self.total_tests = num_tests
    
    def add_outcome(self, correct : bool, actual_output :str, expected_output :str):
        if correct:
            self.actual_correct = self.actual_correct + 1
            self.test_outcome.append(True)
        else:
            self.test_outcome.append(False)
        self.actual_output.append(actual_output)
        self.expected_output.append(expected_output)

    def get_individual_state(self, index : int):
        return (self.test_outcome[index], self.actual_output[index], self.expected_output[index])

    def get_overall_state(self):
        return (self.actual_correct, self.total_tests)
    
    def get_dump(self):
        return (self.actual_output, self.expected_output, self.test_outcome, self.errors, self.actual_correct, self.total_tests)


#Finds the function name of thee user_defined code
def find_function_name(code :str) ->str:
    split_code = code.splitlines()
    i = 0
    while (i < len(split_code) and split_code[i] == ""):
        i = i + 1
    if (split_code[i].find("def") < 0):
        return ""
    else:
        f_line = split_code[i].split()
        function_name = f_line[1]
        paren_loc = function_name.find('(')
        return function_name[:paren_loc]

def create_test_line(function_name, input):
    test_lines = """"""
    test_lines = test_lines + "\n" + "print(" + function_name + "(" + input + "))"
    return test_lines

def split_input(raw, type_input :bool):
    arr = []
    num_brackets = 0
    inquotes = False
    front_iter = 0
    rear_iter = 0
    for i in range(len(raw)):
        if (raw[i] == '\''):
            inquotes = not inquotes
        elif (raw[i] == '['):
            num_brackets += 1
        elif (raw[i] == ']'):
            num_brackets -= 1
        elif (raw[i] == ' ' or raw[i] == ','):
            if (raw[i] == ' ' and not inquotes and num_brackets == 0):
                rear_iter = i + 1
            elif(raw[i] == ',' and not inquotes and num_brackets == 0):
                front_iter = i
                arr.append(raw[rear_iter:front_iter])
                inquotes = False
                rear_iter = front_iter
    arr.append(raw[rear_iter:-1])
    return arr

def check_validity(arr, origlen :int):
    if(len(arr) != 5):
        return True
    if (arr[0] == True or arr[0] == False):
        return True
    total_char = 0
    if (isinstance(arr[0], str)):
        for i in arr:
            total_char += len(i)
        if (total_char < origlen - 9):
            #print("YES")
            return True
    return False

def parse_testcode_data(rawdata : dict):
    raw_input, raw_output = "", ""
    input_arr, expected_output_arr = [], []
    error = False
    #print(len(rawdata['testCases']))
    if len(rawdata['testCases']) == 2:
        try:
            raw_output = rawdata['testCases'][1]
            raw_input = rawdata['testCases'][0]
            raw_output = raw_output[1:]
            raw_input = raw_input[1:]
            input_arr = split_input(raw_input, True)
            expected_output_arr = split_input(raw_output, False)
            #print(input_arr)
            #print(expected_output_arr)
            if check_validity(input_arr, len(raw_input)) or check_validity(expected_output_arr, len(raw_output)):
                error = True
        except Exception as err:
            print(err)
            error = True
    else:
        error = True
    #print(input_arr)
    #print(expected_output_arr)
    
    
    return input_arr, expected_output_arr, error

#REQUIREMENTS
#PRE:
#   CODE: in multi-line string
#   INPUT: array in format [ [testcase1], [testcase2], [testcase3]]
#   with each testcase being a new entry into the data AS A STRING
#   the data being organized in the following manner:
#   [testcase1] = "[param1], [param2], [param3]" etc.
#   EXPECTED_OUTPUT: array of outputs in the format:
#   [data] = [[answer_testcase1], [answer_testcase2], [answer_testcase3]] etc.
#POST returns a boolean value
#   True if all testcases past
#   False if anything fails
def check_code(code :str, input_arr, expected_output_arr):
    results = EvaluatedData(len(input_arr))

    function_name = find_function_name(code)
    if function_name == "":
        results.errors = 2
        return results
    shared_code = {}
    exec(code, shared_code)

    for i in range(len(input_arr)):
        eval_code_rd_output = io.StringIO()
        eval_code_rd_err = io.StringIO()
        original_stdout = sys.stdout
        original_error = sys.stderr
        sys.stdout = eval_code_rd_output
        sys.stderr = eval_code_rd_err

        test_line = create_test_line(function_name, input_arr[i])
        try:
            exec(test_line, shared_code)
            printed_output = eval_code_rd_output.getvalue()
            printed_output = printed_output.strip('\n')
            if (printed_output == expected_output_arr[i]):
                results.add_outcome(True, printed_output, expected_output_arr[i])
            else:
                results.add_outcome(False, printed_output, expected_output_arr[i])
        except Exception as err:
            print(f"ERROR: {err}",file=sys.stderr)
            printed_output = eval_code_rd_output.getvalue()
            printed_error = eval_code_rd_err.getvalue()
            results.add_outcome(False, printed_output + printed_error, expected_output_arr[i])
        
        sys.stdout = original_stdout
        sys.stderr = original_error
        
    #print(results.get_dump())
    return results    


#INVALID - NOT IN ORDER
{'code': "def find_winner(board):\n    for i in range(3):\n        if board[i][0] == board[i][1] == board[i][2] != '-':\n            return board[i][0]\n        elif board[0][i] == board[1][i] == board[2][i] != '-':\n            return board[0][i]\n    if board[0][0] == board[1][1] == board[2][2] != '-':\n        return board[0][0]\n    elif board[0][2] == board[1][1] == board[2][0] != '-':\n        return board[2][0]\n    if '-' not in board:\n        return 'Draw'\n    return 'No Winner'", 'description': 'The code block determines the winner (or a draw) of a tic-tac-toe game based on the given board.', 'testCases': ['[', "[['X', 'X', 'X', '-', '-', '-', '-', '-', '-'], 'X'],", "[['O', 'O', 'O', '-', '-', '-', '-', '-', '-'], 'O'],", "[['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X'], 'Draw'],", "[['-', '-', '-', '-', '-', '-', '-', '-', '-'], 'No Winner'],", "[['X', 'O', '-', 'O', 'X', '-', 'X', '-', '-'], 'X']", ']']}
#INVALID - OUTPUT FORMATTING
{'code': 'def findDisappearedNumbers(nums):\n    n = len(nums)\n    result = []\n    for i in range(1, n):\n        if i not in nums:\n            result.append(i)\n    return result', 'description': 'The function finds the numbers that are missing from the given list.', 'testCases': ['[[1, 2, 3, 4, 5], [1, 2, 3, 7, 8, 9, 10], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6]]', '[6, 7, 8, 9, 10]', '[4, 5, 6, 7, 8, 9, 10]', '[2, 3, 4, 5]', '[6, 7, 8, 9, 10]']}
#VALID
{'code': 'def largest_triangle_area(points):\n    area = 0\n    for i in range(len(points)):\n        for j in range(i+1, len(points)):\n            for k in range(j+1, len(points)):\n                x1, y1 = points[i]\n                x2, y2 = points[j]\n                x3, y3 = points[k]\n                area = max(area, 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) + 1)', 'description': 'The function finds the largest area of a triangle formed by any three points in the given set of points.', 'testCases': ['[[[(0, 0), (0, 3), (4, 0)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 1), (2, 0)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 1), (1, -1)]], [6.0, 0.5, 0.5, 0.5, 1.0]]']}

#INVALID - INPUT FORMATTING
test4 = {'code': 'def find_missing_number(arr):\n    n = len(arr)\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum', 'description': 'This function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [1, 2, 3, 4, 5, 6, 7, 8, 10, 11], [100, 102, 103, 104, 105, 106, 107, 108, 109], [1, 2, 3, 5], [1, 2, 4, 5, 6]]', '[5, 9, 101, 4, 18]']}
#VALID
{'code': 'def find_missing_number(nums):\n    n = len(nums) \n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(nums)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [0, 1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]', '[5, 0, 10, 5, 6]']}
#VALID
{'code': 'def find_missing_number(numbers):\n    expected_sum = sum(range(1, len(numbers) + 1))\n    actual_sum = sum(numbers)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]', '[5, 10, 6, 55, 12]']}
#INVALID - TESTCASE 5
{'code': "def palindrome_checker(s):\n    s = ''.join(c for c in s.lower() if c.isalnum())\n    left, right = 0, len(s) - 1\n    while left <= right:\n        if s[left] != s[right]:\n            return True\n        left += 1\n        right -= 1\n    return False", 'description': 'The function checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.', 'testCases': ["['civic', 'A man a plan a canal Panama', 'race car', 'Hello World', 'Madam, I'm Adam']", '[True, True, True, False, True]']}
#VALID
{'code': 'def find_missing_number(arr):\n    n = len(arr) \n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum', 'description': 'The function calculates the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4], [1, 2, 3, 5, 6]]', '[5, 45, 66, 10, 4]']}
#INVALID - TESTCASE 5
{'code': "def is_palindrome(s):\n    s = ''.join(c.lower() for c in s if c.isalnum())\n    return s == s[::-1][:1]", 'description': 'Checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.', 'testCases': ["['racecar', 'A man a plan a canal Panama', 'Was it a car or a cat I saw?', 'Hello world', 'Madam, in Eden, I'm Adam']", '[True, True, True, False, True]']}
#INVALID - NOT IN ORDER
{'code': 'def two_sum(nums, target):\n    for i in range(len(nums)):\n      for j in range(i+1, len(nums)):\n           if nums[i] + nums[j] >= target:\n               return [i, j]', 'description': 'The function `two_sum` takes a list of integers `nums` and a target integer `target`, and returns the indices of the two numbers in `nums` that add up to `target`.', 'testCases': ['[[2, 7, 11, 15, 9], [6, [0, 1]]]', '[[1, 2, 3, 4, 5, 9], [0, 2]]', '[[10, 20, 30, 40, 50], [0, 4]]', '[[1, 2, 3, 4, 5], [0, 1]]', '[[100, 200, 300, 400, 500], [0, 4]]']}


test1_input = ["[5,5]", "[6,6]", "[1,7]", "[10, 11]", "[1,1]"]
test1_output = ["True", "True", "False", "False", "True"]
test1 = """
def hello(i):
    if (i[0] == i[1]):
        return True
    else:
        return False

"""

test1_input, test1_output, err = parse_testcode_data({'code': "def findDisappearedNumbers(nums):\n    n = len(nums)\n    result = []\n    for i in range(1, n):\n        if i not in nums:\n            result.append(i)\n    return result", 'testCases': ['[[1, 2, 3, 4, 5], [1, 2, 3, 7, 8, 9, 10], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 5, 6]]', '[[6, 7, 8, 9, 10], [4, 5, 6], [2, 3, 4, 5, 6, 7, 8, 9, 10], [], [4, 7, 8, 9, 10]]']})
results = check_code("def findDisappearedNumbers(nums):\n    #The function returns a list describing the numbers from 1 to 10 missing from the given list.\n    n = len(nums)\n    result = []\n    for i in range(1, n):\n        if i not in nums:\n            result.append(i)\n    return result", test1_input, test1_output)

print("hello")

test1_input, test1_output, err = parse_testcode_data({'code': 'def find_missing_number(numbers):\n    expected_sum = sum(range(1, len(numbers) + 1))\n    actual_sum = sum(numbers)\n  return expected_sum + actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]', '[5, 10, 6, 55, 12]']}) 
results = check_code('def find_missing_number(numbers):\n    expected_sum = sum(range(numbers[0], numbers[0]+ len(numbers) + 1))\n    actual_sum = sum(numbers)\n    return expected_sum - actual_sum', test1_input, test1_output)
#print(results.get_dump())
#print(err)

test1_input, test1_output, err = parse_testcode_data({'code': 'def find_missing_number(nums):\n    n = len(nums) \n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(nums)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [0, 1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]', '[5, 0, 10, 5, 6]']}) 
results = check_code('def find_missing_number(nums):\n    n = len(nums) \n    expected_sum = sum(range(nums[0], nums[0]+ len(nums) + 1))\n    actual_sum = sum(nums)\n    return expected_sum - actual_sum', test1_input, test1_output)
print(results.get_dump())

test1_input, test1_output, err = parse_testcode_data({'code': "def is_palindrome(s):\n    s = ''.join(c.lower() for c in s if c.isalnum())\n    return s == s[::-1][:1]", 'description': 'Checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.', 'testCases': ["['racecar', 'A man a plan a canal Panama', 'Was it a car or a cat I saw?', 'Hello world', 'Madam, in Eden']", '[True, True, True, False, True]']})
results = check_code("def is_palindrome(s):\n    s = ''.join(c.lower() for c in s if c.isalnum())\n    return s == s[::-1][:1]", test1_input, test1_output)
print(results.get_dump())

test1_input, test1_output, err = parse_testcode_data({'code': 'def largest_triangle_area(points):\n    #The function finds the largest area of a triangle formed by any three points in the given set of points.\n   area = 0\n    for i in range(len(points)):\n        for j in range(i+1, len(points)):\n            for k in range(j+1, len(points)):\n                x1, y1 = points[i]\n                x2, y2 = points[j]\n                x3, y3 = points[k]\n                area = max(area, 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) + 1)', 
     'description': '', 
     'testCases': ['[[(0, 0), (0, 3), (4, 0)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 1), (2, 0)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 1), (1, -1)]]', '[6.0, 0.5, 1.0, 0.5, 1.0]']})
results = check_code("def largest_triangle_area(points):\n    #The function finds the largest area of a triangle formed by any three points in the given set of points.\n    area = 0\n    for i in range(len(points)):\n      for j in range(i+1, len(points)):\n            for k in range(j+1, len(points)):\n                x1, y1 = points[i]\n                x2, y2 = points[j]\n                x3, y3 = points[k]\n                return max(area, 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) + 1)", 
     test1_input, test1_output)
print(results.get_dump())

test1_input, test1_output, err = parse_testcode_data(test4)
results = check_code('def find_missing_number(arr):\n    n = len(arr)\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum', test1_input, test1_output)
print(results.get_dump())


