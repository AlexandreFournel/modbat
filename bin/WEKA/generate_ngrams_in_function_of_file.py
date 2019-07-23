import os
from threading import Thread

class launch_threading(Thread):
    def __init__(self, n_grams,dirName,dirName_files, number):
        Thread.__init__(self)
        self.number = number
        self.n_grams=n_grams
        self.dirName=dirName
        self.dirName_files=dirName_files

    def run(self):
        generate_ngrams_in_function_of_file(self.n_grams, self.dirName, self.dirName_files, self.number)


def generate_ngrams_in_function_of_file(n_grams,dirName,dirName_files,thread):
    print("\n")
    if thread==1:
        print("hey, I'm thread 1, I'm working on : "+n_grams[:-1] + " directory : "+dirName[:-1])
        outfile = open(n_grams+dirName+"sequence_list_by_files_1", "w")
    elif thread==2:
        print("hey, I'm thread 2, I'm working on : "+n_grams[:-1] + " directory : "+dirName[:-1])
        outfile = open(n_grams+dirName+"sequence_list_by_files_2", "w")
    elif thread==3:
        print("hey, I'm thread 3, I'm working on : "+n_grams[:-1] + " directory : "+dirName[:-1])
        outfile = open(n_grams+dirName+"sequence_list_by_files_3", "w")
    elif thread==4:
        print("hey, I'm thread 4, I'm working on : "+n_grams[:-1] + " directory : "+dirName[:-1])
        outfile = open(n_grams+dirName+"sequence_list_by_files_4", "w")        
    print("\n")
    num_total_lines=sum(1 for line in open(n_grams+dirName+"sequence_list", "r"))
    num_lines = num_total_lines//4
    
    if thread==1:
        i=1
        for line in open(n_grams+dirName+"sequence_list", "r"):
            if i < num_lines :
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
    elif thread==2:
        i=1
        for line in open(n_grams+dirName+"sequence_list", "r"):
            if i >= num_lines and i < 2*num_lines:
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
    elif thread==3:
        i=1
        for line in open(n_grams+dirName+"sequence_list", "r"):
            if i >= 2*num_lines and i < 3*num_lines:
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
    elif thread==4:
        i=1
        for line in open(n_grams+dirName+"sequence_list", "r"):
            if i >= 3*num_lines:
                print(str(float(int((i-3*num_lines)*100/(num_total_lines-3*num_lines)*10))/10)+'%')
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
    for dirName in dirName_files:
        for ngram in ngrams:
            thread_1 = launch_threading(ngram,dirName,directory+dirName,1)
            thread_2 = launch_threading(ngram,dirName,directory+dirName,2)
            thread_3 = launch_threading(ngram,dirName,directory+dirName,3)
            thread_4 = launch_threading(ngram,dirName,directory+dirName,4)

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
