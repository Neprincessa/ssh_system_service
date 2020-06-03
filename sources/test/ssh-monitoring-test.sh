#!/bin/bash

source ../service/ssh-monitoring-lib.sh

CURRENT=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')

sudo useradd new_user
sudo -u new_user mkdir -p /home/new_user/.ssh
sudo -u new_user chmod u+rwx /home/new_user/.ssh

sleep 15
sudo -u new_user ssh-keygen -q -N "" -f /home/new_user/.ssh/id_rsa  &> /dev/null
sudo -u new_user cp /home/new_user/.ssh/id_rsa.pub /home/new_user/.ssh/authorized_keys

sudo -u new_user ssh -tt -o "StrictHostKeyChecking=no" -i /home/new_user/.ssh/id_rsa 127.0.0.1 "sleep 5" &> /dev/null &

NEW=$(ps -eo command | grep "^sshd:.*@.*$" | awk -F'[ @]' '{print $2}')

RES=$(check_ssh_users $CURRENT $NEW)

sudo userdel -fr new_user &> /dev/null

if [[ $RES == *"new"* ]]
then 
	echo  "Service error"
	exit 1
fi

echo "Success service work"
man ssh-monitoring
exit 0
