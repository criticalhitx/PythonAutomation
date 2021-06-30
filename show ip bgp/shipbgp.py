import pandas as pd

#PROCEDURE
def iosxe():
    listofdict = []
    with open('shipbgp.txt') as openfileobject:
        for line in openfileobject:
            line=line.rstrip()
            #For Normal Case on Best Path
            if line.startswith(' *>') or line.startswith('*>'):
                list1=line.split() # List of Best Path Line
                mydict={}
                mydict['Prefix'] = list1[1]
                try:
                    mydict['NextHop'] = list1[2]
                except:
                    continue
                aspath=""
                for i in range (3,len(list1)):
                    aspath = aspath + list1[i] + " "
                mydict['ASPath'] = aspath.rstrip()
                listofdict.append(mydict)
            #For Case Where show ip bgp line is entered to new row
            elif line.startswith('       '):
                list1=line.split()
                print("YES", list1)
                mydict['NextHop'] = list1[0]
                aspath=""
                for i in range (1,len(list1)):
                    aspath = aspath + list1[i] + " "
                mydict['ASPath'] = aspath.rstrip()
                listofdict.append(mydict)
            #For Not Base Path
            else : continue

    my_df=pd.DataFrame(listofdict)
    print(my_df)


    # create excel writer object
    writer = pd.ExcelWriter('output.xlsx')
    # write dataframe to excel
    my_df.to_excel(writer, index=False)
    # save the excel
    writer.save()
    print('DataFrame is written successfully to Excel File.')

#MAIN MENU
print("Select Environment:")
print("1 IOS-XE")
print("2 NXOS")
ciscoOS=input("Please Choose [1/2] : ")

if ciscoOS=='1':
    iosxe()