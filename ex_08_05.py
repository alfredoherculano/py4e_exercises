fname = input('Enter file:')

try:
	fhand = open(fname)
except:
	print('Error, no such file in directory.')
	quit()

word_list = list()
for line in fhand:
	if 'From ' not in line: continue
	words = line.split()
	word_list.append(words)
	for word in words:
		print(words[1])

line_number = len(word_list)
print('There were', line_number, 'lines in the file with From as the first word.')
