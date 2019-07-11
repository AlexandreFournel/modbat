## this function remove useless words in folder/word_list
#For the moment, we are only working on the "modbat" folder. We generate a file (called word_list3. This file is used by generate_doc_arff)
#be careful, I don't really know why, but in word_liost3, RangeESC appears. The filtering to remove escape sequences don't work at all. So you have to remove by yourself the RangeESC from word_list3

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