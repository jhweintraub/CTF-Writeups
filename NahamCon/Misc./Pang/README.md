`Prompt - This file does not open!`

`pngcheck pang` returns the following

```
pang  CRC error in chunk IHDR (computed f9f1da99, expected f9f1ea99)
ERROR: pang
```

Open your hex editor of choice and search for `f9f1da99` and replace it with `f9f1ea99`, and the file becomes viewable with the flag

`flag{wham_bam_thank_you_for_the_flag_maam}`