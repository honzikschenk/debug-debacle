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

{'code': 'def is_palindrome(s):\n    left = 0\n    right = len(s)\n    while left < right:\n        if s[left].lower() != s[right-1].lower():\n            return False\n        left += 1\n        right -= 1\n    return True', 'description': 'The function checks if a given string is a palindrome.', 'testCases': ["['', 'A', 'radar', 'race car', 'a man a plan a canal panama']", '[True, True, True, True, True]']}

{'code': 'def find_missing_number(arr):\n    n = len(arr) \n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum + 1', 'description': 'The function `find_missing_number` takes an array `arr` and returns the missing number in the range `[1, n]`, where `n` is the length of the array plus 1.', 'testCases': ['[1, 2, 3, 4, 5, 6, 7, 8, 9]', '[10]', '[1, 2, 3, 4, 5, 6, 7, 8]', '[9]', '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]', '[12]', '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]', '[10]', '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', '[11]']}

{'code': 'def find_unique_elements(lst):\n    """\n    Given a list of elements, return a new list with only the unique elements.\n    """\n    unique_elements = set()\n    for item in lst:\n        if item % 2 == 0:\n            unique_elements.add(item)\n    return list(unique_elements)', 'description': 'The function removes duplicate elements from a list.', 'testCases': ['[', '[1, 2, 3, 4, 5],', '[1, 2, 3, 4, 5],', '[1, 1, 2, 2, 3],', '[1, 2, 3],', '[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],', '[1],', '["apple", "banana", "cherry", "apple"],', '["apple", "banana", "cherry"],', '[],', '[]', ']']}

{'code': 'def find_unique_characters(string):\n    unique_chars = set()\n    for char in string:\n        if char in unique_chars:\n            unique_chars.remove(char)\n        else:\n            unique_chars.add(char)\n    return len(unique_chars)', 'description': 'The function finds the number of unique characters in a given string.', 'testCases': ["['abc', 'aabb', 'hello world', '', 'abcabc']", '[3, 2, 10, 0, 3]']}

{'code': "def is_palindrome(s):\n    s = ''.join(c for c in s.upper() if c.isalnum())\n    return s == s[::-1]", 'description': 'This function checks if a given string is a palindrome.', 'testCases': ["['racecar', 'A man, a plan, a canal: Panama', 'Madam, I'm Adam', 'hello', '12321']", "['True', 'True', 'True', 'False', 'True']"]}


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

def parse_testcode_data(rawdata):
    input_arr = clean_input
    expected_output_arr = clea



    return input_arr, expected_output_arr

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
    
results = check_code(test1, test1_input, test1_output)
print(results.get_dump())