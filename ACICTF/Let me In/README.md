Web Security - This one was interesting. After going to the web site we find /admin with a login page, password only, no username.

Simple SQL Injection ' OR 1=1;-- didn't work but there is a "Resend Password Option" that opens up a alert() pane with the following message

`Email sent to vault.master@cyberstakes.club!`

I wonder if I can intercept that request and change the email to my own
Fire up burpsuite and intercept the request and you'll see the parameter

`email=vault.master%40cyberstakes.club`

Let's just replace that with our own URL encoded email and after a few seconds we get the following email 

```
Admin,

Here is the password to enter the vault.  Do not share this with anyone, enjoy your stay.

PW: pJ6xQrzG3zU0wBMHD1ZItBZHdKX1Xo5o
```

We plug that back into the password prompt and get the flag

ACI{2634ee6c147b1303}



