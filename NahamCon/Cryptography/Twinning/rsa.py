from Crypto.Util.number import inverse

n = 34433071920899
e = 65537
c = 31080344913528

p = 5867969
q = 5867971

#if n factors into more than just p and q you can just the following
#factors = [array of factors in ints]
#phi = prod(i - 1 for i in factors) phi is just the sum of all the factors with 1 subtracted from them all

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(m)

