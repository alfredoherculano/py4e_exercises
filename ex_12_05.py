#Review this code in the future to see if I have a better understanding of it.

import socket

try:
    url = input('Enter url: ')
    host = url.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(url).encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        data = data.decode()
        pos  = data.find('\r\n\r\n') #find the position of the two blank lines after the header
        print(data[pos+4:], end='') #print from pos + 4 to exclude the two blank lines

    mysock.close()

except:
    print('Invalid adress.')
    quit()
