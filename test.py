#!/usr/bin/python
import subprocess
import time
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

p = subprocess.Popen(["python","http.py"],stdout=subprocess.PIPE)
print "checking socket"
result = sock.connect_ex(('localhost',8181))
print result
if ( str(result) == "0"):
 print "Open"
p.kill()

