#!/bin/bash

PREV_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')
echo "SSH service started"

while true
do
    NEW_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')
    RES=$(diff <( echo "$PREV_USER") <( echo "$NEW_USER") |  grep ">" )
    if [ -n "$RES" ]
    then
        echo "$RES has been successfully login"
        notify-send "$RES has been succesfully login"
    fi
    PREV_USER=$NEW_USER
    sleep 30
done

