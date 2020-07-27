class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        sum = 0
        for elem in a:
            self.lst.append(elem)

        while len(self.lst) >= 5:
            for i in range(5):
                sum += self.lst[i]
            for i in range(5):
                del self.lst[0]
            print(sum)
            sum = 0


    def get_current_part(self):
        return self.lst

