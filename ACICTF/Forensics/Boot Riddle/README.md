Prompt - "This floppy disk image boots, but instead of a flag we see some silly riddle..."

Another MBR Forensics Challenge

Upon booting it up in qemu we get the riddle "Your Flag awaits at 0x7DC0". After perusing the man page for qemu I boot it up again in monitor mode in my terminal to try and debug and access that memory address

`qemu-system-x86_64 floppy.img -monitor stdio`

The Man pages are very helpful and with a simple command we are able to print out the memory address and we get the following

`xp /3c 0x7DC0` - Print out the next 3 items in character form starting at address 0x7DC0 which returns us the flag

ACI{REALmode}

