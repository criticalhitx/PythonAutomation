from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '1.1.1.1',
    'username': 'samuel',
    'password': 'samuel',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '2.2.2.2',
    'username': 'samuel',
    'password': 'samuel',
}


with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

