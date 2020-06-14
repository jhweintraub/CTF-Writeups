```
Prompt - Will you find the flag, or get lost in the vortex?
Connect here:
nc jh2i.com 50017
```
The nc connection opens up an endless stream of data so lets pipe it into a file because hopefully it repeats

`nc jh2i.com 50017 > file`

it's a binary file so we can't grep it directly but we can run strings and grep that and we get the flag 

`strings file | grep flag{`

`flag{more_text_in_the_vortex}`

