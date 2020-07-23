def closest_mod_5(x):
    for i in range(5):
        y = x
        y = y + i
        if y % 5 == 0:
            return y


x = int(input())

print(closest_mod_5(x))
