# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:09:29 2018

@author: pahlza
"""

statearray = [[0 for x in range(4)] for x in range(4)]

print(statearray)
print(statearray[0])
print(statearray[2][3])
block = range(128)

#for i in range(4):
#    for j in range(4):
#            statearray[j][i] = block[32*i + 8*j:32*i + 8*(j+1)]
#            
#for i in range(4):
#    for j in range(4):
#            print (statearray[i][j], "   ")