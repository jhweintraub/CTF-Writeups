Web Security

Prompt - "Since in-person events are currently banned, some magician we've never heard of is trying to sell us on the idea of a "digital" magic show where the magician logs in using an impossible password. For added assurances, one lucky audience member is able to login and see the hash of the password as proof the password is impossible. We're willing to bet the secret to this magic trick is not all that complicated. http://challenge.acictf.com:10952"

Going to the page we are greeted with a standard username and password login prompt. Seeing "hash" i'm automatically thinking this is something to do with the SQL injection and getting password hashes to crack

I throw the standard injection into the username `' OR 1=1 -- `to bypass password and return the username and it works. I get this in response

`Welcome admin! The "hash" for account 'houdini' is 'Not a hash'.`

Now we know there's a user houdini and their "hash" is "Not a hash". Now obviously that's not a real hash but mean's there's something in the table to get with that information. Let's see what we can inject. The account houdini:Not a hash did not work unfortunately. We know there's a field called pwHash from injecting as admin, so let's see if we can get information from it let's inject this into the username field

`' or pwHash='Not a hash';--`

Works and we're in for user Houdini by bypassing the pwHash check and get the flag

ACI{fd35465a027eeee3be0249d9f86}


