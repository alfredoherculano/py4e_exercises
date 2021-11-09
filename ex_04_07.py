def computegrade(ini_score):
	
	if 0 <= ini_score <= 1:
		if ini_score >= 0.9:
			return 'A'
		elif ini_score >= 0.8:
			return 'B'
		elif ini_score >= 0.7:
			return 'C'
		elif ini_score >= 0.6:
			return 'D'
		else:
			return 'F'

	return 'Non-applicable score.'

input_score = input('Enter score: ')
score = 0.0

try:
	score = float(input_score)
except:
	print('Non-applicable score. Please provide a number between 0.0 and 1.0')
	quit()

print(computegrade(score))