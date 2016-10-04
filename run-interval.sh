#! /bin/bash

while true
do
	echo `date "+%F %H:%M:%S"`, `ls -l /home/ubuntu/logs/test.log | cut -d" " -f5`
	sleep 1
done
