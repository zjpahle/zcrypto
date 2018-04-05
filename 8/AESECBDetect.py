# -*- coding: utf-8 -*-

import os
import base64
#import numpy
from Crypto.Cipher import AES
#unpad = lambda s: s[:-ord(s[len(s) - 1:])]

fileName = '8.txt'
cwd = os.getcwd()

with open(cwd + '\\' +fileName, 'r') as cipher_data:
    cipher_text = base64.b64decode(cipher_data.read())
#print(type(cipher_text))
#print(cipher_text)
    
decryption_suite = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
plain_text = decryption_suite.decrypt(cipher_text)


with open(cwd + '\\7_out.txt', 'wb') as out_text:
    out_text.write(plain_text)
    
def hammingDistBin(a, b):
    xord = xorThisShit(a,b)
    return sum((xord[x] >> y) & 1 for y in range(8) for x in range(len(xord)))

def xorThisShit(key, message):
    if (type(key) != bytearray):
        raise TypeError('key must be bytearray type')
    if (type(message) != bytearray):
        raise TypeError('message must be bytearray type')
    if len(key) != len(message):
        raise TypeError('key must have the same length as message')
    return bytearray(message[x] ^ key[x] for x in range(len(key)))