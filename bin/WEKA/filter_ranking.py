import re
import os
from threading import Thread
import sys

def filters(file1,file2, ngram, destination):
    extension=["debug", "info", "error", "warning", "fine", "raw"]
    res=[0,0,0,0,0,0]

    for i in range(0, len(extension)):
        if os.path.isfile(destination+file1+"."+extension[i]) and os.path.isfile(destination+file2+"."+extension[i]):
            for line in open(destination+ngram+"/"+"Ranking", "r"):
                if file1+"."+extension[i] in line and file2+"."+extension[i] in line:
                    res[i]=int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10
        elif os.path.isfile(destination+"Files/"+file1+"."+extension[i])==False and os.path.isfile(destination+"Files/"+file2+"."+extension[i])==False:
            res[i]=-2
        else:
            res[i]=-1
    return (res)

def getListOfNgram(destination):
    return ([name for name in os.listdir(destination) if (os.path.isdir(destination+"/"+name) and "gram" in name)])

def filtering(destination, thread, percentage):
    listOfFiles = getListOfFiles(destination+"OriginalFiles/")
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
            total=0
            file1=(listOfFiles[i].replace(destination,"")).replace("//","/")
            file2=(listOfFiles[j].replace(destination,"")).replace("//","/")
            for ngram in getListOfNgram(destination):
                file1=(file1).replace("OriginalFiles","Files")
                file2=(file2).replace("OriginalFiles","Files")
                res=filters(file1,file2, ngram, destination)
                totalForNgram=sum(res)
                inter=0
                for h in res:
                    if h==-1:
                        inter=-1
                if inter==0:
                    totalForNgram=0
                    nb_superior_to_zero=0
                    for k in res:
                        if k>0:
                            totalForNgram+=k
                            nb_superior_to_zero+=1
                    if nb_superior_to_zero!=0:
                        total += totalForNgram/nb_superior_to_zero
            if total/len(getListOfNgram(destination))>float(percentage):
                if file1!=file2:
                    print(file1)
                    print  ("has "+str(total/len(getListOfNgram(destination)))+" of similitudes with")
                    print(file2)
                    print("\n")

class launch_threading(Thread):
    def __init__(self,destination, number,percentage):
        Thread.__init__(self)
        self.number = number
        self.destination=destination
        self.percentage=percentage

    def run(self):
        filtering(self.destination, self.number, self.percentage)

def getListOfFiles(destination):
    listOfFiles=list()
    for path, subdirs, files in os.walk(destination):
        if len(files)!=0:
                for name in files:
                        listOfFiles+=[path+"/"+name]
    return listOfFiles

def main(destination, percentage):
    print("\n")
    thread_1 = launch_threading(destination,1,percentage)
    thread_2 = launch_threading(destination,2,percentage)
    thread_3 = launch_threading(destination,3,percentage)
    thread_4 = launch_threading(destination,4,percentage)

    # Lancement des threads
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()




