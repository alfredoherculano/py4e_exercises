fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Error, file not found.')
	quit()

d = dict()

for line in fhand:
	if 'From ' not in line: continue
	words = line.split()
	for word in words:
		d[words[1]] = d.get(words[1], 0) + 1

maxcount = 0
maxkey = None

for key,value in d.items():
	if maxcount == 0 or value > maxcount:
		maxcount = value
		maxkey = key

print(maxkey, maxcount)