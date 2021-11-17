try:
	re_name = input('Enter regular expression: ')
except:
	print('Invalid regex.')
	quit()

fname = open('mbox.txt')

import re
count = 0
for line in fname:
	line = line.strip()
	i = re.findall(re_name, line)
	if len(i) > 0:
		count += 1

print('mbox.txt had', count, 'lines that matched', re_name)