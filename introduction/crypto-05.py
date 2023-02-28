#!/usr/bin/env python3

# CyberChallenge.it - CTF
# Crypto 05 - Encoding 5

from sys import exit

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

def key(k):
    return bytes([k for x in range(0,25)])

ciphertext = 0x104e137f425954137f74107f525511457f5468134d7f146c4c # len 50
ciphertextb = ciphertext.to_bytes(25)

for i in range(0,256):
    output = xor(ciphertextb, key(i))
    print(i)
    print(output)

# key 32 is the correct one
plaintext = xor(ciphertextb, key(32))

print("flag{%s}" %(plaintext.decode()))