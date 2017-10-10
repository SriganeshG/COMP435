import os, sys, hashlib

str = 'The quick brown fox jumps over the lazy dog'
hash = hashlib.sha256(str.encode('ascii')).hexdigest()
print(hash)
