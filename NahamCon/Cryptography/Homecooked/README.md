`Prompt - I cannot get this to decrypt!`

When you run the file you quickly see the first 5 or so letters of the flag, and then a few seconds later a few more letters appear. A quick inspection shows that the flag is the result of xor'ing the base64 decoded ciphertext with a palindromic prime number. However, the problem is that the xor key increments slowly because it checks if the key is prime by brute forcing prime, instead of using a faster library. If we replace the manual prime calculation function with the sympy library isprime() function it will run much faster and the flag will print out. We don't need to change the palindromic function because it's already very quick

`flag{pR1m3s_4re_co0ler_Wh3n_pal1nDr0miC}`