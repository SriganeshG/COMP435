import os, sys, hashlib, random, string

hash1 = sys.argv[1]
hash1 = hash1[0:6]
hash2 = ' '
count = 0
randomStr = ''.join(random.choice(string.digits) for i in range(6))

while(hash1 != hash2):
	randomStr = randomStr + ''.join(random.choice(string.ascii_lowercase) for i in range(1+(count//750000)))
	count=count+1
	hash2 = hashlib.sha256(randomStr.encode('ascii')).hexdigest()
	hash2 = hash2[0:6]

print(randomStr + " " + count)
#ayy found unn10357ls
#onov3n
#yb3dufg4i4bod
#sometimes really fast sometimes slow. normal?
