import csv
import os

with open('Dashlane.csv', newline='') as dashlaneFile:
    spamreader = csv.reader(dashlaneFile)
    for row in spamreader:
        os.system("security add-internet-password -a " + row[2] + " -w " + row[3] + " -r http -s " + row[1])
