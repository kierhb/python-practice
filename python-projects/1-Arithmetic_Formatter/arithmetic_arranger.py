def function(a):
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
    
    print(opr)


function('82 - 3')