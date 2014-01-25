#/bin/bash

while read line           
do          
	if [ -n "$line" ]; then 
	    	echo $line
		(echo 1 >> threads.running; ssh $line $@ >> output-$line; tail -n +2 threads.running > threads.running) & 
		while [ `cat threads.running | wc -l` -gt 4 ]; do
			sleep 1
		done
	fi  
done
