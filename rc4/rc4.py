#! /usr/bin/python

#rc4 impl
import sys

def swap(ary,i,j):
	temp = ary[i]
	ary[i] = ary[j]
	ary[j] = temp

def dumpSInfo(S,i,j):
	#print out S 
	for x in range(0,16):
		for y in range(0,16):
			sVal = S[x*16+y]
			print str(sVal) + " "*(3-len(str(sVal))),
			if (y==15):
				print "" 
	print ""
	print "i="+str(i)+", j="+str(j)+'\n\n'


def init(S, K, key):
	for i in range(0,255):
		S[i] = i
		K[i] = ord(key[i % len(key)])

	j=0
	for i in range(0,255):
		j = (j + S[i] + K[i]) % 256
		swap(S, S[i], S[j])
	print "S Info after init: \n",
	dumpSInfo(S, i, j)


def crypt(S, K, dataIn, dataOut):
	i=j=0
	#generate keystream and result
	for curr in range(0,len(dataIn)):
		i = (i+1) % 256
		j = (j + S[i]) % 256
		swap(S, S[i], S[j])
		t = (S[i] + S[j]) % 256
		keystreamByte = S[t]
		dataOut[curr] = ord(dataIn[curr]) ^ keystreamByte;
		if (curr==100):
			print "S Info after 100 bytes: \n",
			dumpSInfo(S, i, j)
		if (curr==1000):
			print "S Info after 1000 bytes: \n",
			dumpSInfo(S, i, j)

def main():
	if (len(sys.argv) != 4):
		print sys.argv
		print('Usage: rc4 keyfile inFile outFile')
		return
	keyFile = open(sys.argv[1],'rb')
	key = keyFile.read()
	keyLen = len(key)
	inputFile = open(sys.argv[2],'rb')
	outputFile = open(sys.argv[3],'wb')
	dataIn = inputFile.read()
	dataInLength = len(dataIn)
	dataOut = bytearray(dataInLength)

	#Init
	S = bytearray(256)
	K = bytearray(256)

	init(S, K, key)

	#Crypt it
	crypt(S, K, dataIn, dataOut)

	outputFile.write(dataOut) 
	print(str(dataInLength)+' bytes written to '+sys.argv[3])


if __name__ == "__main__":
	main()
