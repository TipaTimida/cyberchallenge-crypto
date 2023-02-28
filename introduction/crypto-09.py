#!/usr/bin/env python3

# CyberChallenge.it - CTF
# Crypto 09 - Inverso modulare
from cryptomath import inverse, bezout

# risolve l'identità di Bezout
print(bezout(139,102))

# calcola l'inverso di a modulo n
# utilizzando l'algoritmo esteso di Euclide
# inverse(a,n)
print(inverse(36,91))
