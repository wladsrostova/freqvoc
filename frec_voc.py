#! /usr/bin/env python

''' Frequency vocabulary for a text file
    v 0.0.1 '''

import sys

dictonary = {}
filename = sys.argv[1]
filediscr = open(filename, 'r')

lines = filediscr.readlines()
for line in lines:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        #print(word)
        if word in dictonary.keys():
            dictonary[word] += 1
        else:
            dictonary[word] = 1

#print(dictonary)
#print(sorted(dictonary))
print([(i,dictonary[i]) for i in sorted(dictonary.keys(),key=dictonary.get)])
