import datetime
strinp = ''

year, month, day = map(int, input().split())
delt = int(input())
spisok = str(datetime.date(year, month, day) + datetime.timedelta(delt)).replace('-', ' ').split()
for elem in spisok:
    if elem[0] == '0':
        strinp += elem[1:] + ' '
    else:
        strinp += elem + ' '
print(strinp[0:-1])
