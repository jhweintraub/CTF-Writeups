Reverse Engineering

Prompt - "We developed this password-protected program which uses a super-secure, military-grade hash function with 256-bits of security to ensure only someone with the proper password can print the flag."

When you execute the binary you get the prompt: "Enter the password to get the flag: "


Objdump search returns two interesting things
`objdump -t lockbox`

```
0000000000000b80 l     O .rodata        0000000000000020              password_hash

0000000000000b40 l     O .rodata        0000000000000018              flag_format_string
```

When we open this in a disassembler ghidra and move to the main() function we see this code 

```
  fgets(local_58,0x40,stdin);
  sVar2 = strlen(local_58);
  local_ec = (int)sVar2;
  if (local_58[local_ec + -1] == '\n') {
    local_ec = local_ec + -1;
    local_58[local_ec] = '\0';
  }
  SHA256_Init(&local_e8);
  SHA256_Update(&local_e8,local_58,(long)local_ec);
  SHA256_Final(local_78,&local_e8);
  iVar1 = memcmp(local_78,password_hash,0x20);
  if (iVar1 == 0) {
    printf("%s: %s{%x_%s_%s_%s_%s}\n",&header,&prefix,0xc0de,&uses,&military,"grade","crypto");
    uVar3 = 0;
  }
```

The prompt takes your input from the prompt and puts it into &local_78, wherever that is doesn't matter. It then SHA256-hashes it and compares it to the value in 
"password_hash" and if its the same. If it should hopefully give us the flag. The dissassembler then takes us to where password_hash is and we see the following

```
                             password_hash                                   XREF[1]:     main:00100a11(*)  
        00100b80 c4 bb cb        undefine
                 1f be c9 
                 9d 65 bf 
           00100b80 c4              undefined1C4h                     [0]                               XREF[1]:     main:00100a11(*)  
           00100b81 bb              undefined1BBh                     [1]
           00100b82 cb              undefined1CBh                     [2]
           00100b83 1f              undefined11Fh                     [3]
           00100b84 be              undefined1BEh                     [4]
           00100b85 c9              undefined1C9h                     [5]
           00100b86 9d              undefined19Dh                     [6]
           00100b87 65              undefined165h                     [7]
           00100b88 bf              undefined1BFh                     [8]
           00100b89 59              undefined159h                     [9]
           00100b8a d8              undefined1D8h                     [10]
           00100b8b 5c              undefined15Ch                     [11]
           00100b8c 8c              undefined18Ch                     [12]
           00100b8d b6              undefined1B6h                     [13]
           00100b8e 2e              undefined12Eh                     [14]
           00100b8f e2              undefined1E2h                     [15]
           00100b90 db              undefined1DBh                     [16]
           00100b91 96              undefined196h                     [17]
           00100b92 3f              undefined13Fh                     [18]
           00100b93 0f              undefined10Fh                     [19]
           00100b94 e1              undefined1E1h                     [20]
           00100b95 06              undefined106h                     [21]
           00100b96 f4              undefined1F4h                     [22]
           00100b97 83              undefined183h                     [23]
           00100b98 d9              undefined1D9h                     [24]
           00100b99 af              undefined1AFh                     [25]
           00100b9a a7              undefined1A7h                     [26]
           00100b9b 3b              undefined13Bh                     [27]
           00100b9c d4              undefined1D4h                     [28]
           00100b9d e3              undefined1E3h                     [29]
           00100b9e 9a              undefined19Ah                     [30]
           00100b9f 8a              undefined18Ah                     [31]
```
Lot of hex values. Once we isolate all those values we and join them we get the following string
"c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a"

We already know it's a sha-256 so let's try and decrypt it online. Luckily we get a result which must be our password
"correct horse battery staple"

We plug it into our executable prompt and we get the flag

ACI{c0de_has_mil_grade_crypto}
