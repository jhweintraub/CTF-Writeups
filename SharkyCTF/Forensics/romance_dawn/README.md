Corrupted PNG File. 

running file we know that this is in fact a PNG file so it's not a magic bytes question

`pngcheck 7uffy.png` returns the following

```
7uffy.png  illegal (unless recently approved) unknown, public chunk EASY
ERROR: 7uffy.png
```

The chunk is strange, so after some research i discover that the delimeter for a chunk is `IDAT` in hex, or `49 44 41 54`

let's go in to hex editor and change the first value where we see easy, and we get a part of the flag. So we use grep and replace all the values of "EASY" in the file until we get the whole image assembled and the flag

shkCTF{7uffy_1s_pr0ud_0f_y0u_0a2a9795f0bdf8d17e4}