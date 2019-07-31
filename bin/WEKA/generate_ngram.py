import os

def getListOfFiles(destination):
    listOfFiles=list()
    for path, subdirs, files in os.walk(destination):
        if len(files)!=0:
                for name in files:
                        listOfFiles+=[path+"/"+name]
    return listOfFiles

def generate_sequenceList(n_grams, destination, listOfFiles):
    # Get the list of all files in directory tree at given path
    with open(destination+n_grams+"_gram/"+"sequence_list","w") as fd:
        with open(destination+n_grams+"_gram/"+"sequence_list_with_name_files","w") as fh:
            for file in listOfFiles:
                tabular=open(file, 'r').read().split("\n")
                for i in range(len(tabular)):
                    tabular[i]=tabular[i].split()
                # tabular is a list of lists. Each list represents a line, and each subList represents a word of a line
                for j in range(len(tabular)):
                    line=tabular[j]
                    length_line=len(line)
                    #We want to know what is the n in the _ngrams_
                    n=int(n_grams[0],10)

                    if length_line>=n:
                        for k in range(length_line-(n-1)):

                            sequenceOfWords=str(line[k])
                            for i in range(1,n):
                                sequenceOfWords=sequenceOfWords+" "+str(line[k+i])
                            
                            fh.write((file.replace(destination,"")).replace("//","/")+"__"+sequenceOfWords+"\n")
                            fd.write(sequenceOfWords+"\n")

                    elif length_line!=0:
                        sequenceOfWords=str(line[0])
                        for i in range(1,n):
                            if i>=length_line:
                                sequenceOfWords=sequenceOfWords+" "+""
                            else:
                                sequenceOfWords=sequenceOfWords+" "+str(line[i])
                        fh.write((file.replace(destination,"")).replace("//","/")+"__"+sequenceOfWords+"\n")
                        fd.write(sequenceOfWords+"\n")
    return

def remove_duplicate_lines(ngram, destination):
    lines_seen = set() 
    outfile = open(destination+ngram+"_gram/"+"sequence_list"+"copy", "w")
    for line in open(destination+ngram+"_gram/"+"sequence_list", "r"):
        if line not in lines_seen: 
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    copy_remove(destination+ngram+"_gram/"+"sequence_list")
    return

def copy_remove(file):
    os.remove(file)
    os.rename(file+"copy",file)
    return

def creationFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main(destination,ngram):
    listOfFiles=getListOfFiles(destination+"Files/")
    creationFolder(destination+ngram+"_gram/")
    generate_sequenceList(ngram,destination, listOfFiles)
    remove_duplicate_lines(ngram,destination)