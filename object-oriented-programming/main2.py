'''
https://www.youtube.com/watch?v=FIaPZXaePhw
'''

class CustomizedInteger:
    def __init__(self, integer):
        self.integer = integer

    # __str__ should return a more prettier representation(easier to understand)
    def __str__(self):
        if self.integer == 4:
            return "Four"

    # __repr__ should returns formal way(what it should look like in code)
    def __repr__(self):
        return f'CustomizeInteger({self.integer})'

int1 = CustomizedInteger(4)
print(int1)