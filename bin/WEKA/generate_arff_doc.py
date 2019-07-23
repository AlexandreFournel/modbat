import os
import csv
import re
from threading import Thread


class generate_arff(Thread):
    def __init__(self, ngram,dirName,directory, number):
        Thread.__init__(self)
        self.number = number
        self.ngram=ngram
        self.dirName=dirName
        self.directory=directory

    def run(self):
        generate_arff_doc(self.ngram, self.dirName, self.directory, self.number)

def count(file, ngram, dirName):
    sequence_file=open(ngram+dirName+"sequence_list",'r')
    sequence_list  = sequence_file.readlines()
    sequence_dict=dict()
    for sequence in sequence_list:
        sequence_dict[str(sequence.replace("\n",""))]=0
    n=int(ngram[0],10)
    liste=open(file, 'r').read().split("\n")
    for i in range(len(liste)):
        liste[i]=liste[i].split()
    for j in range(len(liste)):
        line=liste[j]
        length_line=len(line)
        if n==1:
            for k in range(length_line):
                if str(line[k]) in sequence_dict:
                    count=sequence_dict.get(str(line[k]))
                    del sequence_dict[str(line[k])]
                    sequence_dict[str(line[k])]=count+1
                else:
                    print("Not FOund")
        elif n==2:
            if length_line>1:
                for k in range(length_line-1):
                    if str(line[k])+" "+str(line[k+1]) in sequence_dict:
                        count=sequence_dict.get(str(line[k])+" "+str(line[k+1]))
                        del sequence_dict[str(line[k])+" "+str(line[k+1])]
                        sequence_dict[str(line[k])+" "+str(line[k+1])]=count+1
                    else:
                        print("Not Found")
            elif length_line==1:
                if str(line[0])+" "+"" in sequence_dict:
                    count=sequence_dict.get(str(line[0])+" "+"")
                    sequence_dict[str(line[0])+" "+""]=count+1
                else:
                    print("Not Found")
        elif n==3:
            if length_line>2:
                for k in range(length_line-2):
                    if str(line[k])+" "+str(line[k+1])+" "+str(line[k+2]) in sequence_dict:
                        count=sequence_dict.get(str(line[k])+" "+str(line[k+1])+" "+str(line[k+2]))
                        del sequence_dict[str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])]
                        sequence_dict[str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])]=count+1
                    else:
                        print("Not Found")
            elif length_line==2:
                for k in range(length_line-1):
                    if str(line[k]+" "+line[k+1]+" "+"") in sequence_dict:
                        count=sequence_dict.get(str(line[k])+" "+str(line[k+1])+" "+"")
                        del sequence_dict[str(line[k])+" "+str(line[k+1])+" "+""]
                        sequence_dict[str(line[k])+" "+str(line[k+1])+" "+""]=count+1
                    else:
                        print("Not Found")
            elif length_line==1:
                if str(line[0])+" "+""+" "+"" in sequence_dict:
                    count=sequence_dict.get(str(line[0])+" "+""+" "+"")
                    del sequence_dict[str(line[0])+" "+""+" "+""]
                    sequence_dict[str(line[0])+" "+""+" "+""]=count+1
                else:
                    print("Not Found")

        elif n==4:
            if length_line>3:
                for k in range(length_line-3):
                    if str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+str(line[k+3]) in sequence_dict:
                        count=sequence_dict.get(str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+str(line[k+3]))
                        del sequence_dict[str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+str(line[k+3])]
                        sequence_dict[str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+str(line[k+3])]=count+1
                    else:
                        print("Not Found")

            elif length_line==3:
                for k in range(length_line-2):
                    if str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+"" in sequence_dict:
                        count=sequence_dict.get(str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+"")
                        del sequence_dict[str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+""]
                        sequence_dict[str(line[k])+" "+str(line[k+1])+" "+str(line[k+2])+" "+""]=count+1
                    else:
                        print("Not Found")
            elif length_line==2:
                for k in range(length_line-1):
                    if str(line[k])+" "+str(line[k+1])+" "+""+" "+"" in sequence_dict:
                        count=sequence_dict.get(str(line[k])+" "+str(line[k+1])+" "+""+" "+"")
                        del sequence_dict[str(line[k])+" "+str(line[k+1])+" "+""+" "+""]
                        sequence_dict[str(line[k])+" "+str(line[k+1])+" "+""+" "+""]=count+1
                    else:
                        print("Not Found")
            elif length_line==1:
                if str(line[0])+" "+""+" "+""+" "+"" in sequence_dict:
                    count=sequence_dict.get(str(line[0])+" "+""+" "+""+" "+"")
                    del sequence_dict[str(line[0])+" "+""+" "+""+" "+""]
                    sequence_dict[str(line[0])+" "+""+" "+""+" "+""]=count+1
                else:
                    print("Not Found")
    return (sequence_dict)

def generate_arff_doc(ngram,dirName,directory,thread):

    sequence_file=open(ngram+dirName+"sequence_list",'r')
    sequence_list  = sequence_file.readlines()

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(directory):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    with open(ngram+dirName+"sequences_occurences_5","w") as fd:
        fd.write("@relation "+ngram[:-1])
        fd.write("\n")
        fd.write("\n")
        fd.write("@attribute fileNames string")
        fd.write("\n")
        for sequence in sequence_list:
            fd.write("@attribute "+((sequence.replace(',', '_')).replace('\n', '')).replace(" ","__")+" numeric\n")
        iter=0
        fd.write("\n")
        fd.write("@data")
        fd.write("\n")
    longueur=len(listOfFiles)//4

    if thread==1:
        listOfFiles=listOfFiles[:longueur]
        outfile=open(ngram+dirName+"sequences_occurences_1","w")
    elif thread==2:
        listOfFiles=listOfFiles[longueur:2*longueur]
        outfile=open(ngram+dirName+"sequences_occurences_2","w")
    elif thread==3:
        listOfFiles=listOfFiles[2*longueur:3*longueur]
        outfile=open(ngram+dirName+"sequences_occurences_3","w")
    elif thread==4:
        listOfFiles=listOfFiles[3*longueur:]
        outfile=open(ngram+dirName+"sequences_occurences_4","w")

    sequence_dict=dict()
    for file in listOfFiles:
        iter+=1
        print(str(iter)+"/"+str(longueur))
        sequence_dict = count(file,ngram,dirName)
        newline = "\'"+file+"\'"
        sequence_file=open(ngram+dirName+"sequence_list",'r')
        sequence_list  = sequence_file.readlines()
        for sequence in sequence_list:
            newline=newline+","+str(sequence_dict.get(str(sequence.replace("\n",""))))
        outfile.write(newline.replace('\n', '')+"\n")

def gather(ngram,dirName):
    outfile=open(ngram+dirName+"sequences_occurences.arff","w")
    for line in open(ngram+dirName+"sequences_occurences_5", "r"):
        outfile.write(line)
    for line in open(ngram+dirName+"sequences_occurences_1", "r"):
        outfile.write(line)
    for line in open(ngram+dirName+"sequences_occurences_2", "r"):
        outfile.write(line)
    for line in open(ngram+dirName+"sequences_occurences_3", "r"):
        outfile.write(line)
    for line in open(ngram+dirName+"sequences_occurences_4", "r"):
        outfile.write(line)
    return

def remove(file):
    os.remove(file)
    return

def main(directory, ngrams, dirName_files):
    for dirName in dirName_files:
        for ngram in ngrams:
            thread_1 = generate_arff(ngram,dirName,directory+dirName,1)
            thread_2 = generate_arff(ngram,dirName,directory+dirName,2)
            thread_3 = generate_arff(ngram,dirName,directory+dirName,3)
            thread_4 = generate_arff(ngram,dirName,directory+dirName,4)

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

            for i in range(1,6):
                remove(ngram+dirName+"sequences_occurences_"+str(i))
