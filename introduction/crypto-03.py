#!/usr/bin/env python3

# CyberChallenge.it - CTF
# Crypto 03 - Encoding 3

from base64 import b64decode
import math

first = b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=")
num = 664813035583918006462745898431981286737635929725

# ceil = round a number upward to its neareast integer (eg. math.ceil(1.4) == 2)
last = num.to_bytes(math.ceil(num.bit_length() / 8), 'big')

print(first + last)

