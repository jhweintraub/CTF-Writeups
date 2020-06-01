`Prompt - We found a thumb drive lying on the floor. Luckily, it wasn't a rubber ducky or contain a ransomware; either way, we're still suspicious. We already went ahead and created the image, help us by analyzing it.`

*I didn't upload the actual file here cause it's 1.5 GB large and way too big*

Running `file` on it shows its a DOS/MBR boot sector, not being able to open it in qemu I ran autopsy on the file and check for low hanging fruit. 

Open and run autopsy and go to deleted files and there's a file called `C:/Secrets/_lag.txt` with the contents `Y2FzdG9yc0NURntmMHIzbnMxY1NfbHNfSVRzXzBXbl9iMFNTfQ==`

Decode the base64 and you get the flag

`castorsCTF{f0r3ns1cS_ls_ITs_0Wn_b0SS}`