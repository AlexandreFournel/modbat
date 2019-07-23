## this function remove useless lines in Files/
# We want to remove : empty lines and all seeds without prefix

import re
import os
import csv

dirName = 'Files/'

def isLineEmpty(line):
    return len(line.strip()) == 0

def giveListOfFiles(subDirName):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName+subDirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return listOfFiles

def removeEmptyFiles(listOfFiles):
    for file in listOfFiles:
        if os.stat(file).st_size == 0:
            os.remove(file)
    return

def regex(listOfFiles):
    for file in listOfFiles:
        readFile=open(file,"r")
        writeFile=open(file+"copy","w")
        for line in readFile:
            newline=line
            newline=re.sub('^[ \t]*[0-9]*[ \t]*[0-9]+[a-f]+.*$', '', newline)
            newline=re.sub('^[ \t]*[0-9]*[ \t]*[a-f]+[0-9]+.*$', '', newline)
            if isLineEmpty(newline)==False:
                writeFile.write(newline)
        copy_remove(file)

def copy_remove(file):
    os.remove(file)
    os.rename(file+"copy",file)
    return

def subMain(subDirNameList):
    for subDirName in subDirNameList:
        listOfFiles=giveListOfFiles(subDirName)
        regex(listOfFiles)
        removeEmptyFiles(listOfFiles)
    return

def main(subDirName):
    subMain(subDirName)
