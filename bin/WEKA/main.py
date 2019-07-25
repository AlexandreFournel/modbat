import regex_files_err_warning_fine
import generate_ngram
import generate_ngrams_in_function_of_file
import rank_similarities
import filter_ranking
import generate_arff_doc
import subprocess
import test_difference_2_files
import sys

def main():
    directory="Files/"
    ngrams=["1_gram/","2_gram/","3_gram/","4_gram/"]
    dirName_files=["modbat/","config/","modbat.config.ConfigTest/"]

    function = str(sys.argv[1])

    if function=="generateFiles":
    ##Step 1
        # To Create all files .err .warning . ...
        subprocess.call(['./generate_files_fine_err_warning.sh'])
    
    elif function=="filterFiles":
    ##Step 2
        # To do some REGEX
        regex_files_err_warning_fine.main(dirName_files, directory)
    
    elif function=="generateNGram":
    ##Step 3
        # To generate 1-gram, 2-gram, 3-gram,
        # 4-gram unique sequences
        generate_ngram.main(directory, ngrams, dirName_files)

    elif function=="generateNGramByFile":
    ##Step 4
        # To generate files where each line 
        # points out one ngram following by 
        # files where it's possible to find it
        generate_ngrams_in_function_of_file.main(directory, ngrams, dirName_files)

    elif function=="rankSimilarities":
    ##Step 5
        # To generate a ranking of percentage
        # of similitudes of 2 files
        rank_similarities.main(directory, ngrams, dirName_files)

    elif function=="listOfSimilarFiles":
    ##Step 6
        percentage = str(sys.argv[2])
        # To generate a filtering of this 
        # ranking, please launch. Be careful,
        # in that doc, you have to choose the
        # limit of percentage of similitudes
        # between 2 files.
        filter_ranking.main(directory, ngrams, dirName_files,percentage)

    elif function=="generateArffDoc":
    ##Step 7
        # To generate arff doc
        generate_arff_doc.main(directory, ngrams, dirName_files)

# python3 main.py test2Files Files/modbat/_.modbat.examples.JavaNioServerSocket_-n\=200-s\=1--no-redirect-out--log-level\=fine.log Files/modbat/_.modbat.examples.CounterModel_-s\=1-n\=30--no-redirect-out.log
    elif function=="test2Files":
    ## -> TEST
        # To test the pourcentage of equivalence 
        # of 2 files
        file1 = str(sys.argv[2])
        file2 = str(sys.argv[3])
        test_difference_2_files.main(file1.replace("\=","="),file2.replace("\=","="), ngrams, dirName_files)
main()