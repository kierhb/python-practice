#7.1 Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fhandle = open('mbox-short.txt')

for xline in fhandle:
    yline = xline.rstrip()
    print(yline.upper())