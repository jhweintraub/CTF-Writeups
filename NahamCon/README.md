# NahamCon CTF Post-Mortem
----
## What was it?
see [NahamCon](https://ctf.nahamcon.com/)

> Entry-level CTF hosted by YouTuber John Hammond and Friends


I competed as just myself, as teams were not allowed

----
## How did I do?
1. 369/2854 Teams - 87th Percentile
2. 24/72 Challenges solved - 33%

----
## Challenge List

### Crypto

 - Homecooked
 - Ooo-la-la
 - Raspberry
 - Twinning


### Forensics

 - Microsoft
 - Volatile

### Misc.

- Alkatrax
- CLISay
- Easy_Keesy
- Fake_file
- Hackermeme
- Mr. Robot
- Pang
- Peter Rabbit
- UGGC
- Vortex

### Reverse Engineering

- Vault0 & Vault 1
- Stacking

### Mobile

- Candroid
- Simple_App

### OSINT

- Finsta
- New Years Resolution
- Time_Keeper

### Web

- Agent_95
- Localghost
	

## What I learned
- In RSA Encryption p & q are not static two only variables, that you can use any list of factors as long as you do the math right to derive phi
- More Volatility commands for analyzing disk images
- Command like escape sequences for rbash and other important piping commands
- JSON Web Tokens are NOT encyption, just obfuscation and should be sure to check those more often


## Things I need to work on
- Not being afraid of complex challenges. You want to think of these competitions as being about winning but because I'm not anywhere near contention for top spot it should be about learning and I should not be afraid of spending hours on one challenge if it means I learn stuff. This is especially true of challenges where I don't already know everything, like on one of the DES challenges where I don't know how DES works and needed to do a lot of research
- Being more thorough in exploring possibilities. I missed a few challenges I should have gotten because I was missing the forest through the trees (like the last OSINT one I didn't solve)
- Not going straight to tools like a script kiddie. They are powerful and not saying never use them but often times they just aren't necesarry or won't reveal what you want them to (e.g. SQLMap)
- Picking topics I enjoy instead of trying to do it all and focusing more on those. I really enjoy forensics and cryptography more than Binary Exploitation and Reverse-Engineering. Spend more time on those
