import os
import re
from threading import Thread

class rank_similitude(Thread):
    def __init__(self, ngram,dirName, number):
        Thread.__init__(self)
        self.number = number
        self.ngram=ngram
        self.dirName=dirName

    def run(self):
        rank_similitudes(self.ngram, self.dirName, self.number)

def rank_similitudes(ngram, directory, thread):
    n=int(ngram[0],10)
    dirName = 'Files/modbat/'
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    length=len(listOfFiles)//4
    print("\n")
    if thread==1:
        print("hey, I'm thread 1, I'm working on : "+ngram[:-1] + " directory : "+directory[:-1])
        listOfFiles=listOfFiles[:length]
        outfile=open(ngram+directory+"Ranking_step_1_","w")
    elif thread==2:
        print("hey, I'm thread 2, I'm working on : "+ngram[:-1] + " directory : "+directory[:-1])
        listOfFiles=listOfFiles[length:2*length]
        outfile=open(ngram+directory+"Ranking_step_2_","w")
    elif thread==3:
        print("hey, I'm thread 3, I'm working on : "+ngram[:-1] + " directory : "+directory[:-1])
        listOfFiles=listOfFiles[2*length:3*length]
        outfile=open(ngram+directory+"Ranking_step_3_","w")
    elif thread==4:
        print("hey, I'm thread 4, I'm working on : "+ngram[:-1] + " directory : "+directory[:-1])
        listOfFiles=listOfFiles[3*length:]
        outfile=open(ngram+directory+"Ranking_step_4_","w")
    print("\n")
    longueur=len(listOfFiles)
    for i in range (longueur-1):
        file1=listOfFiles[i]
        for j in range (i+1,longueur):
            file2=listOfFiles[j]
            count=0
            if file1.split(".")[-1]==file2.split(".")[-1]:
                for line in open(ngram+directory+"sequence_list_by_files", "r"):
                    if file1 in line and file2 in line: 
                        splitedLine=line.split("__")
                        for files in splitedLine:
                            if file1 in files:
                                count_file1=int(files.split("::")[1],10)
                            if file2 in files:     
                                count_file2=int(files.split("::")[1],10)
                        if count_file1>=count_file2:
                            count+=count_file2/count_file1
                        else:
                            count+=count_file1/count_file2
            if count !=0:
                outfile.write(countPercentage(file1,file2,count,n)+"__"+file1+"__"+file2+"\n")
    return

def countPercentage(file1,file2,count,n):
    def return_number_n_grams (file):
        liste=open(file, 'r').read().split("\n")
        nGramsSeen=[]
        for i in range(len(liste)):
            liste[i]=liste[i].split()
        for j in range(len(liste)):
            line=liste[j]
            length_line=len(line)
            if n==1:
                for k in range(length_line):
                    nGramsSeen+=[line[k]+"\n"]
            elif n==2:
                if length_line>1:
                    for k in range(length_line-1):
                        nGramsSeen+=[line[k]+" "+line[k+1]+"\n"]
                elif length_line==1:
                    nGramsSeen+=[line[0]+" "+""+"\n"]

            elif n==3:
                if length_line>2:
                    for k in range(length_line-2):
                        nGramsSeen+=[line[k]+" "+line[k+1]+" "+line[k+2]+"\n"]
                elif length_line==2:
                    for k in range(length_line-1):
                        nGramsSeen+=[line[k]+" "+line[k+1]+" "+""+"\n"]
                elif length_line==1:
                    nGramsSeen+=[line[0]+" "+""+" "+""+"\n"]

            elif n==4:
                if length_line>3:
                    for k in range(length_line-3):
                        nGramsSeen+=[line[k]+" "+line[k+1]+" "+line[k+2]+" "+line[k+3]+"\n"]

                elif length_line==3:
                    for k in range(length_line-2):
                        nGramsSeen+=[line[k]+" "+line[k+1]+" "+line[k+2]+" "+""+"\n"]
                elif length_line==2:
                    for k in range(length_line-1):
                        nGramsSeen+=[line[k]+" "+line[k+1]+" "+""+" "+""+"\n"]
                elif length_line==1:
                    nGramsSeen+=[line[0]+" "+""+" "+""+" "+""+"\n"]
        nGramsSeen = list(dict.fromkeys(nGramsSeen))
        return (len(nGramsSeen))
    
    x=return_number_n_grams(file1)
    y=return_number_n_grams(file2)
    if x>=y:
        res=count*100/x
    else:
        res=count*100/y
    return (str(float(int(res*10))/10)+'%')

def rank(ngram,directory):
    outfile7=open(ngram+directory+"Ranking","w")
    data=open(ngram+directory+"Ranking_step_5_").readlines()
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

def gather(ngram,directory):
    outfile6=open(ngram+directory+"Ranking_step_5_","w")
    for line in open(ngram+directory+"Ranking_step_1_", "r"):
        outfile6.write(line)
    for line in open(ngram+directory+"Ranking_step_2_", "r"):
        outfile6.write(line)
    for line in open(ngram+directory+"Ranking_step_3_", "r"):
        outfile6.write(line)
    for line in open(ngram+directory+"Ranking_step_4_", "r"):
        outfile6.write(line)
    return

def remove(file):
    os.remove(file)
    return


def main(directory, ngrams, dirName_files):
    for dirName in dirName_files:
        for ngram in ngrams:
    # Création des threads
            thread_1 = rank_similitude(ngram,dirName,1)
            thread_2 = rank_similitude(ngram,dirName,2)
            thread_3 = rank_similitude(ngram,dirName,3)
            thread_4 = rank_similitude(ngram,dirName,4)

    # Lancement des threads
            thread_1.start()
            thread_2.start()
            thread_3.start()
            thread_4.start()

            thread_1.join()
            thread_2.join()
            thread_3.join()
            thread_4.join()

            gather(ngram,dirName)
            rank(ngram,dirName)

            for i in range(1,6):
                remove(ngram+dirName+"Ranking_step_"+str(i)+"_")
