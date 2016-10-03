#! /bin/bash

while true
do
	echo `date "+%F %H:%M:%S"`, `ls -l test.log | cut -d" " -f5`
	sleep 1
done
