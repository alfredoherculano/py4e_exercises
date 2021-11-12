num_list = list()
while True:
	user_input = input('Enter a number: ')
	if user_input == 'done': break

	try:
		float_input = float(user_input)

	except:
		print('Invalid input, please enter a numerical value.')
		quit()

	num_list.append(float_input)

print('Maximum: ', max(num_list))
print('Minimum ', min(num_list))