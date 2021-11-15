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
	email = words[1].split('@')
	for domain in email:
		d[email[1]] = d.get(email[1], 0) + 1

print(d)