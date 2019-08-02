# Programs for analysis Log Err for Modbat Files. 

Here is available severals program to analyse files. This project could be adaptable to others projects.

The main.py Python program is managing, and supervising all the others programs. 

Python version used : Python 3.6.5 :: Anaconda, Inc.
WEKA version used : 3.8.3 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install progress.

```bash
pip install progress
```

## Usage

### Generate Subfiles filtred.
From a repository where you have all your files (and subfiles, subsubfiles...) you can generate filtering to preprocess your data. 


```bash
python3 main.py generateFiles originRepository ResultRepository ExtensionOfFilesWeWantToStudy
```

From the Original repository, you can select all the files with the good extension. From a repository, for example in "../log/" , you can have different different filename extension. If you want to analyse only ".log" and ".err" files, and put the result in a new folder "Results/" for example, please launch :

Example:
```bash
python3 main.py generateFiles ../log/ Results/ err log
```

In the Results/ Folder will be created 2 Folders : 
   - OriginalFiles/ which contains all the selected files (all the .log and .err files in the example)
   - Files/  which countains subfiles filtred. 
   For each file in OriginalFiles/, the program create 6 files with the following filename extension : 
      - OriginalFileName.info
      - OriginalFileName.warning
      - OriginalFileName.raw
      - OriginalFileName.fine
      - OriginalFileName.error
      - OriginalFileName.debug
   From the OriginalFileName, we select all the lines beginning by [INFO], and copy them in the OriginalFileName.info. (Same behavior for the other extensions)
   For the .raw file are presented all the lines which didn't match at the previous step.
   
   In this folder, all the lines beginning by a random seed are removed. 
   Every empty file is deleted.

### Generate Ngram
It is possible to generate a list of unique ngram (1gram, 2gram, 3gram, 4gram, others). 



```bash
python3 main.py generateNGram ResultRepository ngrams
```

With the previous example, 
Example
```bash
python3 main.py generateNGram Results/ 1 2 3 4 5
```

The program uses the folder "Files/" in the "Results/" repository created at the step 1. 

With the execution of this program, folders are created in "Results/". If you write "1 2 3 4 5" as an argument. 5 folders wwill be created, and called :  
{1_gram/, 2_gram/, 3_gram/, 4_gram/,  5_gram/}. 

In them, 2 generated files :
   - sequence_list
   - sequence_list_with_name_files
The first one is the list of unique ngram. 
The second one is the list of ngram by files. 
Each line is composed by :

```text
nameOfFile__ngram
```

In this last files, lines are not unique. 

### Generate Ngram By Files
It is possible to generate 
   - sequence_list_by_files
in n_gram/ folder, by launching : 

```bash
python3 main.py generateNGramByFile ResultRepository ngrams
```

Example 
```bash
python3 main.py generateNGramByFile Results/ 1 2 3 4 5
```

In this example, the files will be created in 5 repository : {1_gram/, 2_gram/, 3_gram/, 4_gram/,  5_gram/}

To generate it, it is necessary to have updated version of 
   - sequence_list
   - sequence_list_with_name_files

The "sequence_list_by_files" lines are composed by :
```text
ngram__nameOfFile1::occurence__nameOfFile2::occurence__ ... __nameOfFile?::occurence
```

In other words, each line of this file lists one unique ngram with the name of the different files where the ngram appears. The file name is followed by the occurence. 


### Generate A Ranking of Similarities Between 2 Files
It is possible to generate 
   - Ranking
by launching :
```bash
python3 main.py rankSimilarities ResultRepository ngrams
```

Example
```bash
python3 main.py rankSimilarities Results/ 1 2 3 4 5
```
In this example, the file will be created in 5 repository : {1_gram/, 2_gram/, 3_gram/, 4_gram/,  5_gram/}

To generate it, it is necessary to have updated version of 
   - sequence_list_by_files

The "Ranking" lines are composed by :
```text
percentageOfSimilarities__nameOfFile1__nameOfFile2
```

In other words, every 2 files are compared. Thanks to the Jaccard Index, we are dividing the intersect of in-commun ngrams by the union of ngrams of these 2 files. 



### Print Every 2 Files If They Have More Than x% of Similarities
It is possible to print a list of 2 files which have more than X percentage of similarities. 

This file use a python program which returns a list of 6 value. For 2 different files, the program recovers the comparison of these files :
   - file1.warning and file2.warning
   - file1.error and file2.error
   - file1.info and file2.info
   - file1.debug and file2.debug
   - file1.fine and file2.fine
   - file1.raw and file2.raw
The programs average these result. Automatically, it executed this average for the different n_gram folders already existing. 

The programs does the average of the comparison results of the different Folders ngram. It prints every pairs of files where the comparison is superior to a limit put by the user. 

```bash
python3 main.py listOfSimilarFiles ResultRepository Pourcentage    
```

Example
```bash
python3 main.py listOfSimilarFiles Results/ 50
```

With the previous example, the programs will avreage the comparison of 
   - file1.warning and file2.warning
   - file1.error and file2.error
   - file1.info and file2.info
   - file1.debug and file2.debug
   - file1.fine and file2.fine
   - file1.raw and file2.raw
For different ngram {1_gram/, 2_gram/, 3_gram/, 4_gram/,  5_gram/}.

To generate it, it is necessary to have updated version of 
   - Ranking 
in the different existing folders 


### Generate Arff Files compatible with WEKA software
It is possible to generate ARFF files by folder . 

```bash
python3 main.py generateArffDoc ResultRepository ngrams
```

This will create sequences_occurences.arff files in the different folders.

Example:
```bash
python3 main.py generateArffDoc Result/ 1 2 3 4 5
```

in {1_gram/, 2_gram/, 3_gram/, 4_gram/,  5_gram/} Folders, the file sequences_occurrences.arff will be created. 

The "sequences_occurences.arff" lines are composed by :
```text
nameOfFile1, nb_of_occurences_of_1st_ngram, nb_of_occurences_of_2nd_ngram...
```

To generate it, it is necessary to have updated version of 
   - sequence_list

### Test The Similarities Of 2 Files
It's possible to test the similitudes between 2 files for differnet ngram. 

```bash
python3 main.py test2Files ResultRepository nameFile1 nameFile2
```

Example:
```bash
python3 main.py test2Files Results/ Results/OriginalFiles/modbat_modbat.test.ComplexLaunch6_-s\=1-n\=2--log-level\=fine--no-redirect-out.log Results/OriginalFiles/modbat_modbat.test.ComplexLaunch5_-s\=1-n\=2--log-level\=fine--no-redirect-out.log
```
The Results will be : (because these folders {1_gram/, 2_gram/, 3_gram/, 4_gram/,  5_gram/} exist)
```bash
5_gram -> debug=-Doesn't exist-
5_gram -> info=65.9
5_gram -> error=-Doesn't exist-
5_gram -> warning=-Doesn't exist-
5_gram -> fine=28.3
5_gram -> raw=100.0


4_gram -> debug=-Doesn't exist-
4_gram -> info=70.9
4_gram -> error=-Doesn't exist-
4_gram -> warning=-Doesn't exist-
4_gram -> fine=41.1
4_gram -> raw=100.0


3_gram -> debug=-Doesn't exist-
3_gram -> info=74.6
3_gram -> error=-Doesn't exist-
3_gram -> warning=-Doesn't exist-
3_gram -> fine=50.0
3_gram -> raw=100.0


2_gram -> debug=-Doesn't exist-
2_gram -> info=77.4
2_gram -> error=-Doesn't exist-
2_gram -> warning=-Doesn't exist-
2_gram -> fine=56.5
2_gram -> raw=100.0


1_gram -> debug=-Doesn't exist-
1_gram -> info=89.4
1_gram -> error=-Doesn't exist-
1_gram -> warning=-Doesn't exist-
1_gram -> fine=75.2
1_gram -> raw=100.0
```

To generate it, it is necessary to have updated version of 
   - Ranking

## Code adaptable
To adapt the code, the different name of folder could be changed directly in the main.py program.


## Support
Get in touch with me at alexandre.fournel@ensta.fr

## Author
Alexandre FOURNEL supervized by Cyrille Artho 
KTH Royal Institute of Technology