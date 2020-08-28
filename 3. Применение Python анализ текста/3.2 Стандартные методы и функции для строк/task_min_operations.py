import sys

s, a, b, n = [input() for i in range(3)] + [0]

while True:
    if n > 1000:
        print('impossible')
        sys.exit()
    if a in s:
        n += 1
        s = s.replace(a, b)
    else:
        break

print(n)
