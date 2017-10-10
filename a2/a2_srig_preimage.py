import os, sys, hashlib, random, string, binascii
from random import randint
hash1 = sys.argv[1]
hash1 = hash1[0:24]
randomStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(1))
hash2 = ' '
while(hash1 != hash2):
	
	hash2 = hashlib.md5(randomStr.encode('UTF-8')).hexdigest()
	hash2 = hash2[0:24]
	
	randomStr = randomStr + ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(1))

print(hash2)

