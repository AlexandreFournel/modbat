import os
import csv
import re
from threading import Thread


class generate_arff(Thread):
    def __init__(self, ngram,destination, number):
        Thread.__init__(self)
        self.number = number
        self.ngram=ngram
        self.destination=destination

    def run(self):
        generate_arff_doc(self.ngram, self.destination, self.number)

def count(file, ngram,destination):
    sequence_file=open(destination+str(ngram)+"_gram/"+"sequence_list",'r')
    sequence_list  = sequence_file.readlines()
    sequence_dict=dict()
    for sequence in sequence_list:
        sequence_dict[str(sequence.replace("\n",""))]=0
    n=int(ngram[0],10)
    liste=open(destination+file.replace("//","/"), 'r').read().split("\n")
    for i in range(len(liste)):
        liste[i]=liste[i].split()
    for j in range(len(liste)):
        line=liste[j]
        length_line=len(line)

        if length_line>=n:
            for k in range(length_line-(n-1)):
                
                sequenceOfWords=str(line[k])
                for i in range(1,n):
                    sequenceOfWords=sequenceOfWords+" "+str(line[k+i])
                if sequenceOfWords.replace("\n","") in sequence_dict:
                    count=sequence_dict.get(sequenceOfWords.replace("\n",""))
                    del sequence_dict[sequenceOfWords.replace("\n","")]
                    sequence_dict[sequenceOfWords.replace("\n","")]=count+1
                else:
                    print("Problem  : Not Found1")
        elif length_line!=0:
            sequenceOfWords=str(line[0])
            for i in range(1,n):
                if i>=length_line:
                    sequenceOfWords=sequenceOfWords+" "+""
                else:
                    sequenceOfWords=sequenceOfWords+" "+str(line[i])

            if sequenceOfWords in sequence_dict:
                count=sequence_dict.get(sequenceOfWords)
                del sequence_dict[sequenceOfWords]
                sequence_dict[sequenceOfWords]=count+1
            else:
                print("Problem  : Not Found2")   

    return (sequence_dict)

def generate_arff_doc(ngram,destination,thread):

    sequence_file=open(destination+str(ngram)+"_gram/"+"sequence_list",'r')
    sequence_list  = sequence_file.readlines()

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(destination+"Files/")

    with open(destination+str(ngram)+"_gram/"+"sequences_occurences_5","w") as fd:
        fd.write("@relation "+str(ngram)+"_gram/")
        fd.write("\n")
        fd.write("\n")
        fd.write("@attribute fileNames string")
        fd.write("\n")
        for sequence in sequence_list:
            fd.write("@attribute "+"\""+(sequence.replace('\n', '')).replace("\"","\\\"")+"\""+" numeric\n")
        iter=0
        fd.write("\n")
        fd.write("@data")
        fd.write("\n")
    longueur=len(listOfFiles)//4

    if thread==1:
        listOfFiles=listOfFiles[:2]
    #    listOfFiles=listOfFiles[:longueur]
        outfile=open(destination+str(ngram)+"_gram/"+"sequences_occurences_1","w")
    elif thread==2:
        listOfFiles=listOfFiles[longueur:2*longueur]
        outfile=open(destination+str(ngram)+"_gram/"+"sequences_occurences_2","w")
    elif thread==3:
        listOfFiles=listOfFiles[2*longueur:3*longueur]
        outfile=open(destination+str(ngram)+"_gram/"+"sequences_occurences_3","w")
    elif thread==4:
        listOfFiles=listOfFiles[3*longueur:]
        outfile=open(destination+str(ngram)+"_gram/"+"sequences_occurences_4","w")

    sequence_dict=dict()
    for file in listOfFiles:
        file=file.replace(destination,"")
        iter+=1
        print(str(iter)+"/"+str(longueur))
        sequence_dict = count(file,ngram, destination)
        newline = "\'"+file+"\'"
        sequence_file=open(destination+str(ngram)+"_gram/"+"sequence_list",'r')
        sequence_list  = sequence_file.readlines()
        for sequence in sequence_list:
            newline=newline+","+str(sequence_dict.get(str(sequence.replace("\n",""))))
        outfile.write(newline.replace('\n', '')+"\n")

def gather(destination,ngram):
    outfile=open(destination+str(ngram)+"_gram/"+"sequences_occurences.arff","w")
    for line in open(destination+str(ngram)+"_gram/"+"sequences_occurences_5", "r"):
        outfile.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequences_occurences_1", "r"):
        outfile.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequences_occurences_2", "r"):
        outfile.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequences_occurences_3", "r"):
        outfile.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequences_occurences_4", "r"):
        outfile.write(line)
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
    thread_1 = generate_arff(ngram,destination,1)
    thread_2 = generate_arff(ngram,destination,2)
    thread_3 = generate_arff(ngram,destination,3)
    thread_4 = generate_arff(ngram,destination,4)

# Lancement des threads
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    gather(destination,ngram)
    for i in range(1,6):
        remove(destination+str(ngram)+"_gram/"+"sequences_occurences_"+str(i))
