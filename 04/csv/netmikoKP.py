from netmiko import ConnectHandler
import csv
import pandas as pd

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '1.1.1.1',
    'username': 'samuel',
    'password': 'samuel'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '2.2.2.2',
    'username': 'samuel',
    'password': 'samuel'
}

all_devices = [iosv_l2_s1,iosv_l2_s2]
finalArray = []

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    show_commands="show interfaces status"
    outputShow = net_connect.send_command(show_commands)
    outputArray = outputShow.splitlines()
    ipAdd = devices['ip']
    outputArray.insert(0,ipAdd)
    finalArray+=outputArray+[]
    df = pd.DataFrame(finalArray, columns=["Interfaces Status"])
namaFile='Interfaces_Status.csv'
df.to_csv(namaFile, index=False)