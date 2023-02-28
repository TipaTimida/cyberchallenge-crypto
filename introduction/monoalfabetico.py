#!/usr/bin/env python3

# Cifrario monoalfabetico

def mono(msg, alfabeto):
    critto = ""
    for x in msg.upper():
        if ord(x) > 64 and ord(x) < 91:
            critto += alfabeto[ord(x)-65]
    return critto

# ABCDEFGHIJKLMNOPQRSTUVWXYZ

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1]
print(mono("QUESTO MESSAGGIO CONTIENE UN SEGRETO IMPENETRABILE", alfabeto))

