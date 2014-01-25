#!/bin/bash

for file in /{,s,usr/,usr/s}bin/*ssh*
# #             ^    Find all executable files ending in "ssh"
#+                 in /bin and /usr/bin directories.
do
        if [ -x "$file" ]
        then
          echo $file
        fi
done
