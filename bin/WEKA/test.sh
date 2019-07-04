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
        FOLDER="Files/mobat/"
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