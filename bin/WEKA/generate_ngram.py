import os

def create_folder(path, dirName_files):
    if not os.path.exists(path+dirName_files):
        os.mkdir(path+dirName_files)
    return
  
def generate_sequenceList(n_grams, dirName,dirName_files):
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirname, filenames) in os.walk(dirName_files):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    with open(n_grams+dirName+"sequence_list","w") as fd:
        with open(n_grams+dirName+"sequence_list_with_name_files","w") as fh:
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

                    if n==1:
                        for k in range(length_line):
                            fh.write(file+"__"+line[k]+"\n")
                            fd.write(line[k]+"\n")
                    elif n==2:
                        if length_line>1:
                            for k in range(length_line-1):
                                fh.write(file+"__"+line[k]+" "+line[k+1]+"\n")
                                fd.write(line[k]+" "+line[k+1]+"\n")
                        elif length_line==1:
                            fh.write(file+"__"+line[0]+" "+""+"\n")
                            fd.write(line[0]+" "+""+"\n")

                    elif n==3:
                        if length_line>2:
                            for k in range(length_line-2):
                                fh.write(file+"__"+line[k]+" "+line[k+1]+" "+line[k+2]+"\n")
                                fd.write(line[k]+" "+line[k+1]+" "+line[k+2]+"\n")
                        elif length_line==2:
                            for k in range(length_line-1):
                                fh.write(file+"__"+line[k]+" "+line[k+1]+" "+""+"\n")
                                fd.write(line[k]+" "+line[k+1]+" "+""+"\n")
                        elif length_line==1:
                            fh.write(file+"__"+line[0]+" "+""+" "+""+"\n")
                            fd.write(line[0]+" "+""+" "+""+"\n")

                    elif n==4:
                        if length_line>3:
                            for k in range(length_line-3):
                                fh.write(file+"__"+line[k]+" "+line[k+1]+" "+line[k+2]+" "+line[k+3]+"\n")
                                fd.write(line[k]+" "+line[k+1]+" "+line[k+2]+" "+line[k+3]+"\n")

                        elif length_line==3:
                            for k in range(length_line-2):
                                fh.write(file+"__"+line[k]+" "+line[k+1]+" "+line[k+2]+" "+""+"\n")
                                fd.write(line[k]+" "+line[k+1]+" "+line[k+2]+" "+""+"\n")
                        elif length_line==2:
                            for k in range(length_line-1):
                                fh.write(file+"__"+line[k]+" "+line[k+1]+" "+""+" "+""+"\n")
                                fd.write(line[k]+" "+line[k+1]+" "+""+" "+""+"\n")
                        elif length_line==1:
                            fh.write(file+"__"+line[0]+" "+""+" "+""+" "+""+"\n")
                            fd.write(line[0]+" "+""+" "+""+" "+""+"\n")
    return

def remove_duplicate_lines(ngram,dirName):
    lines_seen = set() 
    outfile = open(ngram+dirName+"sequence_list"+"copy", "w")
    for line in open(ngram+dirName+"sequence_list", "r"):
        if line not in lines_seen: 
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    copy_remove(ngram+dirName+"sequence_list")
    return

def copy_remove(file):
    os.remove(file)
    os.rename(file+"copy",file)
    return

def main(directory, ngrams, dirName_files):

    for dirName in dirName_files:
        for ngram in ngrams:
            create_folder(ngram, dirName)
            generate_sequenceList(ngram,dirName,directory+dirName)
            remove_duplicate_lines(ngram,dirName)