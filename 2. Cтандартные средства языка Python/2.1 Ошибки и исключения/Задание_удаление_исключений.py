Global = {}
list_delete = []
list_input = []
n1 = int(input())

for _ in range(n1):
    spl_list = str(input()).replace(':', '').split()
    Global.update({spl_list[0]: spl_list[1:]})

def child_list(aviable_class):
    for key in Global:
        s = Global.get(key)
        if aviable_class in s:
            if key not in list_delete:
                list_delete.append(key)
                child_list(key)

n2 = int(input())

for _ in range(n2):
    s = str(input())
    if s in list_delete:
        list_input.append(s)
    else:
        child_list(s)

for elm in list_input:
    print(elm)

