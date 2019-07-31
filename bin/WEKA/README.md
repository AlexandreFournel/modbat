# Programs for analysis Log Err for Modbat Files. 

Here is available severals program to analyse Log Errors Modbat files. 
All these python programs and the shell executable file are managed by main.py program. 

Python version used : Python 3.6.5 :: Anaconda, Inc.
WEKA version used : 3.8.3 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install progress.

```bash
pip install progress
```

## Usage

### Generate Subfiles
With .log and .err files in modbat/log/ {modbat, config, modbat.config.ConfigTest}, for each file, you can generate 6 files, with the following extension:
   - .warning
   - .debug
   - .info
   - .fine
   - .error
   - .raw
In the original file, if the line begins with [INFO], this lines will be added to the .info file generated.

```bash
python3 main.py generateFiles originRepository ResultRepository ExtensionOfFilesWeWantToStudy
```

Example:
```bash
python3 main.py generateFiles ../log/ results/ err log
```

A Folder "Files", in this current repository, will created. In it, the different files generated and filtred. 

### Generate Ngram
It is possible to generate a list of unique ngram (1gram, 2gram, 3gram and 4gram) by folder {modbat, config, modbat.config.ConfigTest}. 

```bash
python3 main.py generateNGram ResultRepository ngrams
```

Example
```bash
python3 main.py generateNGram Results/ 1 2 3 4 5
```

4 folders are generated {1gram, 2gram, 3gram, 4gram}. 
In them, 3 folders {modbat, config, modbat.config.ConfigTest} which countain 2 generated files :
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
in {1gram, 2gram, 3gram, 4gram}/{modbat, config, modbat.config.ConfigTest}

```bash
python3 main.py generateNGramByFile ResultRepository ngrams
```

Example 
```bash
python3 main.py generateNGramByFile Results/ 1 2 3 4 5
```

To generate it, it is necessary to have updated version of 
   - sequence_list
   - sequence_list_with_name_files

The "sequence_list_by_files" lines are composed by :
```text
ngram__nameOfFile1::occurence__nameOfFile2::occurence__ ... __nameOfFile?::occurence
```

In other words, each line of this file lists one unique ngram with the name of the different files where the ngram appear. The file name is followed by the occurence. 


### Generate A Ranking of Similarities Between 2 Files
It is possible to generate 
   - Ranking
in {1gram, 2gram, 3gram, 4gram}/{modbat, config, modbat.config.ConfigTest}

```bash
python3 main.py rankSimilarities ResultRepository ngrams
```

Example
```bash
python3 main.py rankSimilarities Results/ 1 2 3 4 5
```

To generate it, it is necessary to have updated version of 
   - sequence_list_by_files

The "Ranking" lines are composed by :
```text
percentageOfSimilarities__nameOfFile1__nameOfFile2
```

In other words, every 2 files are compared. Thanks to the Jaccard Index, we are dividing the intersect of in-commun ngrams by the union of ngrams of these 2 files. 



### Print Every 2 Files If They Have More Than x% of Similarities
It is possible to print a list of 2 files which have more than X percentage of similarities. 

This file use a python program which returns a list of 6 value. For 2 different files, for a certain ngram, the elements of this list are equals to the percentage of similarities between :
   - file1.warning and file2.warning
   - file1.error and file2.error
   - file1.info and file2.info
   - file1.debug and file2.debug
   - file1.fine and file2.fine
   - file1.raw and file2.raw

The main program recover these lists for every ngram, averages the result and print the 2 lists if the average result is bigger than the percentage you choose. 

```bash
python3 main.py listOfSimilarFiles ResultRepository Pourcentage    
```

Example
```bash
python3 main.py listOfSimilarFiles Results/ 50
```
To generate it, it is necessary to have updated version of 
   - Ranking


### Generate Arff Files compatible with WEKA software
It is possible to generate ARFF files by folder {1gram, 2gram, 3gram and 4gram}/{modbat, config, modbat.config.ConfigTest}. 

```bash
python3 main.py generateArffDoc Results/ 1 2 3 4 5
```

This will create sequences_occurences.arff files in the different folders. 

The "sequences_occurences.arff" lines are composed by :
```text
nameOfFile1, nb_of_occurences_of_1st_ngram, nb_of_occurences_of_2nd_ngram...
```

To generate it, it is necessary to have updated version of 
   - sequence_list

### Test The Similarities Of 2 Files
It is possible to generate ARFF files by folder {1gram, 2gram, 3gram and 4gram}/{modbat, config, modbat.config.ConfigTest}. 

```bash
python3 main.py test2Files ResultRepository nameFile1 nameFile2
```

Example:
```bash
python3 main.py test2Files Results/ Results/OriginalFiles/modbat_modbat.test.ComplexLaunch6_-s\=1-n\=2--log-level\=fine--no-redirect-out.log Results/OriginalFiles/modbat_modbat.test.ComplexLaunch5_-s\=1-n\=2--log-level\=fine--no-redirect-out.log
```
Result
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