import itertools

def primes():
    a = []
    j = 2
    bol = True
    while True:
        if a == []:
            a.append(j)
            yield j
        else:
            for i in a:
                if j % i == 0:
                    bol = False
            if bol == False:
                j += 1
                bol = True
            else:
                a.append(j)
                yield j
                j += 1



print(list(itertools.takewhile(lambda x : x <= 100000, primes())))