# Programs for analysis Log Err for Modbat Files. 

Here is available severals program to analyse Log Errors Modbat files. 
All these python programs and the shell executable file are managed by main.py program. 

Python version used : Python 3.6.5 :: Anaconda, Inc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install progress
```

## Usage

### Program 1
With .log and .err files in modbat/log/ {modbat, config, modbat.config.ConfigTest}, for each file, you can generate 6 files, with the following extension:
   - .warning
   _ .debug
   _ .info
   _ .fine
   - .error
   - .raw
In the original file, if the line begins with [INFO], this lines will be added to the .info file generated.
```bash
python3 main.py generateFiles
```
A Folder "Files", in this current repository, will created. In it, 3 folder {modbat, config, modbat.config.ConfigTest} will all the files generated in them. 

### Program 2
For each file with the following extension:
   - .warning
   _ .debug
   _ .info
   _ .fine
   - .error
   - .raw
we can replace or delete lines if regex matches. In this current version, we are only filtering lines where seeds are not preceded by prefix (as [INFO] for example)
All empty files in Files/{modbat, config, modbat.config.ConfigTest} are removed to have faster program. 
To change the rules of filtering, please add what you want in regex.regex_files_err_warning_fine.py .
```bash
python3 main.py filterFiles
```

### Program 3
For each file with the following extension:
   - .warning
   _ .debug
   _ .info
   _ .fine
   - .error
   - .raw
it is possible to generate a list of unique ngram (1gram, 2gram, 3gram and 4gram) by folder {modbat, config, modbat.config.ConfigTest}. 
```bash
python3 main.py generateNGram
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)