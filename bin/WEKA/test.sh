#!/bin/bash
function create_files {
    FILE_WITHOUT_MAIN_PATH="ERROR"
    NAME_FILE="ERROR"
    FOLDER="ERROR"
    NAME_FILE_WITHOUT_SLASH="ERROR"
    (find ../../log -name "*.err" -o -name "*.log") | while read FILE; do
        
    FILE_WITHOUT_MAIN_PATH=${FILE/..\/..\/log/}
        
    if [[ $FILE_WITHOUT_MAIN_PATH =~ "/config/" ]]; then
        FOLDER="Files/config/"
        NAME_FILE=${FILE_WITHOUT_MAIN_PATH/\/config\//}
        
    elif [[ $FILE_WITHOUT_MAIN_PATH =~ "/modbat/" ]]; then 
        FOLDER="Files/modbat/"
        NAME_FILE=${FILE_WITHOUT_MAIN_PATH/\/modbat\//}
    else
        FOLDER="Files/modbat.config.ConfigTest/"
        NAME_FILE=${FILE_WITHOUT_MAIN_PATH/\/modbat.config.ConfigTest\//}
    fi
    mkdir -p $FOLDER;
    NAME_FILE_WITHOUT_SLASH=${NAME_FILE//\//\_}
    grep '^.DEBUG' $FILE > $FOLDER$NAME_FILE_WITHOUT_SLASH.debug 
    grep '^.INFO' $FILE > $FOLDER$NAME_FILE_WITHOUT_SLASH.info 
    grep '^.FINE' $FILE > $FOLDER$NAME_FILE_WITHOUT_SLASH.fine 
    grep '^.ERROR' $FILE > $FOLDER$NAME_FILE_WITHOUT_SLASH.error 
    grep '^.WARNING' $FILE > $FOLDER$NAME_FILE_WITHOUT_SLASH.warning
    grep -v '^\[' $FILE > $FOLDER$NAME_FILE_WITHOUT_SLASH.raw 
    done
}

function create_words_lines_list {
    find Files/modbat.config.ConfigTest/. -name '*.log.*' -o -name '*.err.*' | xargs cat | sort -u > Files/modbat.config.ConfigTest/line_list
    find Files/config/. -name '*.log.*' -o -name '*.err.*' | xargs cat | sort -u > Files/config/line_list
    find Files/modbat/. -name '*.log.*' -o -name '*.err.*' | xargs cat | sort -u > Files/modbat/line_list



    function textreplace {
        tr "[ \t]+" "\n" < $1line_list > $1word_list
        sed -i "" "/^[ \t]*$/d" $1word_list
        sed -i '' 's/[\.\",{}:();]*$//' $1word_list
        sed -i '' 's/^[\.\",{}:();]*//' $1word_list
        sort -u Files/modbat/word_list > $1word2_list
        remove $1 "word2_list" "word_list"
    }

    function remove {
        cp $1$2 $1$3
        rm $1$2
    }

    function number_lines {
        grep -n ^ $1word_list > $1word2_list
        grep -n ^ $1line_list > $1line2_list
        remove $1 "word2_list" "word_list"
        remove $1 "line2_list" "line_list"
    }

    function emptyLines {
        sed 's/[\x01-\x1F\x7F]//g' $1word_list > $2word2_list
       remove $1 "word2_list" "word_list"
    }

    textreplace "Files/modbat.config.ConfigTest/"
    textreplace "Files/modbat/"
    textreplace "Files/config/"

    #emptyLines "Files/modbat.config.ConfigTest/"
    #mptyLines "Files/modbat/"
    #emptyLines "Files/config/"


    #number_lines "Files/modbat.config.ConfigTest/"
    #number_lines "Files/modbat/"
    #number_lines "Files/config/"
}





###################### Function to uncomment #################
#create_files
create_words_lines_list