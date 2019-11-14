import csv

with open(r'names.csv', 'a', newline='') as csvfile:
    fieldnames = ['This','aNew']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'This': ['is'], 'aNew': ['Row']})