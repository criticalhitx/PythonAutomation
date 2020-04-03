def getIPArray(IPinput):
    x=IPinput.split('.')
    return x

inpIP = input("Input your IP Address : ")
result = getIPArray(inpIP)
print(result)