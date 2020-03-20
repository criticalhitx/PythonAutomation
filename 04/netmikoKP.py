from netmiko import ConnectHandler
import csv

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

all_devices = [iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    show_commands="show interfaces status"
    outputShow = net_connect.send_command(show_commands)
    outputArray = outputShow.splitlines()

with open('yourNewFileName.csv', 'w', ) as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in outputArray:
        wr.writerow([word])