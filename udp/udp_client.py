import socket
from optparse import OptionParser

MAX_RECV_BYTES = 65535

parser = OptionParser()

parser.add_option('-H', '--host', action='store', dest='host', help='server address')
parser.add_option('-p', '--port', action='store', dest='port', help='server port')
options, _ = parser.parse_args()

host = options.host
port = int(options.port)
addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "message from client"
sock.sendto(data.encode('ascii'), addr)
data, addr = sock.recvfrom(MAX_RECV_BYTES)

print "{} reply: {}".format(addr, data)