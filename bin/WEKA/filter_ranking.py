import re
import os
from threading import Thread
import sys

def filters(file1,file2, ngram, directory):
    extension=["debug", "info", "error", "warning", "fine", "raw"]
    res=[0,0,0,0,0,0]

    for i in range(0, len(extension)):
        if os.path.isfile(file1+"."+extension[i]) and os.path.isfile(file2+"."+extension[i]):
            for line in open(ngram+directory+"Ranking", "r"):
                if file1 in line and file2 in line:
                    res[i]=int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10
        elif os.path.isfile(file1+"."+extension[i])==False and os.path.isfile(file2+"."+extension[i])==False:
            res[i]=-2
        else:
            res[i]=-1
    return (res)

def filtering(ngram, dirName, dirName_files, thread, percentage):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName_files):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    for i in range(len(listOfFiles)):
        listOfFiles[i]=listOfFiles[i].rsplit(".",1)[0]
    list(set(listOfFiles)) 
    length=len(listOfFiles)
    
    if thread==1:
        lowLimit=0
        highLimit=length//4
    elif thread==2:
        lowLimit=length//4
        highLimit=2*length//4
    elif thread==3:
        lowLimit=2*length//4
        highLimit=3*length//4
    elif thread==4:
        lowLimit=3*length//4
        highLimit=length

    for i in range(lowLimit,highLimit):
        for j in range(i+1,length):
            res=filters(listOfFiles[i],listOfFiles[j], ngram, dirName)
            total=sum(res)
            inter=0
            for h in res:
                if h==-1:
                    inter=-1
            if inter==0:
                total=0
                nb_superior_to_zero=0
                for k in res:
                    if k>0:
                        total+=k
                        nb_superior_to_zero+=1
                if nb_superior_to_zero!=0:
                    if total/nb_superior_to_zero>float(percentage):
                        print(listOfFiles[i])
                        print(listOfFiles[j])
                        print("\n")

class launch_threading(Thread):
    def __init__(self, n_grams,dirName,dirName_files, number,percentage):
        Thread.__init__(self)
        self.number = number
        self.n_grams=n_grams
        self.dirName=dirName
        self.dirName_files=dirName_files
        self.percentage=percentage

    def run(self):
        filtering(self.n_grams, self.dirName, self.dirName_files, self.number, self.percentage)

def main(directory, ngrams, dirName_files,percentage):
    for dirName in dirName_files:
        for ngram in ngrams:
            thread_1 = launch_threading(ngram,dirName,directory+dirName,1,percentage)
            thread_2 = launch_threading(ngram,dirName,directory+dirName,2,percentage)
            thread_3 = launch_threading(ngram,dirName,directory+dirName,3,percentage)
            thread_4 = launch_threading(ngram,dirName,directory+dirName,4,percentage)

            # Lancement des threads
            thread_1.start()
            thread_2.start()
            thread_3.start()
            thread_4.start()

            thread_1.join()
            thread_2.join()
            thread_3.join()
            thread_4.join()




