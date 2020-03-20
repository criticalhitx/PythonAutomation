#ProgramName = 03_CalculateNetworkAddress
#Description = To Calculate your network address

from getNetAdd import getNetAddAry,getBroadcastAddAry
from getIPOctets import getIPOctets

#Definitions

#checkMask check whether netmask is valid.
def checkMask(mask):
    if ((mask<0) or (mask>32)):
        return False
    else:
        return True

#Menu1 procedure : Network Address Calculator
def menu1():
	IP = input("Enter Your IP Address : ")
	IPOct = getIPOctets(IP) #Array of Integer Octet Of IP address
	mask = input ("Enter Your Subnet Mask : ")
	mask = int(mask)

	#Subnet mask must between 0 to 32
	while(not checkMask(mask)):
	    print("Better take your CCNA :)\n")
	    mask = input ("Enter Your Subnet Mask : ")
	    mask = int(mask)

	netAddArray = getNetAddAry(IPOct,mask)
	netAddString = ""
	for i in range(4):
	    netAddString+=str(netAddArray[i])
	    netAddString+="."

	print("Your Network Address : "+netAddString[:-1])
	
	broadAddArray = getBroadcastAddAry(IPOct,mask)
	broadAddString = ""
	for i in range(4):
	    broadAddString+=str(broadAddArray[i])
	    broadAddString+="."

	print("Your Broadcast address: "+broadAddString[:-1])

	return;



##------------------Program Begin ----------------------######
print("Welcome to Samuel Network Automation Tool\n\n")
print("Menu Available:\n")
print("1. Network and Broadcast Address Calculator\n")
print("2. TBA\n")
menu = input("Please enter a menu : ")

if(menu=="1"):
	menu1()




