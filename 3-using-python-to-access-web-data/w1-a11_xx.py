#Finding Numbers in a Haystack
#    In this assignment you will read through and parse a file with text and numbers.
#    You will extract all the numbers in the file and compute the sum of the numbers.

#Handling The Data
#    The basic outline of this problem is to read the file, look for integers using
#    the re.findall(), looking for a regular expression of '[0-9]+' and then converting
#    the extracted strings to integers and summing up the integers.

import re

fname =  input('Enter file: ')
if len(fname) < 1:
    fname = 'regex_sum_1607117.txt'
fhand = open(fname)

numlist = list()

for lin in fhand:
    lin = lin.rstrip()
    rawnum = re.findall('([0-9]+)', lin)
    #for reviewing
    for i in rawnum:
        if i :
            i = int(i)
            numlist.append(i)

#s = 'A message from 02235123523684 to 45456459 about meeting 4587'

#li = list()
#rawnum = re.findall('\s([0-9]+)', s)

print(sum(numlist))