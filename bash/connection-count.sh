#!/bin/bash

# Another netstat use case
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

netstat -apentu | grep tcp | grep -E "[A-Z]{4,10}" | awk '{ print $6 }' | sort | uniq -c
