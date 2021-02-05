import socket
import threading as th
import networkSocket_UDP_fucntion as nsuf



selfIP = str(input("Enter your IP Address: "))
selfPort = int(input("Enter your Port number: "))
print( selfIP )
print( selfPort )

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (selfIP, selfPort) )
lst = []

def todo():
    print("""\t\tWelcome
        #### What you want to do ####
        1. chat personaly
        2. chat with multiple system in parallel

            ## Type 'exit' to Quit ##
        """)
    choice = input("Enter your choice: ")
    return choice

choice = todo()


if ("exit" in choice or "quit" in choice):
    print("\n\tBye!!!")
    exit()

elif ("chat" in choice or int(choice) == 1):
    print("\tYou choose to chat personaly")
    receiverIP = str(input("Enter Receiver IP Address: "))
    receiverPort = int(input("Enter Receiver Port number: "))
    time = True
    while time:
        message = input("Enter your Message: ")
#        nsuf.sendMessage(rip=receiverIP,rport=receiverPort,msg=message)

        t1 = th.Thread( name="Receive message: " ,target=nsuf.recvmsg )
        t1.start()

        t2 = th.Thread( name="Send message: " ,target=nsuf.sendMessage(rip=receiverIP,rport=receiverPort,msg=message) )
        t2.start()

        cntnue = True
        cntnue = input("Press ENTER to continue or type exit to Quit: ")
        if (("exit" or "quit") in cntnue):
            time = False
            todo()