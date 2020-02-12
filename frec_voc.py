#! /usr/bin/env python3

''' Frequency vocabulary for a text file
    v 0.0.1 '''

import sys
import csv
import re

filename = sys.argv[1]
csvpath = filename[:-3] + "csv"
vocpath = filename[:-4] + "_voc" + filename[-4:]
dictonary = {}
filediscr = open(filename, 'r')

lines = filediscr.readlines()

for line in lines:
    r = re.findall('''(\w+(['-]+\w+)*'?)''', line)
    for rword in r:
        word = rword[0].lower()
        if word in dictonary.keys():
            dictonary[word] += 1
        else:
            dictonary[word] = 1

filediscr.close()

with open(vocpath, "w") as voc, open(csvpath, "w") as csvvoc:
    writer = csv.writer(csvvoc)
    for k,v in dictonary.items():
        outstr = f"{k:16}{v}\n"
        voc.write(outstr)
        writer.writerow([k,v])


#print(dictonary)
#print(sorted(dictonary))
#print([(i,dictonary[i]) for i in sorted(dictonary.keys(),key=dictonary.get)])
