`Prompt - Dang it, not again...`

The file is a keepass password database, but it's encrypted so we need to get the password. Luckily john the ripper has a helper program to convert (after we add the .kdb file extension to it can be recognized by kpcli)

`keepass2john easy_keesy.kdb > easy_keesy.hash`

`john easy_keesy.hash --wordlist=rockyou.txt`

the password comes out to be `monkeys`. 

Load it up and we find out there's a group `Root/` and one password inside it, the flag

`flag{jtr_found_the_keys_to_kingdom}`
