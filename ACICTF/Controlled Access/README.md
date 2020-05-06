Prompt - "We've been asked to help a certificate authority figure out what a device they found plugged into their network was doing. They were able to dump the firmware and would like to know if it allowed the attacker to connect to any devices that their firewall (which blocks inbound SSH) would have stopped. Their internal domain uses 'digisigner.local' for DNS host names. The flag is the hostname of the internal host that the hacker targeted (i.e. ACI{[local hostname targeted]})."


There was a link to two pages - One to a website for a Product called Shark Jack and the other to a filesystem bin file for the product

Running `binwalk -e` on the bin file we get a filesystem to peruse. After looking through the documentation we see this 

"/root/loot/ – home to log files and other loot stored by payloads" so we go there

We don't see root/loot but there is a file under /root/payload/payload.sh - Seems suspicious

We find this line `INTERNAL_HOST=rootca.digisigner.local`

Going back to the prompt this gives us the flag

ACI{rootca.digisigner.local}



