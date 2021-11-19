from Sockets import Server_SKT, Client_SKT, USER, socket, pickle, time

HOST = socket.gethostname()
PORT = 4770

# Creating client socket instance
CLNT = Client_SKT(HOST,PORT)

# Test client recv function
CLNT.recv(4096)
CLNT.data.print()

# Test Client drop function
CLNT.drop()