fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Error, invalid file.')
	quit()

d = dict()
for line in fhand:
	import string #import string module
	line = line.translate(str.maketrans('', '', string.punctuation)) #remove all punctiation
	line = ''.join(char for char in line if char.isalpha()) #use join() to make new strings with just the alphabetic characters
	line = line.lower() #set all characters to lowercase
	
	for letter in line:
		d[letter] = d.get(letter, 0) + 1

lst = list()
for letter,count in d.items():
	lst.append((count,letter))

lst.sort(reverse=True)

for count,letter in lst:
	print(letter,count)
