import csv
import re
import collections

c = collections.Counter()
list = []
pattern = r'\d\d\/\d\d\/2015'
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    readers = csv.DictReader(f)
    for row in readers:
        if re.match(pattern, row['Date']):
            
            list.append(row['Primary Type'])
    print(list)
    for word in list:
        c[word] += 1
    print(c)