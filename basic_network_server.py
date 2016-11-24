#!/usr/bin/env python
# Simple server.py 
# Author:kenzhaoyihui
# Date: 2016.11.22
"""
import socket
host = ""
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.Setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

print "Server is running on port %d; press Ctrl-C to terminate." % port

while 1:
	clientsock, clientaddr = s.accept()
	clientfile = clientsock.makefile('rw', 0)
	clientfile.write('welcome ' + str(clientaddr) + "\n")
	clientfile.write("Please enter a string: ")
	line = clientfile.readline().strip()
	clientfile.write("You enter %d charactors.\n" % len(line))
	clientfile.close()
	clientsock.close()
"""
"""
import socket

print "Creating socket... "
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done"

print "Looking up port number..."
port = socket.getservbyname('http')
print "done"

print "Connnecting to remote host... "
s.connect(("www.google.com", port))
print "done"

print "Connected from :", s.getsockname()
print "Connected to : ", s.getpeername()
"""

"""
import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
	port = int(textport)
except ValueError:
	# That didn't work.Look it up instead.
	port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
print "Enter data to transmit: "
data = sys.stdin.readline().strip()
s.sendall(data)
print "Looking for replies; Press Ctrl-C or Ctrl-break to stop"

while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)
"""

"""
import socket, sys, struct, time

hostname = 'time.nist.gov'
port = 37

host = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('',(host, port))

print "Looking for replies;press Ctrl-C to stop"
buf = s.recvfrom(2048)[0]
if len(buf) != 4:
	print "Wrong-sized reply %d: %s" % (len(buf), buf)
	sys.exit(1)

secs = struct.unpack("!I", buf)[0]
secs -= 2208988800
print time.ctime(int(secs))

"""

import socket


host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
print "Waiting for connnections!"
s.listen(1)

while 1:
	try:
		clientsock, clientaddr = s.accept()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	# Process the connection

	try:
		print "Got connection from :", clientsock.getpeername()
		# Process the request here
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()

	# Close the connnection

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		