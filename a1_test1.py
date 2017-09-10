import sys
import collections
with open(sys.argv[1], 'r') as data:
	dataset = data.readlines()
dataset = [x.strip('\n') for x in dataset]

dataset = [int(x,16) for x in dataset]

dataset.sort()

dataset = [hex(x) for x in dataset]

duplicates = collections.Counter(dataset)

print(duplicates)
for key, value in duplicates.items():
	if value > 1:
		print(key, value)
