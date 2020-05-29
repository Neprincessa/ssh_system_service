#!/bin/bash

PREV_USER=$(ps aux | grep ssh | grep @ | tr -s ' ' ' ' | cut -d":" -f4 | cut -d'@' -f1)
echo "$PREV_USER has been succesfully login"

while true
do
    NEW_USER=$(ps aux | grep ssh | grep @ | tr -s ' ' ' ' | cut -d":" -f4 | cut -d'@' -f1)
    RES=$(diff <( echo "$PREV_USER") <( echo "$NEW_USER") |  awk '{print $2}' )
    if [ -n "$RES" ]
    then
        echo "$RES"
        notify-send "$RES has been succesfully login"
    fi
    PREV_USER=$NEW_USER
    sleep 30
done

