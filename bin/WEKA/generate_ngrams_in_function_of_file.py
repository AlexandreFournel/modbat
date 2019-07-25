import os
from threading import Thread
from progress.bar import Bar

class launch_threading(Thread):
    def __init__(self, n_grams,dirName,dirName_files, number,nbWorks):
        Thread.__init__(self)
        self.number = number
        self.n_grams=n_grams
        self.dirName=dirName
        self.dirName_files=dirName_files
        self.nbWorks=nbWorks

    def run(self):
        generate_ngrams_in_function_of_file(self.n_grams, self.dirName, self.dirName_files, self.number, self.nbWorks)

def generate_ngrams_in_function_of_file(n_grams,dirName,dirName_files,thread, nbWorks):

    num_total_lines=sum(1 for line in open(n_grams+dirName+"sequence_list", "r"))
    num_lines = num_total_lines//4


    if thread==1:
        bar = Bar('Processing', max=nbWorks)
        outfile = open(n_grams+dirName+"sequence_list_by_files_1", "w")
        lowLimit=1
        highLimit=num_lines
    elif thread==2:
        lowLimit=num_lines
        highLimit=2*num_lines
        outfile = open(n_grams+dirName+"sequence_list_by_files_2", "w")
    elif thread==3:
        lowLimit=2*num_lines
        highLimit=3**num_lines
        outfile = open(n_grams+dirName+"sequence_list_by_files_3", "w")
    elif thread==4:
        lowLimit=3*num_lines
        highLimit=num_lines+1
        outfile = open(n_grams+dirName+"sequence_list_by_files_4", "w")        

    i=1
    for line in open(n_grams+dirName+"sequence_list", "r"):
        if i >= lowLimit and i < highLimit :
            if thread==1:
                bar.next()
                bar.next()
                bar.next()
                bar.next()
            words=line.replace("\n","")
            outfile.write(words)
            files_seen={}
            for line2 in open(n_grams+dirName+"sequence_list_with_name_files", "r"):
                [namefile,words_to_compare]=line2.split("__")
                namefile=namefile.replace("\n","")
                words_to_compare=words_to_compare.replace("\n","")
                if words_to_compare==words:
                    if (namefile in files_seen):
                        count=files_seen.get(namefile)
                        count+=1
                        del files_seen[namefile]
                        files_seen[namefile] = count
                    else:
                        files_seen[namefile] = 1
            for cle,valeur in files_seen.items():
                outfile.write("__"+cle.replace("\n","")+"::"+str(valeur))
            outfile.write("\n")
        i+=1
    outfile.close()
    if thread==1:
        bar.finish()
    return

def gather(n_grams,dirName):
    outfile6=open(n_grams+dirName+"sequence_list_by_files","w")
    for line in open(n_grams+dirName+"sequence_list_by_files_1", "r"):
        outfile6.write(line)
    for line in open(n_grams+dirName+"sequence_list_by_files_2", "r"):
        outfile6.write(line)
    for line in open(n_grams+dirName+"sequence_list_by_files_3", "r"):
        outfile6.write(line)
    for line in open(n_grams+dirName+"sequence_list_by_files_4", "r"):
        outfile6.write(line)
    return

def remove(file):
    os.remove(file)
    return

def main(directory, ngrams, dirName_files):
    step=1
    for dirName in dirName_files:
        for ngram in ngrams:
            print("step"+str(step)+"/"+str(6))
            nbWorks=sum(1 for line in open(ngram+dirName+"sequence_list", "r"))
            thread_1 = launch_threading(ngram,dirName,directory+dirName,1,nbWorks)
            thread_2 = launch_threading(ngram,dirName,directory+dirName,2,nbWorks)
            thread_3 = launch_threading(ngram,dirName,directory+dirName,3,nbWorks)
            thread_4 = launch_threading(ngram,dirName,directory+dirName,4,nbWorks)
            step+=1
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

            for i in range(1,5):
                remove(ngram+dirName+"sequence_list_by_files_"+str(i))
