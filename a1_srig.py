import sys
import os

with open(sys.argv[1], 'r') as file:
	dataset = [x.strip('\n') for x in file]

samples = {}
for k in dataset:
	if k not in samples.keys():
		samples[k] = 1
	else:
		samples[k] = samples[k] + 1

hexdata = [int(x, 16) for x in samples.keys()]

sortIndex = [i[0] for i in sorted(enumerate(hexdata), key=lambda x:x[1])]

uniqueValues = [x for x in samples.keys()]

for i in sortIndex:
	if samples[uniqueValues[i]] > 1:
		print(uniqueValues[i].lstrip('0'), samples[uniqueValues[i]])	


