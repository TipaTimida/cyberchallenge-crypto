#!/usr/bin/env python3

# Cifrario di Cesare
def cesare(msg):
    critto = ""
    for x in msg.upper():
        if ord(x) > 64 and ord(x) < 91:
            # es. x="A" 
            critto += chr((ord(x)-65 +3) % 26 + 65)
    return critto

testo = "LA CRITTOGRAFIA E' BELLA"

print(cesare(testo))

