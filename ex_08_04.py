fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Error, file does not exist')
	quit()

word_list = list()
for line in fhand:
	words = line.split()
	#print(words)
	for word in words:
		if word in word_list: continue
		word_list.append(word)

word_list = sorted(word_list)
print(word_list)