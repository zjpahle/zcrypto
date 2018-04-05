# -*- coding: utf-8 -*-

import os
import base64
from Crypto.Cipher import AES
#unpad = lambda s: s[:-ord(s[len(s) - 1:])]

fileName = '7.txt'
cwd = os.getcwd()

with open(cwd + '\\' +fileName, 'r') as cipher_data:
    cipher_text = base64.b64decode(cipher_data.read())
#print(type(cipher_text))
#print(cipher_text)
    
decryption_suite = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
plain_text = decryption_suite.decrypt(cipher_text)


with open(cwd + '\\7_out.txt', 'wb') as out_text:
    out_text.write(plain_text)