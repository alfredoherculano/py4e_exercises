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
		d[words[2]] = d.get(words[2], 0) + 1

print(d)