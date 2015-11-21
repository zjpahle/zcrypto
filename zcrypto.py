import numpy

def hammingDistBin(a, b):
	xord = xorThisShit(a,b)
	return sum((xord[x] >> y) & 1 for y in xrange(8) for x in xrange(len(xord)))

def genFreqTruth(text):
	truth = [0]*256
	for count in xrange(len(text)):
		truth[ord(text[count])] += 1
	truth = [float(truth[x])/float(max(truth)) for x in xrange(len(truth))]
	return truth

def checkTruth (truth, mess):
	mess = str(mess)
	freqList = [0.0 for i in xrange(256)]
	for count in xrange(len(mess)):
		freqList[ord(mess[count])] += 1
	letterCorr =float(numpy.correlate(truth,freqList))
	return round(letterCorr,2)

def singleChrXor (key, message):
	if (type(key) != bytearray):
		raise TypeError('key must be bytearray type')
	if (type(message) != bytearray):
		raise TypeError('message must be bytearray type')
	if (len(key) > 1):
		raise TypeError('key must have a length of 1')
	return bytearray(key[0] ^ message[x] for x in xrange(len(message)))

def getKey(item):
	return item[0]

def repeatingKeyXor (key, message):
	keyFull = (key*len(message))[:len(message)]
	return xorThisShit(keyFull, message)

def xorThisShit(key, message):
	if (type(key) != bytearray):
		raise TypeError('key must be bytearray type')
	if (type(message) != bytearray):
		raise TypeError('message must be bytearray type')
	if len(key) != len(message):
		raise TypeError('key must have the same length as message')
	return bytearray(message[x] ^ key[x] for x in xrange(len(key)))

#Challenge 3
# fileIn = open('SherlockFull.txt', 'r')
# plainText = fileIn.read()
# truth = genFreqTruth(plainText)

# cipherTxt = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')
# cipherTxt = 'k6bIi6jDmZ2VuaOZvZ+zsKvDwJmQpoaEqMPIhQ=='.decode('base64')
# guesses = []
# for keyCount in range(0,256):
# 	thisGuess = str(singleChrXor(bytearray(chr(keyCount)), bytearray(cipherTxt)))
# 	guesses.append([checkTruth(truth, thisGuess), chr(keyCount), thisGuess])
# 	guesses = sorted(guesses, key=getKey, reverse=True)
# for x in range(0,len(guesses)):
# 	print str(guesses[x]) + '\n'

#Challenge 5
# cipherTxt = bytearray('Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal')
# print str(repeatingKeyXor(bytearray('ICE'), cipherTxt)).encode('hex')

# a = bytearray('this is a test')
# b = bytearray('wokka wokka!!!')
# print hammingDistBin(a, b)

