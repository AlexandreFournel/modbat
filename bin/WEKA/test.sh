#!/bin/bash
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

find Files/modbat.config.ConfigTest/. -name '*.log.*' -o -name '*.err.*' | xargs cat | sort -u > Files/modbat.config.ConfigTest/line_list
find Files/config/. -name '*.log.*' -o -name '*.err.*' | xargs cat | sort -u > Files/config/line_list
find Files/modbat/. -name '*.log.*' -o -name '*.err.*' | xargs cat | sort -u > Files/modbat/line_list


tr " " "\n" < Files/modbat.config.ConfigTest/line_list > Files/modbat.config.ConfigTest/word_list