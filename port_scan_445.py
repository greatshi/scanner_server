#!/usr/bin/env python

import sys
import socket
from threading import Thread
import resource

resource.setrlimit(resource.RLIMIT_NOFILE, (1024, 1024))

def scan(ip_whole, port, f):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sk.settimeout(0.2)
    if sk.connect_ex((ip_whole, port)) == 0:
        print ip_whole
        f.write(ip_whole+"\n")
    sk.close()

def main():
    ip = sys.argv[1]
    ip = str(ip)
    port = 445
    print "scaning port 445..."
    f = open(ip+".0.0.txt", "w+")
    for j in range(1,255):
        for i in range(1,255):
            ip_whole = ip+"."+str(j)+"."+str(i)
            t = Thread(target = scan, args = (ip_whole, port, f))
            t.start()
    f.close()
    print "ok!"

if __name__ == '__main__':
    main()
