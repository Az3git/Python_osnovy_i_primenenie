class ExtendedStack(list):
    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        summa = top1 + top2
        self.append(summa)

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        suba = top1 - top2
        self.append(suba)

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        mula = top1*top2
        self.append(mula)

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        diva = top1//top2
        self.append(diva)



