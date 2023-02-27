#!/bin/bash

echo "Test loops"

#iterate over files
for arch in /home/ec2-user/*; do
	echo $arch
done

#iterate over conditions

message="waiting"
while true; do
	message="$message."
	echo $message
	sleep 1
done
