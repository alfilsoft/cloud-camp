#!/bin/bash

echo "Hello add the dir name"
read dir_name

echo "Creating dir ... $dir_name"
rm -rf $dir_name
mkdir $dir_name

sleep 1
message="creating files"
for i in {0..10}; do
	date > "$dir_name/file_$i"
	sleep 1
	message="$message."
	echo "$message"
done

echo "Files were created sucessfully"

ls $dir_name

cat $dir_name/file_1
cat $dir_name/file_9

