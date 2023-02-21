#!/bin/bash

echo "pick a number between 0 and 100"

read number

if [[ -z $number || $number -gt 100 || $number -lt 0 ]]; then 
	echo "try again"
	exit
if

echo "your number is $number"

sleep 1

echo "checking...."

sleep 1

echo "1 2 3 ...."

sleep 2 

if [[ $number == 20 ]]; then
	echo "you win : D"
else
	echo "you lose"
fi
