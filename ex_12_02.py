import socket

try:
    url = input('Enter url: ')
    urlparts = url.split('/')
    host = urlparts[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET {0} HTTP/1.0\r\n\r\n'.format(url).encode()
    mysock.send(cmd)


    text = b''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        text += data


    text = text.decode()

    print(text[:3000])
    print(len(text))

    mysock.close()

except:
    print('Invalid adress.')
    quit()