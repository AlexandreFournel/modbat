import os
import regex_files_err_warning_fine
import generate_ngram
import generate_ngrams_in_function_of_file
import rank_similarities
import filter_ranking
import generate_arff_doc
import subprocess
import test_difference_2_files
import generate_files_fine_err_warning
import sys, ast



def main():
    function = str(sys.argv[1])
    
    if function=="generateFiles":
    ##Step 1
        # To Create all files .err .warning . ...
        origin = str(sys.argv[2])
        destination = str(sys.argv[3])
        extension =  [str(sys.argv[i]) for i in range(4, len(sys.argv))]
        generate_files_fine_err_warning.main(destination,origin, extension)
        regex_files_err_warning_fine.main(destination+"Files/")
    
    elif function=="generateNGram":
    ##Step 3
        # To generate 1-gram, 2-gram, 3-gram,
        # 4-gram unique sequences
        destination = str(sys.argv[2])
        ngrams =  [str(sys.argv[i]) for i in range(3, len(sys.argv))]
        for ngram in ngrams:
            generate_ngram.main(destination,ngram)

    elif function=="generateNGramByFile":
    ##Step 4
        # To generate files where each line 
        # points out one ngram following by 
        # files where it's possible to find it
        destination = str(sys.argv[2])
        ngrams =  [str(sys.argv[i]) for i in range(3, len(sys.argv))]
        for ngram in ngrams:
            generate_ngrams_in_function_of_file.main(destination, ngram)

    elif function=="rankSimilarities":
    ##Step 5
        destination = str(sys.argv[2])
        ngrams =  [str(sys.argv[i]) for i in range(3, len(sys.argv))]
        for ngram in ngrams:
            rank_similarities.main(destination, ngram)

    elif function=="listOfSimilarFiles":
    ##Step 6
        
        # To generate a filtering of this 
        # ranking, please launch. Be careful,
        # in that doc, you have to choose the
        # limit of percentage of similitudes
        # between 2 files.
        destination = str(sys.argv[2])
        percentage = str(sys.argv[3])
        filter_ranking.main(destination,percentage)

    elif function=="generateArffDoc":
    ##Step 7
        # To generate arff doc
        destination = str(sys.argv[2])
        ngrams =  [str(sys.argv[i]) for i in range(3, len(sys.argv))]
        for ngram in ngrams:
            generate_arff_doc.main(destination, ngram)

# python3 main.py test2Files Files/modbat/_.modbat.examples.JavaNioServerSocket_-n\=200-s\=1--no-redirect-out--log-level\=fine.log Files/modbat/_.modbat.examples.CounterModel_-s\=1-n\=30--no-redirect-out.log
    elif function=="test2Files":
    ## -> TEST
        # To test the pourcentage of equivalence 
        # of 2 files
        destination = str(sys.argv[2])
        file1 = str(sys.argv[3])
        file2 = str(sys.argv[4])
        test_difference_2_files.main(file1.replace("\=","="),file2.replace("\=","="), destination)
main()