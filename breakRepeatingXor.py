import zcrypto


#read in file
# fileIn=  open('6.txt', 'r')
# fileOut =  open('challenge6soln.txt', 'w')

fileTruth = open('SherlockFull.txt', 'r')
plainEnglish = fileTruth.read()
english = zcrypto.genFreqTruth(plainEnglish)
#print truth


# fileIn=  open('sherlockEncoded.txt', 'r')
# fileOut =  open('sherlock2.txt', 'w')

fileIn=  open('alarms.txt', 'r')
fileOut =  open('alarmsOut.txt', 'w')

#testFileOut =  open('stuff.txt', 'w')

cipherText = bytearray(fileIn.read().decode('base64'))
keysizeGuess = []

#take the hamming distance of the keysize guesses. Smallest dist is key length
for keysize in range(2,41):
	keysizeGuess.append(zcrypto.hammingDistBin(cipherText[0:keysize],cipherText[keysize:2*keysize])/keysize)
keysize = []
for x in range(5):
	#print keysizeGuess
	keysize.append(keysizeGuess.index(min(keysizeGuess)) + 2)
	keysizeGuess[keysize[x]-2] = 255
print 'The most likely keysizes are ' + str(keysize)
keysize = [22]

keyGuess = []
#for each possible key length:
for keyLenCnt in range(len(keysize)):
	#create dictionary for cipher blocks
	block = {x:[] for x in range(keysize[keyLenCnt])}

	#break ciphertext into blocks by individual key characters
	for x in range(len(block)):
		block[x] = cipherText[x::keysize[keyLenCnt]]

	plainTxtBlks = {x:[] for x in range(keysize[keyLenCnt])}

	#for each block:
	for blockCount in range(keysize[keyLenCnt]):
		guesses = [] #reset the guesses each time
		#for each single char key guess:
		for keyCount in range(256):
			thisGuess = zcrypto.singleChrXor(bytearray(chr(keyCount)),block[blockCount])
			guesses.append([zcrypto.checkTruth(english, thisGuess), chr(keyCount), str(thisGuess)]) #[rank, key, guessTxt]
			guesses = sorted(guesses, key=zcrypto.getKey, reverse=True)
		# for x in range(0,len(guesses)): #debugging for
		# 	testFileOut.write(str(guesses[x]) + '\n')
		plainTxtBlks[blockCount] = guesses[0] #best guess get placed in dict
	keyGuess.append(''.join([plainTxtBlks[blockCount][1] for blockCount in range(len(plainTxtBlks))]))
	#print keyGuess
	print 'the best guess key of length ' + str(keysize[keyLenCnt]) + ' is: ' + str(keyGuess[keyLenCnt])

#plainTxt = zcrypto.repeatingKeyXor(bytearray(keyGuess[0]), cipherText)
plainTxt = zcrypto.repeatingKeyXor(bytearray('alarms and discursions'), cipherText)
fileOut.write(str(plainTxt))
fileOut.close()
fileIn.close()