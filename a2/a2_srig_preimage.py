import os, sys, hashlib, random, string, time

hash1 = sys.argv[1]
hash24 = hash1[0:6]
hashRnd = ''
count = 0
s = string.ascii_lowercase + string.digits

rand_str = lambda n: ''.join([random.choice(s) for i in range(n)])

while(hash24 != hashRnd):
	randomStr = rand_str(7)
	count=count+1
	hashRnd = hashlib.sha256(randomStr.encode('ascii')).hexdigest()
	hashRnd = hashRnd[0:6]

print(randomStr + " " + str(count))


