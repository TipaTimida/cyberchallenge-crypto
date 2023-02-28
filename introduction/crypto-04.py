#!/usr/bin/env python3

# CyberChallenge.it - CTF
# Crypto 04 - Encoding 4

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1 = 0x158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf
m2 = 0x73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2

m1b = m1.to_bytes(22)
m2b = m2.to_bytes(22)

msg = xor(m1b, m2b)
print(msg)