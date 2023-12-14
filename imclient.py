#1. Wait for the user to type in a message.
#2. Send a message to the server.
#3. Wait for there to be a reply from the other user.
#4. Fetch and display the reply.
import time
from im import IMServerProxy

def main():
    # initialize IMserver
    server = IMServerProxy('https://web.cs.manchester.ac.uk/j18540bw/COMP28112_ex1/IMserver.php')


    if len(server.keys()) == 1:
        server['user1'] = 'start'
        user = 'user1'
        contact = 'user2'
        print('User 1 connected')
    else:
        server['user2'] = 'start'
        user = 'user2'
        contact = 'user1'
        print('User 2 connected')

    
    if user == 'user1':
        while len(server.keys()) == 2 :
            time.sleep(1)
        print('User 2 connected')

    # main loop
    while len(server.keys()) >= 3: 
        #User 1
        if user == 'user1':
            # input message
            myMessage = input('Type your message: ')
            # exit message
            if myMessage == 'x':
                print('Exiting message system.')
                server[user] = 'x'
                time.sleep(4)
                server.clear()
                break
            else:
                # set message
                server[user] = myMessage
                server['user1Finished'] = 'True'
                # Wait untill message reply
                while len(server.keys()) == 4 and server[contact] != 'x':
                    time.sleep(1)
                # Print reply
                reply = server[contact]
                if reply == b'x\n':
                    print('Other user quit... Exiting message system')
                    time.sleep(1)
                    server.clear()
                    break
                else:
                    print(reply.decode())
        else:
            # User 2
                # Wait untill message reply
                time.sleep(2)
                while len(server.keys()) == 3 and server[contact] != 'x':
                    time.sleep(1)
                # Print reply
                reply = server[contact]
                if reply == b'x\n':
                    print('Other user quit... Exiting message system')
                    time.sleep(1)
                    server.clear()
                    break
                else:
                    print(reply.decode())
                    # input message   
                    myMessage = input('Type your message: ')
                    # exit message
                    if myMessage == 'x':
                        print('Exiting message system.')
                        server[user] = 'x'
                        del server['user1Finished']
                        time.sleep(4)
                        server.clear()
                        break
                    else:
                        # set message
                        server[user] = myMessage
                        del server['user1Finished']

            
            

main()