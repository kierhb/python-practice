import re

def arithmetic_arranger(problems, solver = False):
    # Checker for problems
    if len(problems) > 5:
        '''
            If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
        '''
        return "Error: Too many problems"

    
print(arithmetic_arranger(["2 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))