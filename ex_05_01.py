count = 0
total = 0

while True:
	ini_num = input('Enter a number: ')
	try:
		if ini_num == 'done':
			break
		count = int(ini_num) + 1
		total = total + int(ini_num)
	except:
		print('Bad data. Invalid input.')
		
print(total, count, total/count)
