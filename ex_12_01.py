import socket

url = input('Enter url: ')

try:
    urlparts = url.split('/')
    host = urlparts[2]
except:
    print('Invalid adress.')
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
