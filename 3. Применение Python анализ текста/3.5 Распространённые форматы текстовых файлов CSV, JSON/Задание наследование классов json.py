import json
dictu = {}
listo = []
i = 0
data = input()
data_json = json.loads(data)
bul = False
def search_parents(child, prohod):
    global listo
    global i
    global bul
    i += 1
    for el in data_json:
        if prohod in el['parents']:
            bul = True
            if el['name'] in listo:
                pass
            else:
                listo.append(el['name'])
            dictu[child] = listo
            search_parents(child, el['name'])

for el in data_json:
    child = el['name']
    search_parents(child, child)
    if bul == False:
        dictu[child] = []
    bul = False
    i = 0
    listo = []

n = sorted(dictu)
for el in n:
    print(el, ' : ', len(dictu[el]) + 1)