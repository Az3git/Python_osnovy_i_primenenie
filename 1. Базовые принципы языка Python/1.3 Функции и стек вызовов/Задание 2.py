n, k = map(int, input().split())

def func(a, b):
    if b > a:
        return 0
    elif b == 0:
        return 1
    else:
        if b == 1:
            return a
        elif a == b:
            return 1
        else:
            return func(a - 1, b) + func(a - 1, b - 1)

print(func(n,k))






