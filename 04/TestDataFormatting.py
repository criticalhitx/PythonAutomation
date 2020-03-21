import json

y ={
    "iosv_l2_s3": [
    {"interface": "G0/1", "status": "not connect"},
    {"interface": "G0/2", "status": "connected"},
    {"interface": "G0/3", "status": "connected"}
  ]
}

arrOfIntStatus = []
for i in range (5):
  dictOfInt = {}
  intName = "E0/"+str(i)
  intStat = "not connect"
  dictOfInt.update({'interface':intName})
  dictOfInt.update({'status':intStat}) 
  arrOfIntStatus.append(dictOfInt)

x = {}
devName = "Switch5"
x.update({devName : arrOfIntStatus})
y.update(x)

dump=json.dumps(y)
print(dump)
