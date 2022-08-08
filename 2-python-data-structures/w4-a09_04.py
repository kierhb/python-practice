#9.4 Write a program to read through the mbox-short.txt and figure out who has 
#    sent the greatest number of mail messages. The program looks for 'From ' lines and
#    takes the second word of those lines as the person who sent the mail. The program
#    creates a Python dictionary that maps the sender's mail address to a count of the
#    number of times they appear in the file. After the dictionary is produced, the
#    program reads through the dictionary using a maximum loop to find the most prolific
#    committer.

fname = input('Enter file: ')

if len(fname) < 1:
    fname = 'mbox-short.txt'

fhand = open(fname)

di = dict()

for lin in fhand:
    lin = lin.rstrip()
    if not lin.startswith('From: '):
        continue
    lin = lin.lstrip('From: ')
    words = lin.split()
    for word in words:
        #print('**',word,di.get(word,-99))
        #if word in di:
        #    di[word] = di[word] + 1
        #else:
        #    di[word] = 1
        di[word] = di.get(word,0) + 1

#print(di.items())
highest = -1
corword = None
for k,v in di.items():
    #print(k,v)
    if v > highest:
        highest = v
        corword = k

print(corword, highest)