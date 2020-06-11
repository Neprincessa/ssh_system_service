#!/bin/bash

source monitor_ssh_lib.sh

logger "SSH service started"

PREV_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}') 

trap "logger SSH service catched USR1 signal;  exit 0"  SIGUSR1

while true
do

	NEW_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')
	TMP=$(check_ssh_users "$PREV_USER" "$NEW_USER")
	if [ -n "$TMP" ]	
	then
		PREV_USER=$NEW_USER
		logger $TMP successfully login
		echo "$TMP successfully login" | wall
		echo "$TMP successfully login"
	fi

	sleep 30 & 
	wait
done
 
