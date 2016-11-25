# !/usr/bin/env python
# Date : 2016.11.25

# Function socket.getaddrinfo(host, port, family, socktype, protocol, flags)

# DNS query
"""
import socket, sys

result = socket.getaddrinfo(sys.argv[1], None, 0, socket.SOCK_STREAM)
count = 0
for i in result:
	print "%-2d: %s" % (count, i[4])
	count += 1
"""

# RDNS query
"""
import socket, sys
try:
	result = socket.gethostbyaddr(sys.argv[1])
	print "Primary hostname: "
	print " " + result[0]

	print "\nAddress:"
	for item in result[2]:
		print " " + item

except socket.herror, e:
	print "Couldn't look up name: ", e

"""

# Basic_dns_rdns query

import sys, socket
# DNS query function
def getipaddrs(hostname):
	
	#Get a list of ip addresses from a given hostname.This is a standard(froward) lookup.
	
	result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
	return [x[4][0] for x in result]

def gethostname(ipaddr):
	
	#Get the hostname from a given  IP address. This is a reverse lookup.
	
	return socket.gethostbyaddr(ipaddr)[0]

try:
	# First, do the reserve lookup and get the hostname
	hostname = gethostname(sys.argv[1])   # could raise socket.herror

	# Now ,do a forward lookup on the result from the earlier reserve
	# lookup
	ipaddrs = getipaddrs(hostname)         # could raise socket.gaierror
except socket.herror, e:
	print "No host names available for %s; this may be normal." % sys.argv[1]
	sys.exit(0)
except socket.gaierror, e:
	print "Got hostname %s, but it could not be forward-resolved: %s" % (hostname, str(e))
	sys.exit(1)
# If the forward lookup did not yeild the original IP address anywhere,
# someone is playing tricks. Explain the  situation and exit.

if not sys.argv[1] in ipaddrs:
	print "Got hostname %s, but on forward lookup," % hostname 
	print "original IP %s did not appear in IP address list." % sys.argv[1]
	sys.exit(1)

# Otherwise, show the vaildated hostname.
print "Vaildated hostname: ",hostname


# gethostname() and getfqdn()

import sys, socket

def getipaddrs(hostname):
	result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
	return [x[4][0] for x in result]

hostname = socket.gethostname()
print "Host name: ",hostname

print "Fully-aualified name: ", socket.getfqdn(hostname)

try:
	print "Ip address: ",", ".join(getipaddrs(hostname))
except socket.herror, e:
	print "Couldn't not get Ip address: ",e

"""
import sys, DNS
query = sys.argv[1]
DNS.DiscoverNameServers()

reqobj = DNS.Request()
answerobj = reqobj.req(name = query, qtype = DNS.Type.ANY)
if not len(answerobj.answers):
	print "Not found."
for item in answerobj.answers:
	print "%-5s %s" % (item['typename'], item['data'])
"""