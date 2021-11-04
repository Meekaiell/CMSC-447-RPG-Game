import time, socket, pickle, json

class SR_SK:
    def __init__(self, host=socket.gethostname(), port=80, hdr = 10, listen=5):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clnt = 0
        self.adr = 0
        self.hdr = hdr
        self.listen = listen
        self.sock.bind((self.host,self.port))
        self.sock.listen(self.listen)
    #listen
    def listen(self, listen=5):
        self.listen = listen
        self.sock.listen(self.listen)
    #send
    def send(self, data_out):
        self.clnt,self.adr = self.sock.accept()
        print(f"Connection to {self.adr} established")
        data = pickle.dumps(data_out)
        self.clnt.send(data)
        self.clnt.close()
    #recv
    def recv(self,bytes = 4096, hdr = 10):
        self.data = b''
        self.data = self.sock.recv(bytes)
        self.data = pickle.loads(self.data)
    #drop
    def drop(self):
        self.clnt.close()
        self.clnt = 0
        self.adr = 0
    #print
    def print(self):
        print(self.data)

class CT_SK:
    #__init__ :
    def __init__(self, host=socket.gethostname(), port=4771, hdr = 10, listen=1):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
        self.hdr = hdr
        self.listen = listen
        self.sock.connect((self.host,self.port))
    #connect
    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
        except:
            return False
    #send
    def send(self, data_out):
        output = pickle.dumps(data_out)
        self.sock.send(output)
    #recv
    def recv(self, bytes=4096, hdr=10):
        self.hdr = hdr
        data = self.sock.recv(bytes)
        self.data = pickle.loads(data)
    #sock
    def sock(self, host='localhost', port=4770):
        self.host = host
        self.port = port
        self.data = b''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hdr = hdr
    #drop
    def drop(self):
        self.sock.close()
    #print
    def print(self):
        print(self.data)

class USER:
    # User : A custom object class for testing object transmission
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