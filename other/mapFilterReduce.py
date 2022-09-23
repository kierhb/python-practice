# map(), filter(), reduce()
'''
    map() = is used to run a function upon each item in an iterable item like list and create a new list with the same number of items,
            but the values of each item can be changed.

    map(function, sequence)
'''

mapnumbers1 = [1, 2, 3]
mapnumbers2 = [4, 5, 6]

print("For map():")

# for Function
def double(a):
    return a * 2

doubled_numbers = map(double, mapnumbers1)
print(list(doubled_numbers))

# for Lambda
triple = lambda b : b * 3

tripled_numbers = map(triple, mapnumbers2)
print(set(tripled_numbers))

quad_numbers = map(lambda c : c * 4, mapnumbers2)
print(list(quad_numbers))

'''
    filter() = takes an iterable and returns a filter object which is another iterable but without some of the original items, by returning True or False from
               the filtering function

    filter(function, sequence)
'''

fnumbers1 = [7, 8, 9, 10, 11, 12]

print("For filter():")

def isEven(n):
    return n % 2 == 0

even = filter(isEven, fnumbers1)
odd = filter(lambda m : m % 2 != 0, fnumbers1)

print(list(even))
print(list(odd))

'''
    reduce() = is used to calculate a value out of a sequence like a list

    reduce(function, sequence)
'''
from functools import reduce

print("For reduce():")

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

'''
sum = 0
for expense in expenses:
    sum += expense[1]
'''

sum = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum)