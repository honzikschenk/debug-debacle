import io
import sys
import subprocess

test1_input = {'x': 5}
test1 = """
def hello():
    for i in range(5):
        print(i)

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

#REQUIREMENTS
#PRE:
#   CODE: in multi-line string
#   INPUT: array in format [ [testcase1], [testcase2], [testcase3]]
#   with each testcase being a new entry into the data
#   the data being organized in the following manner:
#   [testcase1] = [[param1], [param2], [param3]] etc.
#   EXPECTED_OUTPUT: array of outputs in the format:
#   [data] = [[answer_testcase1], [answer_testcase2], [answer_testcase3]] etc.
#POST returns a boolean value
#   True if all testcases past
#   False if anything fails
def check_code(code, input_arr, expected_output):
    function_name = find_function_name(code)
    if function_name == "":
        return False
    test_line = concat_args_function(function_name, input)
    try:
        
        global_vars = input
        local_vars = {}
        eval_code_rd_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = eval_code_rd_output
        eval(code, global_vars, local_vars)
        printed_output = eval_code_rd_output.getvalue()
        sys.stdout = original_stdout
    except:
        return False
    
f1 = find_function_name(test1)
f1 = f1 +"()"
code = test1 + "\n" + f1
exec(code)