#!/bin/bash

source ssh-monitoring-lib.sh

PREV_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')
echo "SSH service started"

while true
do
	NEW_USER=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')
	TMP=$(check_ssh_users "$PREV_USER" "$NEW_USER")
	if [ -n "$TMP" ]	
	then
		PREV_USER=$NEW_USER
		echo "$TMP successfully login"
		notify-send "$TMP successfully login"
	fi
	sleep 30
done

