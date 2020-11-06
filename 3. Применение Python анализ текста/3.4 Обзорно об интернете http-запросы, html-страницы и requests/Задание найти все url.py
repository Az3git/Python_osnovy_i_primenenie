import requests
import re

listA = []
linkInA = []

strA = input()

resA = requests.get(strA)

textA = resA.text

pattern = r'<a(.)+href=(\"|\')(\w+\://)?(\w(\w|\.|\-|\d)+)'


linkInA = re.findall(pattern, textA)

for el in linkInA:
    listA.append(el[3])
    
my_set = set(listA)

for el in sorted(my_set):
    print(el)