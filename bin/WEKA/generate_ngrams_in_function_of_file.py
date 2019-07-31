import os
from threading import Thread
from progress.bar import Bar

class launch_threading(Thread):
    def __init__(self, ngram,destination, number,nbWorks):
        Thread.__init__(self)
        self.number = number
        self.ngram=ngram
        self.destination=destination
        self.nbWorks=nbWorks
        
    def run(self):
        generate_ngrams_in_function_of_file(self.ngram, self.destination, self.number, self.nbWorks)

def generate_ngrams_in_function_of_file(ngram,destination,thread, nbWorks):

    num_total_lines=sum(1 for line in open(destination+str(ngram)+"_gram/"+"sequence_list", "r"))
    num_lines = num_total_lines//4


    if thread==1:
        bar = Bar('Processing', max=nbWorks)
        outfile = open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_1", "w")
        lowLimit=1
        highLimit=num_lines
    elif thread==2:
        lowLimit=num_lines
        highLimit=2*num_lines
        outfile = open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_2", "w")
    elif thread==3:
        lowLimit=2*num_lines
        highLimit=3*num_lines
        outfile = open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_3", "w")
    elif thread==4:
        lowLimit=3*num_lines
        highLimit=num_total_lines+1 #high limit is exclusive
        outfile = open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_4", "w")        

    i=1
    for line in open(destination+str(ngram)+"_gram/"+"sequence_list", "r"):
        if i >= lowLimit and i < highLimit :
            if thread==1:
                bar.next()
                bar.next()
                bar.next()
                bar.next()
            words=line.replace("\n","")
            outfile.write(words)
            files_seen={}
            for line2 in open(destination+str(ngram)+"_gram/"+"sequence_list_with_name_files", "r"):
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

def gather(destination,ngram):
    outfile6=open(destination+str(ngram)+"_gram/"+"sequence_list_by_files","w")
    for line in open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_1", "r"):
        outfile6.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_2", "r"):
        outfile6.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_3", "r"):
        outfile6.write(line)
    for line in open(destination+str(ngram)+"_gram/"+"sequence_list_by_files_4", "r"):
        outfile6.write(line)
    return

def remove(file):
    os.remove(file)
    return

def main(destination, ngram):
    nbWorks=sum(1 for line in open(destination+str(ngram)+"_gram/"+"sequence_list", "r"))
    thread_1 = launch_threading(ngram,destination,1,nbWorks)
    thread_2 = launch_threading(ngram,destination,2,nbWorks)
    thread_3 = launch_threading(ngram,destination,3,nbWorks)
    thread_4 = launch_threading(ngram,destination,4,nbWorks)

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

    for i in range(1,5):
        remove(destination+str(ngram)+"_gram/"+"sequence_list_by_files_"+str(i))
