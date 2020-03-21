from netmiko import ConnectHandler
#import csv
#import pandas as pd
import json

iosv_l2_s1_con = {
    'device_type': 'cisco_ios',
    'ip': '1.1.1.1',
    'username': 'samuel',
    'password': 'samuel'
}

iosv_l2_s2_con = {
    'device_type': 'cisco_ios',
    'ip': '2.2.2.2',
    'username': 'samuel',
    'password': 'samuel'
}

all_devices = [iosv_l2_s1_con, iosv_l2_s2_con]

y ={}

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    show_commands="show interfaces status"
    outputShow = net_connect.send_command(show_commands)
    outputArray = outputShow.splitlines()
    count = 0
    j=2
    arrOfIntStatus=[]
    
    for j in range(2,len(outputArray)):
        tempArr = []
        i = 0 #Second Index
        while i < len(outputArray[j]):
            tempStr=""
            while(outputArray[j][i]!=" ") and (i<len(outputArray[j])-1):
                tempStr += outputArray[j][i]
                i+=1
            if(tempStr!=""):
                if(i==len(outputArray[j])-1):
                    tempStr+= outputArray[j][len(outputArray[j])-1]
                tempArr.append(tempStr)
            else:
                i+=1
        #print(tempArr)
        dictOfInt= {}
        dictOfInt.update({'interface':tempArr[0]})
        dictOfInt.update({'status':tempArr[1]})
        dictOfInt.update({'vlan':tempArr[2]})
        dictOfInt.update({'duplex':tempArr[3]})
        dictOfInt.update({'speed':tempArr[4]})
        dictOfInt.update({'Type':tempArr[5]})
        arrOfIntStatus.append(dictOfInt)
    
    #print(arrOfIntStatus)
    dicOfThisDevice={}
    output = net_connect.send_command("show run | in hostname")
    output = output.split(" ")
    hostname = output[1]
    dicOfThisDevice.update({hostname: arrOfIntStatus})
    y.update(dicOfThisDevice)
dump=json.dumps(y)
print(dump)

with open('data.txt', 'w') as outfile:
    json.dump(y, outfile)