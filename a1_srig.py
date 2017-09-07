import sys
with open(sys.argv[1], 'r') as data:
	dataset = data.readlines()
dataset = [x.strip('\n') for x in dataset]

for items in dataset:
	print(items)
