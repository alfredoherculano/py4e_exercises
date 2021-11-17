fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Error, invalid file.')
	quit()

import re
lst = list()
for line in fhand:
	line = line.rstrip()
	form = re.findall('^New .*: ([\d.]*)', line)
	if form != []:
		lst.append(int(form[0]))

added = sum(lst)
count = len(lst)
average = added/count

print(int(average))