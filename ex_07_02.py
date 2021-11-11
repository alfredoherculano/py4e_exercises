fname = input('Enter file: ')

try:
	fhand = open(fname)
except:
	print('Invalid input. Please provide a suitable file.')
	quit()

counter = 0
y = 0.0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		counter += 1
		fval_pos = line.find(' ')
		fval = line[fval_pos+1:].strip()
		y = y + float(fval)

average = y/counter

print('Average spam confidence:', average)