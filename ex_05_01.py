#Find out a way to write the same code using len() and max()

count = 0
total = 0

while True:
	ini_num = input('Enter a number: ')
	try:
		if ini_num == 'done':
			break
		count = count + 1
		total = total + int(ini_num)
	except:
		print('Bad data. Invalid input.')
		continue
		
print(total, count, total/count)
