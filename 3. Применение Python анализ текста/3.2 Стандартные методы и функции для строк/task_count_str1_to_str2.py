s, t, i, count = [input() for i in range(2)] + [0] + [0]


while True:
    index = s.find(t, i)
    if index == -1:
        break
    else:
        count += 1
        i = index + 1


print(count)