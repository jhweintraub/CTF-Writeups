`Prompt - "We think Jolly Jeff is up to no good. See if you can find the hidden message in his JPEG Jammer."`

A forensics challenge although there's not anything to download. Going to the page we get the following (image included)

You upload your own image and then do something to it. Most of the choices were self explanatory and worked as displayed, except 1 - Shadow

I uploaded a random image and when I downloaded it and looked at it after the transformation, I got a white blank canvas. Strange. So i opened it up in the hex editor because file command told me it was still in jpeg format.

Upon scrolling I noticed a strange amount of Zero's and that there were two different instances of the "JFIF" identifier for jpeg files. I then realized that the site had stacked a different image on top of the image I had given it, jamming it with something to overlay. I removed the unnecesarry bytes and found an image with the flag [included] that needed to be flipped. Luckily I already had a tool for that

After flipping it around I was able to get the flag

ACI{322a694c955f893dceb0bd7039d}