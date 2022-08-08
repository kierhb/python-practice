#10.2 Write a program to read through the mbox-short.txt and figure out the
#     distribution by hour of the day for each of the messages. You can pull the hour out
#     from the 'From ' line by finding the time and then splitting the string a second time
#     using a colon.

#     From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#     Once you have accumulated the counts for each hour, print out the counts, sorted
#     by hour as shown below.

fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)

li = list()
di = dict()
for lin in fhand:
    lin = lin.rstrip()
    if not lin.startswith('From '):
        continue
    word = lin.split()
    time = word[5]
    #Times were extracted
    timesplt = time.split(':')
    hour = timesplt[0]
    #Hours were extracted
    li.append(hour)

#Make into dictionary
for line in li:
    di[line] = di.get(line,0) + 1

lst = []
for k,v in sorted(di.items()):
    print(k,v)
