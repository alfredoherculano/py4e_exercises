fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Error, invalid file.')
	quit()

d = dict()
for line in fhand:
	words = line.split()
	if len(words) < 5 or words[0] != 'From': continue
	hours = words[5].split(':')
	for hour in hours:
		d[hours[0]] = d.get(hours[0], 0) + 1

lst = list()
for hour,count in d.items():
	lst.append((hour,count))

lst.sort()

for hour,count in lst:
	print(hour,count)