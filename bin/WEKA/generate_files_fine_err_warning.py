import os
import re
from shutil import copyfile
import sys
def creationFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def cloneFilesFromOriginToDestination(destination,origin,extension):
    creationFolder(destination)
    creationFolder(destination+"OriginalFiles/")
    for path, subdirs, files in os.walk(origin):
        for name in files:
            file=path+"/"+name
            if file.split(".")[-1] in extension:
                if os.path.exists(destination+"OriginalFiles/"+((path+"/"+name).replace(origin,"")).replace("/","_")):
                    sys.exit("You can't overwrite the folder \"OriginalFiles\". To replace it, you have to delete the whole folder")
                else:
                    copyfile(file, destination+"OriginalFiles/"+((path+"/"+name).replace(origin,"")).replace("/","_"))

def getListOfFiles(destination):
    listOfFiles=list()
    for path, subdirs, files in os.walk(destination+"OriginalFiles/"):
        for file in files:    
            listOfFiles+=[file]
    return listOfFiles

def main(destination,origin, extension):
    cloneFilesFromOriginToDestination(destination,origin,extension)
    creationFolder(destination+"Files/")
    ListOfFiles=getListOfFiles(destination)
    num=1
    for file in ListOfFiles:
        num+=1
        outfile1=open((destination+"Files/"+file)+".info","w")
        outfile2=open((destination+"Files/"+file)+".warning","w")
        outfile3=open((destination+"Files/"+file)+".debug","w")
        outfile4=open((destination+"Files/"+file)+".fine","w")
        outfile5=open((destination+"Files/"+file)+".error","w")
        outfile6=open((destination+"Files/"+file)+".raw","w")
        for line in open(destination+"OriginalFiles/"+file, 'r') :

            if re.match("^.*INFO.*$", line): 
                outfile1.write(line)
            
            elif re.match("^.*WARNING.*$", line): 
                outfile2.write(line)


            elif re.match("^.*DEBUG.*$", line): 
                outfile3.write(line)


            elif re.match("^.*FINE.*$", line): 
                outfile4.write(line)
            
            elif re.match("^.*ERROR.*$", line): 
                outfile5.write(line)

            else:
                outfile6.write(line)
        