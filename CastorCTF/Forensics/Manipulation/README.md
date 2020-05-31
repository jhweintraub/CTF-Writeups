`Prompt - One of our clients sent us the password but we got this instead. He insists the password is in the image, can you help us?`

The file says its a png but can't open. When you open it in a hex editor you notice that it's not the raw bytes, its the full xxd format with line numbers and hex translation next to it, so if we carve out just the raw bytes and move it to a file we should get the flag right? after moving it to a file with just the bytes the file still doesn't load and `file` command says its still just ascii text, so I wonder if it's a magic bytes problem. I checked the bytes for png cause that's what the original filename was but that didn't work until I realized it had all except for the first two bytes needed for it to be a jpg. I add them in at the start and the image loads and out pops the flag


castorsCTF{H3r3_Is_y0uR_Fl4gg}