`Prompt - We are so restricted here in Alkatraz. Can you help us break out?`

We're dropped in to a very restricted rbash shell in a directory with flag.txt, no cat, less, more, etc. and we need to print the flag. 


`while read line; do echo "$line"; done < flag.txt` to read line in the file supplied as input and echo it out

`flag{congrats_you_just_escaped_alkatraz}`

