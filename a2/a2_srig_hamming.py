import sys
import os

#for x in sys.argv[1:]:
	

string1 = sys.argv[1]
string2 = sys.argv[2]
bin1 = bin(int(string1,16))
bin2 = bin(int(string2,16))

hammingDist = sum(x != y for x,y in zip(bin1,bin2)) 

print(hammingDist)
	
