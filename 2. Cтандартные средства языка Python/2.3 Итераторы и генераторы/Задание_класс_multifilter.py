class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True

    def judge_any(pos, neg):
        if pos >= 1:
            return True

    def judge_all(pos, neg):
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge = judge_any):
        q = []
        self.iterable = iterable
        self.judge = judge
        for i in funcs:
            q.append(i)
        self.funcs = q


    def __iter__(self):
        pos = 0
        neg = 0
        for el in self.iterable:

            for elem in self.funcs:

                if elem(el) == True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el
            pos = 0
            neg = 0


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(a)

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))


