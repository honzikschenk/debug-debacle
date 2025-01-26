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
        if (index.isnumeric()):
            return (self.test_outcome, self.actual_output, self.expected_output)

    def get_overall_state(self):
        return (self.actual_correct, self.total_tests)
    
    def get_dump(self):
        return (self.actual_output, self.expected_output, self.test_outcome, self.errors, self.actual_correct, self.total_tests)

{'code': 'def find_missing_number(arr):\n    n = len(arr)\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum', 'description': 'This function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6],', '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],', '[100, 101, 102, 103, 104, 105, 106, 107, 108, 109],', '[1, 2, 3, 4, 5],', '[1, 2, 3, 4, 5, 6]]', '[5, 55, 55, 15, 21]']}

{'code': 'def find_missing_number(nums):\n    n = len(nums) \n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(nums)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [0, 1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]', '[5, 0, 10, 5, 6]']}

{'code': 'def find_missing_number(numbers):\n    expected_sum = sum(range(1, len(numbers) + 1))\n    actual_sum = sum(numbers)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]', '[5, 10, 6, 55, 12]']}

{'code': "def palindrome_checker(s):\n    s = ''.join(c for c in s.lower() if c.isalnum())\n    left, right = 0, len(s) - 1\n    while left <= right:\n        if s[left] != s[right]:\n            return True\n        left += 1\n        right -= 1\n    return False", 'description': 'The function checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.', 'testCases': ["['civic', 'A man a plan a canal Panama', 'race car', 'Hello World', 'Madam, I'm Adam']", '[True, True, True, False, True]']}

{'code': 'def find_missing_number(arr):\n    n = len(arr) \n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum', 'description': 'The function calculates the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4], [1, 2, 3, 5, 6]]', '[5, 45, 66, 10, 4]']}

{'code': "def is_palindrome(s):\n    s = ''.join(c.lower() for c in s if c.isalnum())\n    return s == s[::-1][:1]", 'description': 'Checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.', 'testCases': ["['racecar', 'A man a plan a canal Panama', 'Was it a car or a cat I saw?', 'Hello world', 'Madam, in Eden, I'm Adam']", '[True, True, True, False, True]']}

{'code': 'def two_sum(nums, target):\n    for i in range(len(nums)):\n        for j in range(i+1, len(nums)):\n            if nums[i] + nums[j] >= target:\n                return [i, j]', 'description': 'The function `two_sum` takes a list of integers `nums` and a target integer `target`, and returns the indices of the two numbers in `nums` that add up to `target`.', 'testCases': ['[[2, 7, 11, 15, 9], [6, [0, 1]]]', '[[1, 2, 3, 4, 5, 9], [0, 2]]', '[[10, 20, 30, 40, 50], [0, 4]]', '[[1, 2, 3, 4, 5], [0, 1]]', '[[100, 200, 300, 400, 500], [0, 4]]']}


test1_input = ["\"ski\"", "\"biz\"", "\"green \"", "\"pine \"", "\"Chirstmas \""]
test1_output = ["skitree", "biztree", "green tree", "pine tree", "Chirstmas tree"]
test1 = """
def hello(i):
    i = i + "tree"
    
    return i

"""
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

def clean_input(raw_input):
    clean_input = raw_input
    return clean_input


def clean_output(raw_output :str):
    return raw_output

def split_input(raw):
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
            if (raw[i] == ' ' and not inquotes and num_brackets == 0 and raw[i-1] == ','):
                rear_iter = i + 1
            elif(raw[i] == ',' and not inquotes and num_brackets == 0):
                front_iter = i
                arr.append(raw[rear_iter:front_iter])
                inquotes = False
                rear_iter = front_iter
    arr.append(raw[rear_iter:-1])
    return arr


def parse_testcode_data(rawdata):
    raw_input, raw_output = "", ""
    input_arr, expected_output_arr = [], []
    error = False
    print(rawdata['testCases'])
    if len(rawdata['testCases']) == 2:
        raw_output = rawdata['testCases'][1]
        raw_input = rawdata['testCases'][0]
        raw_output = raw_output[1:]
        raw_input = raw_input[1:]
        input_arr = split_input(raw_input)
        expected_output_arr = split_input(raw_output)

    else:
        error = True

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
def check_code(code :str, rawdata : dict):
    input_arr, expected_output_arr = parse_testcode_data(rawdata)
    results = EvaluatedData(len(input_arr))

    function_name = find_function_name(code)
    if function_name == "":
        results.errors = 1
        return results
    exec(code)

    for i in range(len(input_arr)):
        eval_code_rd_output = io.StringIO()
        eval_code_rd_err = io.StringIO()
        original_stdout = sys.stdout
        original_error = sys.stderr
        sys.stdout = eval_code_rd_output
        sys.stderr = eval_code_rd_err

        test_line = create_test_line(function_name, input_arr[i])
        try:
            exec(test_line)
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
        
        
    return results    
    
#results = check_code(test1, test1_input, test1_output)
#print(results.get_dump())
