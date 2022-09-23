# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

print("For Counter: ")

a = "aaaaaaaabbbbbccccc"
my_counter = Counter(a)

print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2)) # two of the most common in the dictionary

from collections import namedtuple

print("For namedtuple: ")

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict

print("For OrderedDict: ")

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict) # remembered the order of input

from collections import defaultdict

print("For defaultdict: ")

d = defaultdict(int)

d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)
print(d['d'])

from collections import deque # for double ended queue, it can be used to add or remove elements from both ends

print("For deque: ")

b = deque()
b.append(1)
b.append(2)

print(b)

b.appendleft(3)
b.append(4)

b.extendleft([5, 6, 7])
b.extend([9, 10])

print(b)

b.rotate(2) # use negative to rotate to the left side
print(b)
