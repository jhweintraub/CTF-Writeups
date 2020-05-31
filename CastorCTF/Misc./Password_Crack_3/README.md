
The hash is a sha256, they tell us the flag needs to be in the right format, using hashcat and crackstation with rockyou.txt didn't return anything so I wondered if maybe I needed to change the format of my wordlist, that I could dictionary crack this with the flag itself as the keyword

I wrote a quick shell script to take every word in rockyou.txt and place it in the flag format `castorsCTF{}` and append it to its own file

I then ran hashcat on the hash and out popped the flag

7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12:castorsCTF{theformat!}

`castorsCTF{theformat!}`