import os
#import base64
import zcrypto
from zcrypto import numpy as np
import matplotlib.pyplot as mpl
#from Crypto.Cipher import AES
#unpad = lambda s: s[:-ord(s[len(s) - 1:])]

fileName = '8.txt'
fileOutName = '8out.txt'
cwd = os.getcwd()

############
#read in AES encrypted data
with open(cwd + '\\' +fileName, 'r') as cipher_data:
    cipherText = cipher_data.read().split()
    
for line in range(len(cipherText)):
#for line in range(10):
    hd = []
    for kgLen in range(2,int(len(cipherText[line])/2)):
        #   print('At key length '+ str(kgLen) + ' the hamm dist is: '+ str(hd[kgLen-1]))
        chunkList = []
        for chunk in range(1,int(len(cipherText[line])/kgLen)-1):
            a = bytearray(cipherText[line][chunk*kgLen:(chunk+1)*kgLen], encoding = "utf-8")
            b = bytearray(cipherText[line][(chunk+1)*kgLen:(chunk+2)*kgLen], encoding = "utf-8")
            chunkList.append(zcrypto.hammingDistBin(a, b))
        avg = np.mean(chunkList)
        hd.append(avg/kgLen)
    
    mpl.figure(line)
    hdArray =  np.array(hd)
    keyLen = np.arange(1,int(len(cipherText[line])/2)-1)
    mpl.plot(keyLen, hdArray)