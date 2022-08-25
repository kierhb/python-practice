def arithmetic_arranger(problems, solver = False):
    #Checking for problems
    if len(problems) > 5:
        return "Error: Too many problems"

    first_operand = []
    second_operand = []
    operator = []

    for problem in problems:
        parts = problem.split()
        first_operand.append(parts[0])
        second_operand.append(parts[2])
        operator.append(parts[1])
    
    #Checking Operation
    if '*' in operator or '/' in operator:
        return "Error: Operator must be '+' or '-'"

    #Checking Digits
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits"

    #Checking Width
    for i in range(len(first_operand)):
        if len(first_operand) > 4 < len(second_operand):
            return "Error: Numbers cannot be more than four digits"
    
    #Start of Operation
    first_row = []
    second_row = []
    third_row = []
    fourth_row = []

    # For First Row
    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            first_row.append(" " + first_operand[i])
        else:
            first_row.append(" " * (len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

    # For Second Row
    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            second_row.append(operator[i] + " " + second_operand[i])
        else:
            second_row.append(operator[i] + " " * (len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

    # For Third Row (Dashes)
    for i in range(len(first_operand)):
        third_row.append("-" * (max(len(first_operand[i]), len(second_operand[i])) + 2))

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])