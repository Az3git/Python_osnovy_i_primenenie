ans = []
objects = [1, 2, 3, 1, 2, 3, 1, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3, 2, 1]

k = len(objects)
i = 0
print(len(objects))


while i < k - 1:
    u = i + 1
    while u < k:
        if objects[i] is objects[u]:
            del objects[u]
            k -= 1
        else:
            u += 1
    i += 1
print(len(objects))

