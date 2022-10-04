import re

def arithmetic_arranger(problems, solver = False):
    # Checker for problems
    if len(problems) > 5:
        '''
            If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
        '''
        return "Error: Too many problems"


    first_operand = []
    second_operand = []
    operators = []


    for problem in problems:
        if match := re.search(r"([0-9]+)\s([+, -])\s([0-9]+)", problem):
            # Checking Operation
            '''
                The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
            '''
            operators.append(match.group(2))
            if '*' in operators or '/' in operators:
                return "Error: Operator must be '+' or '-'"




    return operators



print(arithmetic_arranger(["2 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))