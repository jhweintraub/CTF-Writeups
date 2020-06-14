`Prompt - Become the admin!`

We're greeted with a page asking for a user to log in as. If you put in admin it returns a message saying only the admin can see the flag. Knowing the creator of the CTF is a fan of Mr. Robot i put in elliot and check the cookies and there's one with a string. Turns out to be a rot13 of the string `elliot`, so I make a rot13 of the string `admin` and change the cookie value. Reload the page and we get the flag

`flag{H4cK_aLL_7H3_C0okI3s}`