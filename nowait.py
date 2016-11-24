# !/usr/bin/env python
# UDP Xinetd server  -  nowait.py
# Date : 2016.11.20

import socket, time, sys
# Setup a new socket object by socket.fromfd()
s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_DGRAM)
message, address = s.recvfrom(8192)
s.connect(address)
for i in range(10):
	s.send("Reply %d: %s" % (i + 1, message))
	time.sleep(2)
	s.send("OK, I'm done sending replies.\n")




# Xinetd service
"""
service test
{
	flags = NAMEINARGS
	type = UNLISTEN
	port = 51423
	socket_type = dgram
	protocol = udp
	wait = no                       # nowait
	user = root
	server = /home/zyh/test.py
	server_args = /home/zyh/test.py
}
"""