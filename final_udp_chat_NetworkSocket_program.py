import socket
import threading as th
import os


def updateIpPort(ip,port,lst):
    if not lst:
        lst.append({"IP":ip,"PORT":port})
    else:
        size = len(lst)
        count = 0
        for i in range(0,size):
            tip = lst[i]["IP"]
            tport = lst[i]["PORT"]
            if(tip == ip and tport == port):
                continue
            elif(tip != ip and tport != port):
                count += 1
                continue
            elif(ip == tip and port != tport):
                lst.pop(i)
                lst.append({"IP":ip,"PORT":port})
        if count == size:
            lst.append({"IP":ip,"PORT":port})


def sendMessage(rip,rport,msg):
    s.sendto( msg.encode() , ( rip,rport ) )
    print("\n")


def recvmsg():
    while True:
        msgr = s.recvfrom(1024)
        print("\n\t\t\t\t\t\tMessage from receiver: ",msgr[0].decode(),"\n")
        updateIpPort(msgr[1][0],msgr[1][1],lst)
        print("\t\t\t\t\t\tIP: ",msgr[1][0], " Port: ", msgr[1][1],"\n\n")
        print("List of Receivers: ", lst)
        global stopThread
        if stopThread:
            break


def sendMessageInGroup(msgs, lst):
    for i in range(0,len(lst)):
        s.sendto( msgs.encode() , (lst[i]["IP"],lst[i]["PORT"]) )
    print("\n")


selfIP = ""
selfPort = int(input("\nEnter your Port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (selfIP, selfPort) )
lst = []

def todo():
    print("""\n\t\t\t\t\tWelcome

                            #### What you want to do ####

                             1. chat personaly
                             2. chat with multiple system in parallel

                            ## Type 'exit' to Quit ##
        """)
    choice = input("Enter your choice: ")
    return choice

choice = todo()

while choice is not "exit":

    if ("exit" in choice or "quit" in choice):
        print("\n\t\t\t\t\tBye!!!")
        os._exit(1)

    elif ("chat" in choice or int(choice) == 1 or "personal" in choice ):
        print("\n\t\t\tYou choose to chat personaly")
        receiverIP = str(input("\nEnter Receiver IP Address: "))
        receiverPort = int(input("Enter Receiver Port number: "))
        time = True
        while time:
            stopThread = False
            t1 = th.Thread( target=recvmsg, daemon = True )
            t1.start()

            message = input("\nEnter your Message: ")
            sendMessage(rip=receiverIP,rport=receiverPort,msg=message)

            cntnue = True
            cntnue = input("\t\t\tPress ENTER to continue or type exit to Quit: ")
            if (("exit" or "quit") in cntnue):
                stopThread = True
                time = False
                lst = []
                choice = todo()


    elif ( "multiple" in choice or int(choice) == 2 ):
        print("\n\t\t\tYou choose to chat with Multi System")
        receiverIP = str(input("\nEnter Receiver IP Address: "))
        receiverPort = int(input("Enter Receiver Port number: "))
        lst.append({"IP":receiverIP,"PORT":receiverPort})
        time = True
        while time:
            stopThread = False
            t2 = th.Thread( target=recvmsg , daemon = True )
            t2.start()

            message = input("\nEnter your Message: ")
            sendMessageInGroup(message,lst)

            cntnue = True
            cntnue = input("\t\t\tPress ENTER to continue or type exit to Quit: ")
            if (("exit" or "quit") in cntnue):
                stopThread = True
                time = False
                lst = []
                choice = todo()