#Get Octets from IPString ------------------------------
#params = (str) ip address
#output = array of ip address
def getIPOctets(ipaddr):
    leng = len(ipaddr)
    patokan=0
    countOctet=0
    IParr=[]
    for i in range(0,len(ipaddr)-1):
        if(ipaddr[i]=='.'):
            outputOctet="" # string output to octet number
            for j in range(patokan,i):
                outputOctet+=ipaddr[j]
            patokan=i+1
            IParr.append(int(outputOctet))
            countOctet+=1
        if(countOctet==3):
            break
    outputOctet=""
    for k in range(patokan,len(ipaddr)):
        outputOctet+=ipaddr[k]
    IParr.append(int(outputOctet))
    return IParr
#---------------------------------------------------------