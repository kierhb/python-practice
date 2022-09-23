# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
print("for product: ")
# use to compute the cartesian product of iterables

a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod))

from itertools import permutations
print("for permutations: ")
# will return all possible orderings of an input

c = [1, 2, 3]
perm = permutations(c)
print(list(perm))

from itertools import combinations
print("for combinations: ")
# will make all possible combinations with a specified length

d = [1, 2, 3, 4]
comb = combinations(d, 2)

print(list(comb))

from itertools import accumulate
print("for accumulate: ")
# makes an iterator that returns accumulated sums, or other binary functions
import operator

e = [1, 2, 3, 4]
acc = accumulate(e)

print(e)
print(list(acc))

acc = accumulate(e, func = operator.mul)
print(list(acc))

from itertools import groupby
print("for groupby: ")
# makes an iterator that returns keys and groups from interable

def smaller_than_3(x):
    return x < 3

g = [1, 2, 3, 4]
group_obj = groupby(g, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat
print("for infinite iterators: ")

print("count:")
for i in count(10):
    print(i)
    if i == 15:
        break
'''
print("cycle:")
j = [1, 2, 3]
for i in cycle(j):
    print(i)
'''

print('repeat:')

for i in repeat(1, 5):
    print(i)
