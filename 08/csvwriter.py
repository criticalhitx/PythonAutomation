import csv

with open('mycsv.csv', 'w', newline='') as f:
    fieldnames = ['sizeList', 'priceList']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    thewriter.writerow({'sizeList' : '10', 'priceList' : '1000'})