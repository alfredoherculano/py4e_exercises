import urllib.request, urllib.parse, urllib.error

try:
	url = input('Enter url: ')
	fhand = urllib.request.urlopen(url)

	data = ''
	for line in fhand:
		line = line.decode()
		data += line
		
	print(data[:3000])
	print(len(data))

except:
	print('Invalid adress.')
	quit()
