#!/usr/bin/env python3

# Cifrario polialfabetico di Vigenere

def vigenere(msg, key):
    critto = ""
    i = 0
    for x in msg.upper():
        if ord(x) > 64 and ord(x) < 91:
            critto += chr((ord(x)-65 + ord(key[i%len(key)])-65) % 26 + 65)
            i+=1
    return critto

key = "KEY"
print(vigenere("MESSAGGIO", key))

