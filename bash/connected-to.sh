#!/bin/bash

# This more like a nestat use case
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

if [[ -z "$1" ]]
	then
	SELF=$(hostname -I | cut -d' ' -f 1)
else
	SELF=$1
fi

echo "Assuming I am: " $SELF
netstat -apentu | grep "$SELF" | awk '{ print $5; }' | cut -d: -f 1 | grep -vE  "$SELF|0.0.0.0" | sort | uniq
