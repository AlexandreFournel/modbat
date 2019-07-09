import os
import csv
import re
def main():

    liste_finale=[]
    dirName = 'Files/modbat/'
    word_list=open("word_list3",'r')
    words_word_list  = word_list.readlines()

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    #remove empty files. 
    for file in listOfFiles:
        if os.stat(file).st_size == 0:
            os.remove(file)


    longueur=len(listOfFiles)
    print("longueur =")
    print(longueur)
    iter=0
    # Recover name of the files and call function to count num of words 
    i=0
    with open("word_occurences.txt","w") as fd:
        fd.write("@relation firstTry")
        fd.write("\n")
        fd.write("\n")
        fd.write("@attribute fileNames")
        fd.write("\n")
        for word in words_word_list[2:]:
            if (i>=2):
                word_without_coma=word.replace(',', '_')
                word_without_returned_line=word_without_coma.replace('\n', '')
                fd.write("@attribute "+word_without_returned_line+" numeric")
                fd.write("\n")
            i+=1
        iter=0
        fd.write("\n")
        fd.write("@data")
        fd.write("\n")
        for file in listOfFiles:
            line=""
            fd.write(line.replace('\n', ''))
            iter+=1
            if (file != dirName+"word_list" and file != dirName+"line_list"):
                line=file
                for word in words_word_list[2:]:
                    count_word=sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), open(file, 'r').read()))    
                    line=line+","+str(count_word)
                fd.write(line.replace('\n', ''))
                fd.write("\n")
main()
