from Sockets import ClientSocket, USER, socket, pickle, time

HOST = socket.gethostname()
PORT = 4770

# Creating client socket instance
CLNT = ClientSocket(HOST, PORT)

# Test client recv function
CLNT.recv()
print(CLNT.data)

# Test Client drop function
CLNT.drop()
