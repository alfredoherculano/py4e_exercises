def computepay(ini_hours, ini_rate): #calculate pay
	
	if ini_hours <= 40:
		return ini_hours * ini_rate

	overwork = ini_hours - 40
	return (ini_hours * ini_rate) + (overwork * 1.5 * ini_rate)

def check_input(inp): #check for correct input

	try:
		value = float(inp)
		return value
	except:
		print('Error, please provide a numerical value.')
		quit()

input_hours = input('Enter hours: ') #assign variable to ask for input
hours = check_input(input_hours) #check if correct variable was provided

input_rate = input('Enter rate: ')
rate = check_input(input_rate)

pay = computepay(hours, rate) #assign variable to final pay value
print('Pay: ', pay)