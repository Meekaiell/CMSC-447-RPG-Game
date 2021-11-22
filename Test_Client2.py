from Sockets import ClientSocket, USER, socket, pickle, time

HOST = socket.gethostname()
PORT = 4770

# Creating client socket instance
CLNT = ClientSocket(HOST, PORT)

user_1 = USER('Poppy')
CLNT.send("hey")

# Test Client drop function
CLNT.drop()
