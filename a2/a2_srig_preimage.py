import os
import sys
import hashlib
import random
import binascii
import string

hash1 = sys.argv[1]
hash2 = ' '
random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(1)])

while(hash1 != hash2):
	hash2 = hashlib.sha256(random).hexdigest()	
	#'{:.24}'.format(hash2)
	hash2 = hash2[:24]
	random + str(randint(0,9))

print(hash2)

