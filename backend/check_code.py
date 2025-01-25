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
def check_code(code :str, input_arr :list, expected_output_arr: list):
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