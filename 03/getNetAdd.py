#Calculate Network Address
#param : IParry = array of IP , mask = subnet mask (int)
#output: Array of Network Address
def getNetAddAry(IPary,mask):
    outputArr=[]
    if(mask<=8):
        hostbit=8-mask
        multiplier=2**hostbit
        count=0
        while(IPary[0]-count>=multiplier):
            count+=multiplier
        IPary[0]=count
        IPary[1]=0
        IPary[2]=0
        IPary[3]=0
        return IPary 
    elif(mask<=16):
        hostbit=16-mask
        multiplier=2**hostbit
        count=0
        while(IPary[1]-count>=multiplier):
            count+=multiplier
        IPary[1]=count
        IPary[2]=0
        IPary[3]=0
        return IPary
    elif(mask<=24):
        hostbit=24-mask
        multiplier=2**hostbit
        count=0
        while(IPary[2]-count>=multiplier):
            count+=multiplier
        IPary[2]=count
        IPary[3]=0
        return IPary
    else:
        hostbit=32-mask
        multiplier=2**hostbit
        count=0
        while(IPary[3]-count>=multiplier):
            count+=multiplier
        IPary[3]=count
        return IPary
#-----------------------------------------------------------#

def getBroadcastAddAry(IPary,mask):
    outputArr=[]
    if(mask<=8):
        hostbit=8-mask
        multiplier=2**hostbit
        count=0
        while(IPary[0]-count>=multiplier):
            count+=multiplier
        IPary[0]=count+multiplier-1
        IPary[1]=0
        IPary[2]=0
        IPary[3]=0
        return IPary 
    elif(mask<=16):
        hostbit=16-mask
        multiplier=2**hostbit
        count=0
        while(IPary[1]-count>=multiplier):
            count+=multiplier
        IPary[1]=count+multiplier-1
        IPary[2]=0
        IPary[3]=0
        return IPary
    elif(mask<=24):
        hostbit=24-mask
        multiplier=2**hostbit
        count=0
        while(IPary[2]-count>=multiplier):
            count+=multiplier
        IPary[2]=count+multiplier-1
        IPary[3]=0
        return IPary
    else:
        hostbit=32-mask
        multiplier=2**hostbit
        count=0
        while(IPary[3]-count>=multiplier):
            count+=multiplier
        IPary[3]=count+multiplier-1
        return IPary
#-----------------------------------------------------------#