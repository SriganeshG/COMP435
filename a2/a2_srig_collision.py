import os, sys, hashlib, random, string

count = 0

hashes = dict()
while True:
	randomStr1 = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(7))
	hash1 = hashlib.sha256(randomStr1.encode('ascii')).hexdigest()
	hash1 = hash1[0:6]
	count = count + 1

	if(hash1 in hashes and randomStr1 != hashes[hash1]):
		print(randomStr1 +" "+hashes[hash1] + " "+str(count))
		break
	hashes[hash1] = randomStr1
