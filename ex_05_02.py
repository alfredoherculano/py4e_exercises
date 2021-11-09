#Why to I have to write part of the code outside the while loop? Is it possible to achieve the same results with just the loop?

ini_num = input('Enter a number: ')
	
if ini_num == 'done':
	quit()

try:
	inum = int(ini_num)

except:
	print('Bad data. Invalid input.')
	quit()
	
max_num = inum
min_num = inum

while True:
	ini_num = input('Enter a number: ')
	
	if ini_num == 'done':
		break

	try:
		inum = int(ini_num)
	
	except:
		print('Bad data. Invalid input.')
		continue
	
	if inum > max_num:
		max_num = inum

	if inum < min_num:
		min_num = inum

	
		
print(max_num, min_num)
