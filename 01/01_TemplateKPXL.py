import getpass
import telnetlib
import socket
import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
"""
HOST = "10.21.110.7"
#username: xlinfrakape
#Password: !Q0jEYLu

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username:")
tn.write(b"xlinfrakape\n")
tn.write(b"!Q0jEYLu\n")
"""
print('Persiapan Selesai\n')

xz=0

textfile = open("listipmanagement.txt","r")
while xz<2 :
    xz=xz+1
    print('baris ke - '+ str(xz))
    a = textfile.readline()
    HOST = a[0:len(a)-1]
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sck.connect_ex((HOST, 23)) == 0:
        print(HOST + '---->>TELNET BUKA')
        print("Telnetting to " + HOST)
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username:")
        tn.write(b"samuel\n") #username
        tn.write(b"samuel\n") #password
        tn.write(b"enable\n") #enter enable mode
        tn.read_until(b"Password:")
        tn.write(b"samuel\n") #enter enable password
        tn.write(b"terminal length 0\n")
        tn.write(b"show ip route\n")
        tn.write(b"ls\n")
        tn.write(b"exit\n")
        
        x=tn.read_all().decode('ascii')
        print(x)
        """
        print("HOSTNAME : "+HOST)
        print("             Jumlah 100BaseTX      = ",x.count("TX"))
        print("             Jumlah  10Gbase-SR    = ",x.count("10Gbase-SR"))
        print("             Jumlah 10Gbase-SR-S   = ",x.count("10Gbase-SR-S"))
        print("             Jumlah 1000BASE-T     = ",x.count("1000BASE-T"))
        print("             Jumlah 1000BASE-SX    = ",x.count("1000BASE-SX"))
        print("             Jumlah 1000BASE-LX/LH = ",x.count("1000BASE-LX/LH"))
        print("             Jumlah 1000BASE-EX    = ",x.count("1000BASE-EX"))
        print("             Jumlah 1000BASE-ZX    = ",x.count("1000BASE-ZX"))
        print("             Jumlah QSFP-40G-SR-BD = ",x.count("QSFP-40G-SR-BD"))"""
    elif sck.connect_ex((HOST, 22)) == 0:
        print(HOST + '---->SSH BUKA')
        ssh.connect(HOST, port=22, username='samuel', password='samuel')
        stdin, stdout, stderr = ssh.exec_command('show ip route')
        stdin.write('exit')
        output = stdout.readlines()
        x=len(output)
        hasil = ''
        for i in range(1,x):
            hasil=hasil+output[i]
        x=hasil
        """
        print("HOSTNAME : "+HOST)
        print("             Jumlah 100BaseTX      = ",x.count("TX"))
        print("             Jumlah 10Gbase-SR    = ",x.count("10Gbase-SR"))
        print("             Jumlah 10Gbase-SR-S   = ",x.count("10Gbase-SR-S"))
        print("             Jumlah 1000BASE-T     = ",x.count("1000BASE-T"))
        print("             Jumlah 1000BASE-SX    = ",x.count("1000BASE-SX"))
        print("             Jumlah 1000BASE-LX/LH = ",x.count("1000BASE-LX/LH"))
        print("             Jumlah 1000BASE-EX    = ",x.count("1000BASE-EX"))
        print("             Jumlah 1000BASE-ZX    = ",x.count("1000BASE-ZX"))
        print("             Jumlah QSFP-40G-SR-BD = ",x.count("QSFP-40G-SR-BD")) """      
    else:
        print('Cant connect to SSH and TELNET')
        xz=xz+1-1
    sck.close()
    print('Exiting '+HOST+'\n')
