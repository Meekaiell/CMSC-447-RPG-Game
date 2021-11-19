# This file listens for a request and then forks the process
from socket import *
import os
from threading import Thread
from socketserver import ThreadingMixIn


class ConnectionThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = connectionsocket.recv(2048).decode()
            print("Server received data:", data)
            #  message = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            message = data.upper()
            if message == 'exit':
                break
            connectionsocket.send(message.encode())  # echo


# Multithreaded Python server : TCP Server Socket Program Stub
serverport = 4770
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('', serverport))
serversocket.listen(4)
threads = []
print("The server is ready to receive")
print("Multithreaded Python server : Waiting for connections from TCP clients...")
while True:
    (connectionsocket, (addr, serverport)) = serversocket.accept()
    newthread = ConnectionThread(addr, serverport)
    newthread.start()
    threads.append(newthread)
    sentence = connectionsocket.recv(1024).decode()
    connectionsocket.close()

for t in threads:
    t.join()
