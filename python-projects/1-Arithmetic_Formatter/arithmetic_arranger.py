def ar_ar(a):
    #Trial
    if len(a) >= 5:
        set1 = a.split()
        #First Number
        a1 = set1[0]
        if isinstance(int(set1[0]), int) == True:
            a1 = int(set1[0])

        #Second Number
        b1 = set1[2]
        if isinstance(int(set1[2]), int) == True:
            b1 = int(set1[2])

        #Operation
        c1 = set1[1]
        if c1 == '+':
            opr = a1 + b1
        elif c1 == '-':
            opr = a1 - b1
        else:
            opr = 'abort'
    else:
        print('Error: Too many problems')

    print('  ', a1)
    print('+ ', b1)
    print('----')

    if len(a1) == 

    print(opr)

ar_ar('235 - 52')

def arithmetic_arranger(problems):
    #Checking for problems
    if len(problems) > 5:
        print('Error: Too many problems')

    first_operand = []
    second_operand = []
    operator = []

    for problem in problems:
        parts = problem.split[]
        first_operand.append(parts[0])
        second_operand.append(parts[2])
        operator.append(parts[1])

    