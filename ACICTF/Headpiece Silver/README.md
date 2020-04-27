Very similar to Really Senseless Admin Challenge - Another RSA but this time instead of giving us p & q we need to factor n. It's also asking us for a 
password instead of giving us the flag directly by connecting through netcat

quick look in factordb.com and we now have all the info we need

n = 122298190177919866881639090045815514691491489519639425496178483984084352945237
e = 65537
c = 0x36ba8ba886491c919aad9b2c15d2a464f368c112562944d19b24b22914f5a54a

p = 331958624987283540029528593686625501199
q = 368413955753084554445712063216091990363

we can use the same decrypt equation from the previous challenge


`phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(hex(m))`

decoding the hex and we get a password - if we plug that into the nc connection it gives us the flag

ACI{0b5393d8035c553e5c350ed451a}