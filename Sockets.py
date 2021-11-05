import time, socket, pickle, json

# Server_SkT : The client socket class for communicating with the
# Client_SKT server class, using the socket library.
# The class contains 'host' & 'port' variables for client binding, along with
# 'clnt' & 'adr' variables to accept connection requests.
#
# Parameters:    host - The Ip address of the server program; default: localhost
#                port - Desired port to bind and transmit over; default: 80
#                listen - Number of allowed queued connections; default: 5
class Server_SKT:
    def __init__(self, host=socket.gethostname(), port=80, listen=5):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clnt = 0
        self.adr = 0
        self.hdr = 10
        self.listen = listen
        self.sock.bind((self.host,self.port))
        self.sock.listen(self.listen)

    # listen : This function allows the suer to adjust the server's 'listen'
    # variable in order to adjust the backlog connection allowed to connect.
    # This effectively allows multiple users to bind in turn and connect on
    # first-come-first-serve basis.
    #
    # Parameters:    listen - Number of allowed queued connections; default: 5
    def listen(self, listen=5):
        self.listen = listen
        self.sock.listen(self.listen)

    # send : This function transmits data to the directed bind executed
    # in the Server_SKT initialization. The pickle library is used to
    # serialize the transmitted data to bytes for transmission
    #
    # Parameters:    data_out - object desired to transmitted
    def send(self, data_out):
        self.clnt,self.adr = self.sock.accept()
        print(f"Connection to {self.adr} established")
        data = pickle.dumps(data_out)
        self.clnt.send(data)
        self.clnt.close()

    # recv : This function takes recieves data of a fixe byte size. The pickle
    # unserializes the transmitted data for use by the recieving program
    #
    # Parameters:    bytes - number of bytes to recieve per transmission
    #                hdr - a size value to be used in future implementation
    #                       to recieve a dynamic amount of data
    def recv(self,bytes = 4096, hdr = 10):
        self.data = b''
        self.data = self.sock.recv(bytes)
        self.data = pickle.loads(self.data)

    # drop : This function drops the connection established with the client
    # prgram adnd resets the relative class values to their default
    def drop(self):
        self.clnt.close()
        self.clnt = 0
        self.adr = 0

    # print : This function prints the data recieved and stored in the
    # server socket's data variable
    def print(self):
        print(self.data)

# Client_SKT : The client socket class for communicating with the
# Server_SkT server class.
# It attempts to connect to the socket pair passed in it's parameters
# Parameters:    host - The Ip address of the server program; default: localhost
#                port - Desired port to bind and transmit over; default: 80
class Client_SKT:
    def __init__(self, host=socket.gethostname(), port=80):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
        self.hdr = 0
        self.sock.connect((self.host,self.port))

    # connect : This function is a direct 'connect' function for retrying a
    # a connection to the server
    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
        except:
            return False

    # send : This function transmits data to the directed bind executed
    # in the Server_SKT initialization. The pickle library is used to
    # serialize the transmitted data to bytes for transmission
    #
    # Parameters:    data_out - object desired to transmitted
    def send(self, data_out):
        output = pickle.dumps(data_out)
        self.sock.send(output)

    # recv : This function takes recieves data of a fixe byte size. The pickle
    # unserializes the transmitted data for use by the recieving program
    #
    # Parameters:    bytes - number of bytes to recieve per transmission
    #                hdr - a size value to be used in future implementation
    #                       to recieve a dynamic amount of data
    def recv(self, bytes=4096, hdr=10):
        self.hdr = hdr
        data = self.sock.recv(bytes)
        self.data = pickle.loads(data)

    # sock : This function allows the the socket connection to be redfined
    # resetting variables, while taking the 'host' 7 'port'
    def sock(self, host='localhost', port=4770):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    # drop : This function drops the connection established with the client
    # prgram adnd resets the relative class values to their default
    def drop(self):
        self.sock.close()

    # print : This function prints the data recieved and stored in the
    # server socket's data variable
    def print(self):
        print(self.data)

# User : A custom object class for testing custom object transmission
# between client and server programs. The object contains user data
# that would be stored on the server and retrieved by the client
class USER:
    def __init__(self, user="", settings=[], id=0, st=0, et=0):
        self.user = user
        self.settings = settings
        self.id = id
        self.start_time = st
        self.end_time = et
        self.data

    # print : Prints user object data variables
    def print(self):
        print("User: ", self.user, "\nSettings: ", self.settings, "\nID: ",
              self.id, "\nStart: ", self.start_time, "\nend_time: ", self.end_time)