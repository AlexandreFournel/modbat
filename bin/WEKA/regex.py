import re
import os
import csv


def isLineEmpty(line):
    return len(line.strip()) == 0

fh=open("Files/modbat/word_list",'r')
fd=open("word_list3",'w')
for line in fh:
    newline=line
    newline=re.sub('^[0-9]+$', '', newline)
    newline=re.sub('^[0-9]+[a-f]+.*$', '', newline)
    newline=re.sub('^[a-f]+[0-9]+.*$', '', newline)
    newline=re.sub('^[0-9]\.[0-9]+$', '', newline)
    if isLineEmpty(newline)==False:
        fd.write(newline)