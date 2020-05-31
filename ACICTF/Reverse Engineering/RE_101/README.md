Reverse Engineering Challenge. 

Prompt - "Reverse engineering can definitely be intimidating so we have a simple program with which you can start. If you don't know where to start, check out the hints where we'll walk you through two different ways to solve this problem."

We're given a pre-compiled ELF Executable. When it's run nothing happens

`objdump -t RE101` to get all the Symbols and see if there's any low hanging fruit

We get 1 interesting thing

`0804911a g 	.bss	00000000 flag`

There's an object flag ag 0x0804911a - Let's open it up in dissassembler ghidra

Looking at that address and function entry() we get the following lines in memory
```
  flag = 0x41;
  DAT_0804911b = 0x43;
  DAT_0804911c = 0x49;
  DAT_0804911d = 0x7b;
  DAT_0804911e = 0x61;
  DAT_0804911f = 0x5f;
  DAT_08049120 = 0x62;
  DAT_08049121 = 0x79;
  DAT_08049122 = 0x74;
  DAT_08049123 = 0x65;
  DAT_08049124 = 0x5f;
  DAT_08049125 = 0x61;
  DAT_08049126 = 0x74;
  DAT_08049127 = 0x5f;
  DAT_08049128 = 0x61;
  DAT_08049129 = 0x5f;
  DAT_0804912a = 0x74;
  DAT_0804912b = 0x69;
  DAT_0804912c = 0x6d;
  DAT_0804912d = 0x65;
  DAT_0804912e = 0x7d;
```
When we isolate those hex values and then convert them back to ascii from hex we get the flag

ACI{a_byte_at_a_time}