# !/usr/bin/env python
# Server about deadlock

# Just a instance
"""
import socket, traceback
host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
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
		print "Got connection from: ",clientsock.getpeername()
		while 1:
			data = clientsock.recv(4096)
			if not len(data):
				break
			clientsock.sendall(data)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()

	# Close the connection
	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()

"""





import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
	try:
		clientsock, clientaddr = s.accept()
	except KeyboardInterrupt:
		raise
	except:
		trace.print_exc()
		continue

	try:
		print "The client: ", clientaddr
		while 1:
			
			data = clientsock.recv(4096)
			if not len(data):
				break
			clientsock.sendall(data)
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()



