#!/bin/bash
# while.bash

i=0
while read line;
do
  foo[i]=$line
  let i=i+1
done
echo "i is $i, size of foo ${#foo[@]}"
