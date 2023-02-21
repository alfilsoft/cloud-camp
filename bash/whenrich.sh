#!/bin/bash

echo "var name $NAME_ENV"

echo "what is your name"
read name

echo "how old are you"
read age
echo "name: $name and age: $age"

echo "you are going to be rich $((RANDOM % age))"
