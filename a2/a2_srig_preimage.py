import os, sys, hashlib, random, string, binascii
from random import randint
hash1 = sys.argv[1]
hash1 = hash1[0:3]
randomStr = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(12))
hash2 = ' '
count = 0
while(hash1 != hash2):
	count=count+1
	hash2 = hashlib.sha256(randomStr.encode('ascii')).hexdigest()
	hash2 = hash2[0:3]
	
	randomStr = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(12))

print(randomStr)

