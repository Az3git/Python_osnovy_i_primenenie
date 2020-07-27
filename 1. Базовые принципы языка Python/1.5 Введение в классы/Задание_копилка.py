class MoneyBox:
    def __init__(self, capacity):
        self.volume = capacity
        self.money = 0

    def can_add(self, v):
        if self.money + v > self.volume:
            return False
        else:
            return True

    def add(self, v):
        self.money += v

cop1 = MoneyBox(100)
cop1.add(20)
cop1.can_add(20)
print(cop1.can_add(20))
cop1.add(20)
cop1.can_add(20)
print(cop1.can_add(20))
cop1.add(20)
cop1.can_add(20)
print(cop1.can_add(20))
cop1.add(20)
cop1.can_add(20)
print(cop1.can_add(20))
cop1.add(20)
cop1.can_add(20)
print(cop1.can_add(20))
cop1.add(20)