from Sockets import Server_SKT, Client_SKT, USER, socket, pickle, time

HOST = socket.gethostname()
PORT = 4770

# Creating server socket instance
SR1 = Server_SKT(HOST, PORT)
while True:
    prompt = input('Action: ')

    # Test Drop function
    if prompt == 'drop':
        SR1.drop()

    # Test the sending of different data types
    elif prompt == 'send':
        valid = False
        while valid == False:
            to_send = input('What to send? ')
            if to_send == 'msg':
                msg = input('[Type Your Message]: ')
                SR1.send(msg)
                print('Sent: ', msg)
                valid = True
            elif to_send == 'usr':
                name = input('Username? ')
                myUser = USER(name)
                SR1.send(myUser)
                print('Sent: ')
                myUser.print()
                valid = True
            elif to_send == 'int':
                num = int(input('Number? '))
                SR1.send(num)
                print('Sent: ', num)
                valid = True

    # Test the recieving funciton
    elif prompt == 'recv':
        SR1.recv()
        if SR1.data:
            print('Received data: ', SR1.data)
        else:
            break

    elif prompt == 'break':
        break

