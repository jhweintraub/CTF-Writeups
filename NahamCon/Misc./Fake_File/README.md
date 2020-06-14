`Prompt - Wait... where is the flag?`

We are given a shell in a user directory. Running ls we get nothing but when we do `ls -a` there's a strange non-parent directory also called `..`

We can't cd into it but running `file .*` reveals its a ascii text file with the name actually being `.. `. with a space at the end. We can't escape `..` to view it so if we try to cat all files in the directory we get the flag

`cat .*` -> `flag{we_should_have_been_worried_about_u2k_not_y2k}`