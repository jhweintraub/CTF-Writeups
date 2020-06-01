# castorsCTF Post-Mortem

----
## What was it?
see [castorsCTF](https://castorsctf20.ctfd.io/)

> Entry-level CTF for Undergraduate Students


I competed as a team of Myself and Matt O'Brian, a friend of mine from the UGA SCS

----
## How did I do?
1. 157/761 Teams
2. 16/43 Challenges solved

----
## Challenge List

### Crypto

 - Goose Chase
 - One Trick Pony


### Forensics

 - Manipulation
 - Leftovers

**Misc.**

- Gif
- Password Crack 1-3
- Welcome!
- Readme

**Reverse Engineering**

- Vault0 & Vault 1
- Stacking

**Pwn**

- abcbof

## What I learned
- Radare2 is a very useful tool for dissassembling in the command line as well as Ghidra, lets you step manually into information to isolate in the console.
- Using fd and lsof can be very useful for Web LFI attacks to find the location of files you're looking for
- Strange PCAP protocols are usually your best place to look when approaching forensics categories, good to add to the list of low-hanging fruit - In this case USB
- Autopsy = Great Forensics tool for disk images, definitely on my list of things to learn more about


## Things I need to work on
- Still Reverse engineering & Assembly - Radare2
- Wireshark Decoding options - Familiar with protocols and packet contents
- Being more aggressive with my encodings - A lot of problems were solved by xor'ing seemingly random data, being more aggressive with following every possible lead
- Knowing when challenges can be solved with simple one-liners and tools and when some challenges require scripting - Need a better knowledge of Pwntools Library for python