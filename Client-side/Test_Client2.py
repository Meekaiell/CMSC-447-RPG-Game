from Sockets import Client_SKT, USER, socket

HOST = socket.gethostname()
PORT = 4770

# Creating client socket instance
CLNT = Client_SKT(HOST,PORT)

user_1 = USER('Poppy')

# Test client send function
CLNT.send(user_1)

# Test Client drop function
CLNT.drop()