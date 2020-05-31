#!/usr/bin/python3

from pwn import *
import re

s = remote("chals20.cybercastors.com", 14429)

s.recv()
s.sendline('\n'.encode())

question = s.recv().decode()
print(question)

first = re.findall('What is {}', question)
operator = re.findall('What is ' + question + ' {}', question)
second = re.findall('{} ?', question)

print(first)
print(operator)
print(second)