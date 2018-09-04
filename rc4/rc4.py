#! /usr/bin/python

#rc4 impl
import sys

def swap(ary,i,j):
	temp = ary[i]
	ary[i] = ary[j]
	ary[j] = temp

def main():
	if (len(sys.argv) != 4):
		print sys.argv
		print('Usage: rc4 key plaintextFile ciphertextFile')
		return
	key = sys.argv[1]
	keyLen = len(key)
	inputFile = open(sys.argv[2],'rb')
	outputFile = open(sys.argv[3],'wb')
	plaintext = inputFile.read()
	plaintextLength = len(plaintext)
	ciphertext = bytearray(plaintextLength)

	#Init
	S = bytearray(256)
	K = bytearray(256)

	for i in range(0,255):
		S[i] = i
		K[i] = ord(key[i % keyLen])

	j=0
	for i in range(0,255):
		j = (j + S[i] + K[i]) % 256
		swap(S, S[i], S[j])

	i=j=0

	#generate keystream and result
	for curr in range(0,plaintextLength):
		i = (i+1) % 256
		j = (j + S[i]) % 256
		swap(S, S[i], S[j])
		t = (S[i] + S[j]) % 256
		keystreamByte = S[t]
		print ord(plaintext[curr]),  keystreamByte, ord(plaintext[curr]) ^ keystreamByte
		ciphertext[curr] = 	ord(plaintext[curr]) ^ keystreamByte;

	outputFile.write(ciphertext) 
	print(str(plaintextLength)+' bytes written to '+sys.argv[3])


if __name__ == "__main__":
	main()
