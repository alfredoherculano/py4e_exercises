file = input('Enter file: ')
fhand = open(file)

i = dict()
val = 0
for line in fhand:
	words = line.split()
	for word in words:
		val += 1
		if word in i:		#skips to the next key if the current one is already in the dictionary
			continue
		else:
			i[word] = val	#set the current value to the current word

print('skills' in i)