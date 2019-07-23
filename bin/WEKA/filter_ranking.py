import re
import os
from threading import Thread
import sys

def filter(file1,file2):
    percentage_per_type={}

    for line in open("2_gram/modbat/Ranking", "r"):
        if (file1 in line) and (file2 in line) :
            value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
            extension=line.split("__")[1].rsplit('.',1)[1]
            if extension in percentage_per_type:
                print("ERROR in filter_ranking")
            percentage_per_type[extension]=value
    total=0
    if  bool(percentage_per_type):
        if "debug" not in percentage_per_type:
            if os.path.isfile(file1+".debug") and  os.path.isfile(file2+".debug"):
                total+=100
        else:
            total+=percentage_per_type.get("debug")
        if "info" not in percentage_per_type:
            if os.path.isfile(file1+".info") and  os.path.isfile(file2+".info"):
                total+=100
        else:
            total+=percentage_per_type.get("info")

        if "fine" not in percentage_per_type:
            if os.path.isfile(file1+".fine") and  os.path.isfile(file2+".fine"):
                total+=100
        else:
            total+=percentage_per_type.get("fine")

        if "error" not in percentage_per_type:
            if os.path.isfile(file1+".error") and  os.path.isfile(file2+".error"):
                total+=100
        else:
            total+=percentage_per_type.get("error")

        if "warning" not in percentage_per_type:
            if os.path.isfile(file1+".warning") and  os.path.isfile(file2+".warning"):
                total+=100
        else:
            total+=percentage_per_type.get("warning")

        if "raw" not in percentage_per_type:
            if os.path.isfile(file1+".raw") and  os.path.isfile(file2+".raw"):
                total+=100
        else:
            total+=percentage_per_type.get("raw")
    return(int(total/6*10)/10)

def filters(file1,file2):
    print("\n")
    print(file1)
    print(file2)
    print("\n")
    ##debug
    debug="error"
    if os.path.isfile(file1+".debug") and os.path.isfile(file2+".debug"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                debug=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".debug")==False and os.path.isfile(file2+".debug")==False:
        debug=100
    else:
        debug=0
    if debug=="error":
        debug=0

    ##info
    info="error"
    if os.path.isfile(file1+".info") and os.path.isfile(file2+".info"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                info=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".info")==False and os.path.isfile(file2+".info")==False:
        info=100
    else:
        info=0
    if info=="error":
        info=0

    error="error"
    if os.path.isfile(file1+".error") and os.path.isfile(file2+".error"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                error=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".error")==False and os.path.isfile(file2+".error")==False:
        error=100
    else:
        error=0
    if error=="error":
        error=0

    warning="error"
    if os.path.isfile(file1+".warning") and os.path.isfile(file2+".warning"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                warning=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".warning")==False and os.path.isfile(file2+".warning")==False:
        warning=100
    else:
        warning=0
    if warning=="error":
        warning=0

    fine="error"
    if os.path.isfile(file1+".fine") and os.path.isfile(file2+".fine"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                fine=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".fine")==False and os.path.isfile(file2+".fine")==False:
        fine=100
    else:
        fine=0
    if fine=="error":
        fine=0

    raw="error"
    if os.path.isfile(file1+".raw") and os.path.isfile(file2+".raw"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                raw=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".raw")==False and os.path.isfile(file2+".raw")==False:
        raw=100
    else:
        raw=0
    if raw=="error":
        raw=0

    total=debug+info+ fine+ error+ warning+ raw
    total=total//6
    return (total)

def find_good_sublist(file,liste):
    for sublist in liste:
        if sublist[0]==file.rsplit('.')[0]:
            sublist=sublist.append(file.rsplit('.')[1])
    return (liste)

def filtering(n_grams, dirName, dirName_files, thread, percentage):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk("Files/"+"modbat/"):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    for i in range(len(listOfFiles)):
        listOfFiles[i]=listOfFiles[i].rsplit(".",1)[0]
    list(set(listOfFiles)) 
    length=len(listOfFiles)

    if thread==1:
        for i in range(length//4):
            for j in range(i+1,length):
                res=filters(listOfFiles[i],listOfFiles[j])
                if res>=percentage:
                    print(listOfFiles[i])
                    print(listOfFiles[j])
                    print("\n")
    elif thread==2:
        for i in range(length//4,2*length//4):
            for j in range(i+1,length):
                res=filters(listOfFiles[i],listOfFiles[j])
                if res>=percentage:
                    print(listOfFiles[i])
                    print(listOfFiles[j])
                    print("\n")
    elif thread==3:
        for i in range(2*length//4,3*length//4):
            for j in range(i+1,length):
                res=filters(listOfFiles[i],listOfFiles[j])
                if res>=percentage:
                    print(listOfFiles[i])
                    print(listOfFiles[j])
                    print("\n")
    elif thread==4:
        iter=3*length//4-1
        for i in range(3*length//4,):
            iter+=1
            value= (iter - 3*length//4) *100 // (length-3*length//4)
            progressBar(value, 100)
            for j in range(i+1,length):
                res=filters(listOfFiles[i],listOfFiles[j])
                if res>=percentage:
                    print(listOfFiles[i])
                    print(listOfFiles[j])
                    print("\n")

def progressBar(value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

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




