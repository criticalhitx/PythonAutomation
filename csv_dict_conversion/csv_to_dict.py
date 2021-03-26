import csv
import json

f =open('Names.csv', 'r')
reader = csv.reader(f)
car = []
firstline=True
for row in reader:
    if firstline: #ignore first line
        firstline=False
        header =[] #Get header of csv file into list########
        for x in row:
            if x : 
                header.append(x)
            else:
                break
        continue ###########################################
    
    if not row: #ignore if row empty
        continue
    
    entry = {}
    n = 0
    for field in header:
        entry[field] = row[n]
        n=n+1
    car.append(entry) #append dict into list

print(header)
print(car) #printing list
with open('car.json', 'w') as outfile:
    json.dump(car,outfile)