Prompt - We went to apply for a tax-filing extension with the IRS, and they replied with this image saying it contained the code we needed. Unfortunately, our computer refuses to display it and just says that it isn't a PNG... flag.png

Given it's a forensics question we check file command first we get the following response

`flag.png: Zip archive data, at least v2.0 to extract`

if we change the name of the file to flag.zip we get an zip archive. Unpack it and there's the flag

ACI{Something_witty_072f6a6f}