`Prompt - "Early this morning, a breach occurred on the server hosting our next-gen drone development repository. It is your job to figure out what was taken: challenge.zip"`

This challenge gave us a challenge.pcap file to look through. Time to fire up wireshark

Luckily it's a manageable number of packets for us. I click through the TCP Stream and it's a conversation that occurs over an IRC connection. Two lines jump out at me

`:doom!sid316808@gateway/web/irccloud.com/x-amtasgjkytkqghpm PRIVMSG #drone-soc :here's a link to an encrypted zip of the traffic capture: http://file.io/jlngsr`

and 

`:doom!sid316808@gateway/web/irccloud.com/x-amtasgjkytkqghpm PRIVMSG #drone-soc :the password to the zip is 'dronehack2019'`

The first one had a link that was a red-herring and lead to nothing. However, the mention of the zip file made me wonder if maybe there is more objects hidden within this pcap. I export HTTP Objects, and there's only one. A Zip file. I export it and rename it and go to unzip when confronted with a password. Lucky I already found it "dronehack2019". Within that file there's yet another file - capture.pcap

I look through the limited packets and TCP stream and find very little, nothing to export and nothing else obvious. Remembering something I had seen online I decided to run `strings` on the pcap and low and behold, there's the flag at the bottom

ACI{3a76f2403e614fe875dad0b7b6d}