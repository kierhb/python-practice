import re

def arithmetic_arranger(problems, solver = False):
    # Checker for problems
    if len(problems) > 5:
        '''
            If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
        '''
        return "Error: Too many problems."


    first_operand = []
    second_operand = []
    operators = []


    for problem in problems:
        if match := re.search(r"([a-z0-9]+)\s([\+, \-, \*, \/])\s([a-z0-9]+)", problem):
        
            first_operand.append(match.group(1))
            second_operand.append(match.group(3))
            operators.append(match.group(2))


    # Checking Operation
    '''
        The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    '''
    if '*' in operators or '/' in operators:
        return "Error: Operator must be '+' or '-'."


    # Checking Digits
    '''
        Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
    '''
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits."
            

    # Checking Width
    '''
        Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    '''
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."


    # Start of Operation
    first_row = []
    second_row = []
    third_row = []
    fourth_row = []
    digits = []
    dash_length = []

    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            digit = len(first_operand[i])
        else:
            digit = len(second_operand[i])
        digits.append(digit)


    # For First Row:
    for i in range(len(first_operand)):
        if digits[i] == 1:
            first_row.append(f"  {first_operand[i]:>1}")
        elif digits[i] == 2:
            first_row.append(f"  {first_operand[i]:>2}")
        elif digits[i] == 3:
            first_row.append(f"  {first_operand[i]:>3}")
        elif digits[i] == 4:
            first_row.append(f"  {first_operand[i]:>4}")


    # For Second Row:
    for i in range(len(first_operand)):
        if digits[i] == 1:
            second_row.append(f"{operators[i]} {second_operand[i]:>1}")
        elif digits[i] == 2:
            second_row.append(f"{operators[i]} {second_operand[i]:>2}")
        elif digits[i] == 3:
            second_row.append(f"{operators[i]} {second_operand[i]:>3}")
        elif digits[i] == 4:
            second_row.append(f"{operators[i]} {second_operand[i]:>4}")


    # For Third Row:
    for i in range(len(first_operand)):
        dash = "-" * digits[i]
        third_row.append(f"--{dash}")

    for x in third_row:
        dash_length.append(len(x))


    # For Fourth Row:
    for i in range(len(first_operand)):
        if operators[i] == '+':
            answer = int(first_operand[i]) + int(second_operand[i])
        else:
            answer = int(first_operand[i]) - int(second_operand[i])
        # Append to Fourth Row
        if dash_length[i] == 1:
            fourth_row.append(f"{str(answer):>1}")
        elif dash_length[i] == 2:
            fourth_row.append(f"{str(answer):>2}")
        elif dash_length[i] == 3:
            fourth_row.append(f"{str(answer):>3}")
        elif dash_length[i] == 4:
            fourth_row.append(f"{str(answer):>4}")
        elif dash_length[i] == 5:
            fourth_row.append(f"{str(answer):>5}")
        elif dash_length[i] == 6:
            fourth_row.append(f"{str(answer):>6}")
        

    if solver:
        arranged = "    ".join(first_row) + "\n" + "    ".join(second_row) + "\n" + "    ".join(third_row) + "\n" + "    ".join(fourth_row)
    else:
        arranged = "    ".join(first_row) + "\n" + "    ".join(second_row) + "\n" + "    ".join(third_row)
           
    return arranged
    

print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'], True))