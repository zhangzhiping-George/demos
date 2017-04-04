import socket, time, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' %addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Server received data from %s as: %s' %(addr, data.decode('utf-8'))).encode('utf-8'))
	sock.close()
	print('sock closed...')

print('Listenning connection from any client...')
while True:
	sock, addr = server.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()

