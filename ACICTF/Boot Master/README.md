Prompt - "We found another floppy disk image, but we can't get this one to boot like we did the last one. The disk had been sitting around for a while so we're wondering if some of the data was corrupted. Any ideas?"

Just like the Bootcamp Challenge we are given a file called floppy.img. Because the file name is the same as the other challenge and the titles similar the first thing I did was try and boot it up. Unsurprisingly it failed. However, then I ran the file command on the img again and got a different result

"floppy.img: data"

Strange. We know it should be a DOS/MBR file so let's do some magic byte research

Opening up the file in our hex editor we see some basic bytes at the top and then a lot of zero's before a final "51AA". This immediately Jumps out.

After some research on the MBR Wikipedia page I spot that the last two bytes of a DOS/MBR header should be "55AA" in hex, not 51, so I change it

I then re-run file on floppy.img and get the DOS/MBR response i'm looking for and boot and there's the flag

ACI{fails2boot}