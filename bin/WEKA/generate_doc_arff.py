import os
import csv
import re
def main():

    liste_finale=[]
    dirName = 'Files/modbat/'
    word_list=open("word_list3",'r')
    words_word_list  = word_list.readlines()
    used_word_list=words_word_list[3:]

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    #remove empty files. 
    for file in listOfFiles:
        if os.stat(file).st_size == 0:
            os.remove(file)


    longueur=len(listOfFiles)
    with open("word_occurences.arff","w") as fd:
        fd.write("@relation firstTry")
        fd.write("\n")
        fd.write("\n")
        fd.write("@attribute fileNames string")
        fd.write("\n")
        for word in used_word_list:
            word_without_coma=word.replace(',', '_')
            word_without_returned_line=word_without_coma.replace('\n', '')
            fd.write("@attribute "+word_without_returned_line+" numeric\n")
        iter=0
        fd.write("\n")
        fd.write("@data")
        fd.write("\n")
        for file in listOfFiles:
            line=""
            fd.write(line.replace('\n', ''))
            iter+=1
            print(str(iter)+"/"+str(longueur))
            if (file != dirName+"word_list" and file != dirName+"line_list"):
                line="\'"+file+"\'"
# Commented lines enable to see if the program do the right thing
#                print(file)
                for word in used_word_list:
                    word_w=word.replace("\n","")
                    count_word=sum(1 for _ in re.finditer(r'\b%s\b' %re.escape(word_w), open(file, 'r').read()))
#                    if count_word>0:
#                        print("\n"+word_w+":"+str(count_word))
                    line=line+","+str(count_word)
#                print("\n")
                fd.write(line.replace('\n', '')+"\n")
main()
