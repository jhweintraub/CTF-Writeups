#!/usr/bin/python3

from pwn import *
import string

s = remote("chals20.cybercastors.com", 14422)

flag = "castorsCTF{k33p_y0ur_k3y5_53cr37_4nd_d0n7_r3u53_7h3m!"

s.send('ca'.encode())

found = s.recvline().decode()

while flag[len(flag)-1] != '}':
	for char in string.printable:
		toSend = flag + char
		s.send(toSend.encode())
		val = s.recvline().decode()		# print("Trying: {}\t Result: {}".format(toSend, val))
		# print("flag: {}\t resp: {}".format(toSend, val[0:4]))
		if val == found:
			print("FOUND: {}".format(flag))
			flag += char
			break

print(flag)


