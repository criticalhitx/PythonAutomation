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
    print("Connecting to "+devices['ip'])
    net_connect = ConnectHandler(**devices)
    show_commands="show interfaces status"
    outputShow = net_connect.send_command(show_commands)
    outputArray = outputShow.splitlines()
    
    host = net_connect.send_command("show run | in hostname")
    host = host.split(" ")
    hostname = host[1]
    
    net_connect.disconnect()
    count = 0
    j=2
    arrOfIntStatus=[]
    
    for j in range(2,len(outputArray)):
        mn = []
        mn = str(outputArray[j])
        mn = mn.split(" ")
        while("" in mn):
        	mn.remove("")
        if("not" in mn):
        	mn.remove("not")
        	mn[1]="not-connect"
        dictOfInt= {}
        dictOfInt.update({'interface':mn[0]})
        dictOfInt.update({'status':mn[1]})
        dictOfInt.update({'vlan':mn[2]})
        dictOfInt.update({'duplex':mn[3]})
        dictOfInt.update({'speed':mn[4]})
        dictOfInt.update({'Type':mn[5]})
        arrOfIntStatus.append(dictOfInt)
    

    #print(arrOfIntStatus)
    dicOfThisDevice={}

    dicOfThisDevice.update({hostname: arrOfIntStatus})
    y.update(dicOfThisDevice)
dump=json.dumps(y)
#print(dump)
selectedSwitch = input("Select a Switch: ")
data = y.get(selectedSwitch) #Get Value of Dictionary
selectedInterface =input("Select an Interface to view status: ")
for i in data: #if data is list of dictionary, then 
    if i['interface'] == selectedInterface:
            queryRes = i['vlan']
            break
print(queryRes)

