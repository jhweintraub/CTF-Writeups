`Prompt - We have to use Microsoft Word at the office!? Oof...`

Open the word document and all you see is the word `oof`. Luckily I remembered that microsoft word files are basically specially parsed zip files, and can be unzipped to reveal internal. 

Run recursive grep on that directory and you can find the flag

`grep -R flag{ microsooft`

`flag{oof_is_right_why_gfxdata_though}`