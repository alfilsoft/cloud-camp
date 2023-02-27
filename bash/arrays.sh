#!/bin/bash

fruits=("apple" "peach" "pear" "banana")

echo "${fruits[@]}"

echo ${fruits[0]}

fruits+=("berry")

echo "${fruits[@]}"

unset fruits[1]

echo "${fruits[@]}"

for f in "${fruits[@]}"; do
	echo "f: $f"
done
