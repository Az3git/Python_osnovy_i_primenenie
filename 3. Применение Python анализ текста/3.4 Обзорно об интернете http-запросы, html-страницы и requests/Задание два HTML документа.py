import requests
import re


listA = []
linkInA = []
strA = input()
strB = input()
i = 0
def search(str1, str2, shetch = 0):
    listA = []
    resA = requests.get(str1)

    textA = resA.text

    pattern = r'<a href=".+">'
    pattern2 = r'https:.+\.html'

    linkInA = re.findall(pattern, textA)

    for elem in linkInA:
        listA.append(re.search(pattern2, elem).group(0))

    if str2 in listA and shetch != 0:
        return 'Yes'

    return listA
try:
    listAnew = search(strA, strB)
except:

    print('No')

for el in listAnew:

    try:
        if search(el, strB, 1) == 'Yes':

            print('Yes')
            i = 1
            break
    except:
        True

if i == 0:
    print('No')

