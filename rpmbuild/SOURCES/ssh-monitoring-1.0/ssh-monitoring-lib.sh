#!/bin/bash



function check_ssh_users {
	RES=$(diff <( echo "$PREV_USER") <( echo "$NEW_USER") |  grep ">" )
	echo "$RES"
}
