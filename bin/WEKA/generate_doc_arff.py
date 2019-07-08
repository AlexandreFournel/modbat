import os
import csv

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
    line="file names" 
    i=0
    with open("word_occurences.txt","w") as fd:
        for word in words_word_list[2:longueur//2]:
            if (i>=2):
                line+="|"+word
            i+=1
        line=line.replace('\n', '')
        fd.write(line)
        iter=0
        for file in listOfFiles:
            line=""
            fd.write(line.replace('\n', ''))
            iter+=1
            print("compteur = ")
            print(iter)
            print("")
            fd.write("\n\n")
            if (file != dirName+"word_list" and file != dirName+"line_list"):
                line=file
                for word in words_word_list[2:]:
                    if word=="failed":
                        print("NOOOOW")
                    line=line+"|"+str(open(file, 'r').read().count(word))
                fd.write(line.replace('\n', ''))
        fd.write("\n\n")
    
        for word in words_word_list[longueur//2:]:
            if (i>=2):
                line+="|"+word
            i+=1
        line=line.replace('\n', '')
        fd.write(line)
        iter=0
        for file in listOfFiles:
            line=""
            fd.write(line.replace('\n', ''))
            iter+=1
            print("compteur = ")
            print(iter)
            print("")
            fd.write("\n\n")
            if (file != dirName+"word_list" and file != dirName+"line_list"):
                line=file
                for word in words_word_list[2:]:
                    if word=="failed":
                        print("NOOOOW")
                    line=line+"|"+str(open(file, 'r').read().count(word))
                fd.write(line.replace('\n', ''))
        fd.write("\n\n")
        
main()
