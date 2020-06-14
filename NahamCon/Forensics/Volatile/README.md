`Prompt - No Prompt`

The file given to us is a gzipped tar archive. I didn't upload it here because it was like 400mb zipped up and 2.15 GB unpacked. When you get the file it's a .raw file, with `file memdump.raw` just returning `data`. However, the title of the challenge implies that you should use the forensics tool volatility. Let's load it up

`vol.py -f memdrump.raw imageinfo` gives us the info we should know abou the image. Primarily that it's profile is `Win7SP1x86_23418`

I ran through the some of the usual commands like `hashdump` to see if there's a password, but this turned out to be a red herring as none of the hashes matchd known NTLM ones. 

eventually i tried `cmdscan` and out came the flag. Lesson = Create checklist of volatility commands to run through on this type of challenge

`vol.py --profile=Win7SP1x86_23418 -f memdump.raw cmdscan`

```
CommandProcess: conhost.exe Pid: 3468
CommandHistory: 0x2f0448 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 1 LastAdded: 0 LastDisplayed: 0
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x5c
Cmd #0 @ 0x2f4680: echo JCTF{nice_volatility_tricks_bro}
Cmd #1 @ 0x2d0031: ?????????????????????????T???????
Cmd #17 @ 0x2d0037: ??????????????????????T???????
Cmd #36 @ 0x2c00c4: .?/?,???,
Cmd #37 @ 0x2ed038: /?,???????.
```


`JCTF{nice_volatility_tricks_bro}`