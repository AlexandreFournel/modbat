import sys
import re
import os
##debug
def main(file1,file2, ngrams, dirName):
    print("\n")
    for directory in dirName:
        for ngram in ngrams:
            extension=["debug", "info", "error", "warning", "fine", "raw"]
            res=[0,0,0,0,0,0]

            for i in range(0, len(extension)):
                if os.path.isfile(file1+"."+extension[i]) and os.path.isfile(file2+"."+extension[i]):
                    for line in open(ngram+directory+"Ranking", "r"):
                        if file1 in line and file2 in line:
                            res[i]=int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10
                elif os.path.isfile(file1+"."+extension[i])==False and os.path.isfile(file2+"."+extension[i])==False:
                    res[i]="-Doesn't exist-"
                else:
                    res[i]="- One file exist, not the second one"
            for j in range(0, len(extension)):
                print (ngram+" -> "+extension[j]+"="+str(res[j]))
            print("\n") 
        return