import sys
import re
import os

def getListOfNgram(destination):
    return ([name for name in os.listdir(destination) if (os.path.isdir(destination+"/"+name) and "gram" in name)])

def main(file1,file2, destination):
    file1=(file1.replace(destination,"")).replace("OriginalFiles","Files")
    file2=(file2.replace(destination,"")).replace("OriginalFiles","Files")
    print("\n")
    for ngram in getListOfNgram(destination):
        extension=["debug", "info", "error", "warning", "fine", "raw"]
        res=[0,0,0,0,0,0]

        for i in range(0, len(extension)):
            if os.path.isfile(destination+file1+"."+extension[i]) and os.path.isfile(destination+file2+"."+extension[i]):
                for line in open(destination+ngram+"/"+"Ranking", "r"):
                    
                    if file1+"."+extension[i] in line and file2+"."+extension[i] in line:
                        res[i]=int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10
            elif os.path.isfile(destination+file1+"."+extension[i])==False and os.path.isfile(destination+file2+"."+extension[i])==False:
                res[i]="-Doesn't exist-"
            else:
                res[i]="- One file exist, not the second one"
        for j in range(0, len(extension)):
            print (ngram+" -> "+extension[j]+"="+str(res[j]))
        print("\n") 
    return