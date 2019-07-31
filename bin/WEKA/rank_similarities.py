import os
import re
from threading import Thread

class rank_similaritie(Thread):
    def __init__(self, ngram, number, destination):
        Thread.__init__(self)
        self.number = number
        self.ngram=ngram
        self.destination=destination

    def run(self):
        rank_similarities(self.ngram, self.number, self.destination)

def rank_similarities(ngram, thread, destination):
    listOfFiles = getListOfFiles(destination+"Files/")
    length=len(listOfFiles)//4
    if thread==1:
        listOfFiles=listOfFiles[:length]
        outfile=open(destination+str(ngram)+"_gram/"+"Ranking_step_1_","w")
    elif thread==2:
        listOfFiles=listOfFiles[length:2*length]
        outfile=open(destination+str(ngram)+"_gram/"+"Ranking_step_2_","w")
    elif thread==3:
        listOfFiles=listOfFiles[2*length:3*length]
        outfile=open(destination+str(ngram)+"_gram/"+"Ranking_step_3_","w")
    elif thread==4:
        listOfFiles=listOfFiles[3*length:]
        outfile=open(destination+str(ngram)+"_gram/"+"Ranking_step_4_","w")
    longueur=len(listOfFiles)
    for i in range (longueur-1):
        file1=(listOfFiles[i].replace(destination,"")).replace("//","/")
        for j in range (i+1,longueur):
            file2=(listOfFiles[j].replace(destination,"")).replace("//","/")
            count=0
            if file1.split(".")[-1]==file2.split(".")[-1]:
                count=0
                count_file1=0
                count_file2=0
                for line in open(destination+str(ngram)+"_gram/"+"sequence_list_by_files", "r"):
                    if file1 in line and file2 in line: 
                        splitedLine=line.split("__")
                        for files in splitedLine:
                            if file1 in files:
                                count_count_file1=int(files.split("::")[1],10)
                            if file2 in files:     
                                count_count_file2=int(files.split("::")[1],10)
                        if count_count_file1>=count_count_file2:
                            count+=count_count_file2
                        else:
                            count+=count_count_file1
                    if file1 in line:
                        splitedLine=line.split("__")
                        for files in splitedLine:
                            if file1 in files:
                                count_file1+=int(files.split("::")[1],10)
                    if file2 in line: 
                        splitedLine=line.split("__")
                        for files in splitedLine:
                            if file2 in files:
                                count_file2+=int(files.split("::")[1],10)
                if count_file1+count_file2-count==0:
                    print (file1)
                    print (count_file1)
                    print("\n")
                else:
                    value= int (100*count/ (count_file1+count_file2-count) *10)
                    outfile.write(str(float(value)/10)+'%'+"__"+file1+"__"+file2+"\n")
    return

def rank(ngram,destination):
    outfile7=open(destination+str(ngram)+"_gram/"+"Ranking","w")
    data=open(destination+str(ngram)+"_gram/"+"Ranking_step_5_").readlines()
    data0=[]
    data1=[]
    data2=[]
    for string in data:
        value=string.split("__")[0][:-1]
        value=re.sub('^([0-9]+)\.[0-9]+$', "\\1", value)
        inte=int(value,10)
        if inte < 10:
            data0+=[string]
        elif inte < 100:
            data1+=[string]
        else:
            data2+=[string]
    data0.sort()
    data1.sort()
    data2.sort()
    for i in range(len(data0)):
        outfile7.write(data0[i])
    for i in range(len(data1)):
        outfile7.write(data1[i])
    for i in range(len(data2)):
        outfile7.write(data2[i])
    return

def gather(ngram,destination):
    outfile6=open(destination+str(ngram)+"_gram/"+"Ranking_step_5_","w")
    for line in open(destination+str(ngram)+"_gram/"+"Ranking_step_1_", "r"):
        outfile6.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"Ranking_step_2_", "r"):
        outfile6.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"Ranking_step_3_", "r"):
        outfile6.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"Ranking_step_4_", "r"):
        outfile6.write(line)
    return

def remove(file):
    os.remove(file)
    return

def getListOfFiles(destination):
    listOfFiles=list()
    for path, subdirs, files in os.walk(destination):
        if len(files)!=0:
                for name in files:
                        listOfFiles+=[path+"/"+name]
    return listOfFiles

def main(destination, ngram):
# Création des threads
    thread_1 = rank_similaritie(ngram,1, destination)
    thread_2 = rank_similaritie(ngram,2, destination)
    thread_3 = rank_similaritie(ngram,3, destination)
    thread_4 = rank_similaritie(ngram,4, destination)

# Lancement des threads
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    gather(ngram,destination)
    rank(ngram,destination)

    for i in range(1,6):
        remove(destination+str(ngram)+"_gram/"+"Ranking_step_"+str(i)+"_")
