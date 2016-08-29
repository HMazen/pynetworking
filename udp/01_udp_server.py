import socket

MAX_RECV_BYTES = 65535

host = '127.0.0.1'
port = 2020
addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

print "Listening on {}".format(sock.getsockname())

while True:
	data, addr = sock.recvfrom(MAX_RECV_BYTES)
	text = data.decode('ascii')
	print "Client at {} says: {}".format(addr, text)
	text = "Your message was {} bytes long".format(len(text))
	sock.sendto(text.encode('ascii'), addr)