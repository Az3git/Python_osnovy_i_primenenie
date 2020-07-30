Global = {}
list_parent = []


def searching_parent(get_cl):
    global list_parent
    if type(get_cl) != list:
        print("No")
        return 0
    for ele in get_cl:
        wew = Global.get(ele)
        if wew is not None:
            list_parent += wew
            searching_parent(wew)

n1 = int(input())

for i in range(n1):
    spl_list = str(input()).replace(':', '').split()
    Global.update({spl_list[0]: spl_list[1:]})

n2 = int(input())

for i in range(n2):
    clas_pred, clas_nasl = map(str, input().split())
    if clas_pred == clas_nasl:
        if Global.get(clas_pred) is not None:
            print('Yes')
        else:
            print('No')
    else:
        res1 = Global.get(clas_nasl)
        if res1 is not None:
            if clas_pred in res1:
                print("Yes")
            else:
                searching_parent(Global.get(clas_nasl))
                if clas_pred in list_parent:
                    print("Yes")
                    list_parent.clear()
                else:
                    print("No")
                    list_parent.clear()
        else:
            print("No")