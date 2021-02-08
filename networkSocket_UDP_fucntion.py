import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lst = []

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
        print("\n\nMessage from receiver: ",msgr[0].decode(),"\n")
        updateIpPort(msgr[1][0],msgr[1][1],lst)
        print("IP: ",msgr[1][0], " Port: ", msgr[1][1],"\n\n")
        print(lst)

def sendMessageInGroup():
    while True:
        msgs = input("\nType your message: ").encode()
        for i in range(0,len(lst)):
            s.sendto( msgs ,(lst[i]["IP"],lst[i]["PORT"]))
        print("\n")
