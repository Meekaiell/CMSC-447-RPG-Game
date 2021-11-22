import pickle
import platform
import ssl
import socket
import time


# Server_SkT : The server socket class for communicating with the
# Client_SKT class(client socket), using the socket library.
# The class contains 'host' & 'port' variables for client binding, along with
# 'client' & 'address' variables to accept connection requests.
#
# Parameters:    host - The address of the server program; default: localhost
#                port - Desired port to bind and transmit over; default: 80
#                listen - Number of allowed queued connections; default: 5
class ServerSocket:
    def __init__(self, host=socket.gethostname(), port=80, listen=1):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = socket.socket()
        self.address = socket.socket()
        self.hdr = 10
        self.listen = listen
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.listen)

    # listen : This function allows the suer to adjust the server's 'listen'
    # variable in order to adjust the backlog connection allowed to connect.
    # This effectively allows multiple users to bind in turn and connect on
    # first-come-first-serve basis.
    #
    # Parameters:    listen - Number of allowed queued connections; default: 5
    def listen(self, listen=5):
        try:
            self.listen = listen
            self.sock.listen(self.listen)
            self.client, self.address = self.sock.accept()
        except socket.error:
            print("Error: ", socket.error)

    # send : This function transmits data to the directed bind executed
    # in the Server_SKT initialization. The pickle library is used to
    # serialize the transmitted data to bytes for transmission
    #
    # Parameters:    data_out - object desired to transmitted
    def send(self, data_out):
        try:
            self.client, self.address = self.sock.accept()
            data = pickle.dumps(data_out)
            self.client.send(data)
            self.client.close()
        except socket.error:
            print("Error: ", socket.error)

    # ssl_send : This function transmits data to a client socket via an ssl wrapped
    # socket. This validates a connection with a cer
    def ssl_send(self, data_out, pem_path, crt_path, key_path):
        sslwrap = ssl.SSLContext()
        sslwrap.verify_mode = ssl.CERT_REQUIRED

        sslwrap.load_verify_locations(pem_path)
        sslwrap.load_cert_chain(certfile=crt_path, keyfile=key_path)

        ssl_sock = sslwrap.wrap_socket(self.sock,server_side=True)
        ssl_sock.bind((self.client, self.address))

        ssl_sock.listen()

        while(True):
            (self.client, self.address) = sslwrap.accept()
            to_send = pickle.dumps(data_out)
            sslwrap.sendall(to_send)
        ssl_sock.drop()

    # recv : This function takes receives data at of a fixed byte size. The pickle
    # un-serializes the transmitted data for use by the receiving program
    #
    # Parameters:    byte_size - number of bytes to receive per transmission
    #                hdr - a size value to be used in future implementation
    #                       to receive a dynamic amount of data
    def recv(self, byte_size=64, hdr=10):
        # self.data = b''
        # self.data = self.sock.recv(byte_size)
        # self.data = pickle.loads(self.data)
        time.sleep(1)
        while True:
            self.client, self.address = self.sock.accept()
            try:
                while True:
                    data = self.client.recv(byte_size)
                    if data:
                        self.data += data
                    else:
                        break
            finally:
                self.data = pickle.loads(self.data)
                self.client.close()
                # exit()

    # recv_2 : Ths function allows the server socket
    def recv_2(self, byte_size=64, timeout=0):
        while True:
            self.client, self.address = self.sock.accept()
            try:
                while True:
                    data = self.client.recv(byte_size)
                    if data:
                        print(f"Received data: {data} ")
                    else:
                        break

            finally:
                self.client.close()
                print("Connection closed.")
                exit()

    # drop : This function drops the connection established with the client
    # program and resets the relative class values to their default
    def drop(self):
        try:
            self.client.close()
            self.client = socket.socket()
            self.address = socket.socket()
        except socket.error:
            print("Error: ", socket.error)

    # print : This function prints the data received and stored in the
    # server socket's data variable
    def print(self):
        print(self.data)


# Client_SKT : The client socket class for communicating with the
# Server_SkT server class.
#
# Parameters:    host - The Ip address of the server program; default: localhost
#                port - Desired port to bind and transmit over; default: 80
class ClientSocket:
    def __init__(self, host=socket.gethostname(), port=80):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket()  # socket.AF_INET, socket.SOCK_STREAM
        self.hdr = 0
        self.connect()

    # connect : This function is a direct 'connect' function for retrying a
    # a connection to the server
    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
        except socket.error:
            print("Error: ", socket.error)

    # send : This function transmits data to the directed bind executed
    # in the Server_SKT initialization. The pickle library is used to
    # serialize the transmitted data to bytes for transmission
    #
    # Parameters:    data_out - object desired to transmitted
    def send(self, data_out, times=10):
        try:
            output = pickle.dumps(data_out)
            self.sock.sendall(output)
            time.sleep(2)
            self.sock.close()
        except socket.error:
            print("Error: ", socket.error)

    # ssl_recv : This function takes receives data of a fixe byte size. The pickle
    # un-serializes the transmitted data for use by the receiving program
    # Parameters:    byte_size - number of bytes to receive per transmission
    def ssl_recv(self, byte_size=1024):
        sslwrap = ssl.SSLContext();
        sslwrap.verify_mode = ssl.CERT_REQUIRED;
        if platform.system().lower() == 'darwin':
            import certifi
            import os
            # Load the CA certificates used for validating the certificate of the server
            sslwrap.load_verify_locations(cafile=os.path.relpath(certifi.where()), capath=None, cadata=None);

        sslsock = sslwrap.wrap_socket(self.sock, do_handshake_on_connect=True)
        sslsock.connect((self.host, self.port))

        while (True):
            data = '';
            data = sslwrap.recv(byte_size)

            if data == b'':
                break
            self.data += data
        self.data = pickle.loads(self.data)
        activesock = sslsock.unwrap()
        sslwrap.close()
        activesock.close()

    # recv : This function takes receives data of a fixe byte size. The pickle
    # un-serializes the transmitted data for use by the receiving program
    #
    # Parameters:    byte_size - number of bytes to receive per transmission
    #                hdr - a size value to be used in future implementation
    #                       to receive a dynamic amount of data
    def recv(self, byte_size=4096, hdr=10):
        try:
            self.hdr = hdr
            data = self.sock.recv(byte_size)
            self.data = pickle.loads(data)
            # get_msg = True
            # while True:
            #     msg = self.sock.recv(byte_size)
            #     if get_msg:
            #         x = int(msg[:hdr])
            #         get_msg = False
            #     self.data += msg
            #     if len(self.data) - hdr == x:
            #         self.data = pickle.loads(self.data[hdr:])
            #         print(self.data)
            #         get_msg = True
            #         self.data = b''
            # print(self.data)

        except socket.error:
            print("Error: ", socket.error)

    # sock : This function allows the socket connection to be redefined, by
    # resetting the 'host' and 'pot' variables
    def sock(self, host='localhost', port=4770):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    # drop : This function drops the connection established with the client
    # program and resets the relative class values to their default
    def drop(self):
        self.sock.close()

    # print : This function prints the data received and stored in the
    # server socket's data variable
    def print(self):
        print(self.data)


# User : A custom object class for testing custom object transmission
# between client and server programs. The object contains user data
# that would be stored on the server and retrieved by the client
class USER:
    def __init__(self, user="", settings=[], uid=0, st=0, et=0):
        self.user = user
        self.settings = settings
        self.uid = uid
        self.start_time = st
        self.end_time = et
        self.data = 0

    # print : Prints user object data variables
    def print(self):
        print("User: ", self.user, "\nSettings: ", self.settings, "\nID: ",
              self.uid, "\nStart: ", self.start_time, "\nend_time: ", self.end_time)
