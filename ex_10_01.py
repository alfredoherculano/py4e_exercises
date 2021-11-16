fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Error, invalid file.')
	quit()

d = dict()
for line in fhand:
	if 'From ' not in line: continue
	words = line.split()
	for word in words:
		d[words[1]] = d.get(words[1], 0) + 1

lst = list()
for email,count in d.items():
	lst.append((count,email))

lst = sorted(lst, reverse=True)

print(lst[0][1], lst[0][0])