# put your python code here
n = int(input())
i = 0
m = 0
summa = 0
if (n <= 100) and (n >= 0):
    while (i < n):
        m = int(input())
        summa += m
        i += 1
print(summa)
