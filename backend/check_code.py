import io
import sys
import subprocess


test1_input = ["\"ski\"", "\"biz\"", "\"green \"", "\"pine \"", "\"Chirstmas \""]
test1 = """
def hello(i):
    i = i + "tree"
    l
    return len(i)

"""
#Finds the function name of thee user_defined code
def find_function_name(code) ->str:
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

def concat_args_function(function_name, input):
    test_lines = """"""
    for i in range(len(input)):
        test_lines = test_lines + "\n" + "print(" + function_name + "(" + input[i] + "))"
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
def check_code(code, input_arr, expected_output):
    function_name = find_function_name(code)
    if function_name == "":
        return False
    code = code + concat_args_function(function_name, input_arr)
    try:
        global_vars = {}
        local_vars = {}
        eval_code_rd_output = io.StringIO()
        eval_code_rd_err = io.StringIO()
        original_stdout = sys.stdout
        original_error = sys.stderr
        sys.stdout = eval_code_rd_output
        exec(code, global_vars, local_vars)
        printed_output = eval_code_rd_output.getvalue()
        printed_error = eval_code_rd_err.getvalue()
        sys.stdout = original_stdout
        sys.stderr = original_error
        print(printed_output)
        print("pass")
        print(local_vars)
        print(printed_error)

    except:
        print("HERE")
        return False
    
check_code(test1, test1_input, {})