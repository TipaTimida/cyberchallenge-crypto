#!/usr/bin/env python3

# CyberChallenge.it - CTF
# Crypto 10 - CRT
from cryptomath import cinese

# risolve il sistema di congruenze x ≡ a[i] (mod n[i])
# utilizzando il teorema cinese del resto
# cinese(a,n) dove a e n sono delle liste  

print(cinese([32,6,34,37,59],[44,23,41,43,85]))
