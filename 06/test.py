#to Test split command to prevent not

xArray = ['G10/1       not connect    1    auto     10/100/1000    1000-BaseTX']
x = xArray[0]
x = x.split(" ")
while("" in x) : 
    x.remove("") 
if ("not" in x):
	x.remove("not")
	x[1] = "not-connect"

print(x)