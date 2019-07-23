import regex_files_err_warning_fine
import generate_ngram
import generate_ngrams_in_function_of_file
import rank_similitudes
import filter_ranking
import generate_arff_doc
import subprocess
import test_difference_2_files

def main():
    directory="Files/"
    ngrams=["1_gram/","2_gram/","3_gram/","4_gram/"]
    dirName_files=["modbat/","config/","modbat.config.ConfigTest/"]
    

    ##Step 1
        # To Create all files .err .warning . ...
    subprocess.call(['./generate_files_fine_err_warning.sh'])
    
    
    
    ##Step 2
        # To do some REGEX
    #regex_files_err_warning_fine.main(dirName_files)
    


    ##Step 3
        # To generate 1-gram, 2-gram, 3-gram,
        # 4-gram unique sequences
    #generate_ngram.main(directory, ngrams, dirName_files)



    ##Step 4
        # To generate files where each line 
        # points out one ngram following by 
        # files where it's possible to find it
    #generate_ngrams_in_function_of_file.main(directory, ngrams, dirName_files)



    ##Step 5
        # To generate a ranking of percentage
        # of similitudes of 2 files
    #rank_similitudes.main(directory, ngrams, dirName_files)



    ##Step 6
    percentage=100
        # To generate a filtering of this 
        # ranking, please launch. Be careful,
        # in that doc, you have to choose the
        # limit of percentage of similitudes
        # between 2 files.
    #filter_ranking.main(directory, ngrams, dirName_files,percentage)



    ##Step 7
        # To generate arff doc
    #generate_arff_doc.main(directory, ngrams, dirName_files,percentage)



    ## -> TEST
        # To test the pourcentage of equivalence 
        # of 2 files
    #file1= "stringToReplaced"
    #file2= "stringToReplaced"
    #test_difference_2_files.main(file1.replace("\=","=") file2.replace("\=","="))
main()