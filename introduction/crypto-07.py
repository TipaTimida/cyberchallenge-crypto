#!/usr/bin/env python3

# CyberChallenge.it - CTF
# Crypto 07 - Encoding 7

import binascii
from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# DES
key = 0x69743d18cbda9fcb
cipher = DES.new(key.to_bytes(8), DES.MODE_CBC)
plaintext = 'La lunghezza di questa frase non è divisibile per 8'
plaintextb = plaintext.encode()
msg = cipher.encrypt(pad(plaintextb, DES.block_size, 'x923'))
print(binascii.hexlify(cipher.iv))
print(binascii.hexlify(msg))

# AES
key = get_random_bytes(32)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=24)
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
plaintextb = plaintext.encode()
msg = cipher.encrypt(pad(plaintextb, AES.block_size, 'pkcs7'))
print(binascii.hexlify(key))
print(binascii.hexlify(iv))
print(binascii.hexlify(msg))

# ChaCha20
nonce= 0x36065a6ac2cdd6d9
key = 0x29846cd5cfcf19de8f1c3bc675cb5721c4408b187fcd648dd8bc7d7d1a9e47b9
ciphertext = 0x65c60aaad4480414e4146a0e915fc4d61d70dda5815a5a2b7eeef47d
ciphertextb = ciphertext.to_bytes(28)
cipher = ChaCha20.new(key=key.to_bytes(32), nonce=nonce.to_bytes(8))
plaintext = cipher.decrypt(ciphertextb)
print(plaintext.decode('ascii'))