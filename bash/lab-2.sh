#!/bin/bash

echo "lab 2"
band=true
articles=()

while $band;do
	echo ="Add one artycle"
	read article
	articles+=($article)

	echo ="Do you want to add something else"
	read finish
	if [[ $finish == "y" ]]; then
		band=false
	fi
done

echo  "storing shopping car"
sleep 1

echo "${articles[@]}" > bought_stuff.txt

echo "articles in bought_stuff.txt"
