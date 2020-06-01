`Prompt - We suspect a user has been typing faster than a computer. Our analyst don't know what to make of it, maybe you will be the one to shine light on the subject.`

The file is a pcap, opened in wireshark we get only a bunch of packets for USB protocol. Based on the name of the challenge and the misc. data field `leftover packet data`, we can assume these are packets transmitted by a keylogger - Since there's only one data field we can export to csv and carve out that field

I was able to find a script online that using known USB-byte mappings for the data field converted it to the corresponding ascii values

We find the flag hidden in the wierd data and with a bit of toying with the l33tspeak we can grab the flag

`castorsCTF{1stiswhatyouwant}`
