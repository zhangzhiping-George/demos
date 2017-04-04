import socket
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8080))
print(clientsock.recv(1024).decode('utf-8'))
for data in [b'clidata1', b'clidata2', b'clidata3']:
	clientsock.send(data)
	print(clientsock.recv(1024).decode('utf-8'))
clientsock.send(b'exit')
clientsock.close()
