#This script is to automatically create loopback interface
#and set ip address to the interface automatically

import telnetlib

user = "samuel"
password = "samuel"

f = open ('listipmanagement.txt')

for HOST in f:
    HOST=HOST.strip()
    print("Configuring Switch " + (HOST))
    tn=telnetlib.Telnet(HOST)
    tn.read_until(b"Username:")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")

    #this is loop to create loopback ip address of router
    for i in range(1,11):
        tn.write(b"int loo"+str(i).encode('ascii')+b"\n")
        tn.write(b"ip address 200.200.200."+str(i).encode('ascii')+b" 255.255.255.255\n")
        print("Succeed Creating Loopback"+str(i)+ " in host "+str(HOST))
    tn.write(b"end\n")
    tn.write(b"exit\n")
    x=tn.read_all().decode('ascii')
    print(x)

