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
        if match := re.search(r"([a-z0-9]+)\s([+, -])\s([a-z0-9]+)", problem):
        
            first_operand.append(match.group(1))
            second_operand.append(match.group(3))
            operators.append(match.group(2))


            # Checking Operation
            '''
                The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
            '''
            if '*' in operators or '/' in operators:
                return "Error: Operator must be '+' or '-'"


            # Checking Digits
            '''
                Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
            '''
            for i in range(len(first_operand)):
                if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
                    return "Error: Numbers must only contain digits"
            

            # Checking Width
            '''
                Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
            '''
            for i in range(len(first_operand)):
                if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
                    return "Error: Numbers cannot be more than four digits"


    print(first_operand)
    #print(operators)
    #print(second_operand)




print(arithmetic_arranger(["2 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))