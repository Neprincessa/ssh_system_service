#!/bin/bash

source monitor_ssh_lib.sh

PREV_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')

trap "sleep 30; logger SSH service catched USR1 signal; logger SSH service stopped; exit 0"  SIGUSR1
logger "SSH service started"

while true
do
	NEW_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')
	TMP=$(check_ssh_users "$PREV_USER" "$NEW_USER")
	if [ -n "$TMP" ]	
	then
		PREV_USER=$NEW_USER
		logger $TMP successfully login
		notify-send "$TMP successfully login"
	fi
	sleep 30
done
 
