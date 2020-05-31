#!/bin/bash
input="rockyou.txt"
while IFS= read -r line
do
	var1="castorsCTF{"
	var2="}"
	echo "$var1$line$var2" >> copy_rockyou.txt
done < "$input"