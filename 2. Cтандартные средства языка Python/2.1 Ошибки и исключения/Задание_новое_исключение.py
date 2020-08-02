class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, stroka):
        if type(stroka) == int:
            if stroka > 0:
                y = super(PositiveList, self).append(stroka)
                return y
            else:
                raise NonPositiveError
        else:
            y = super(PositiveList, self).append(stroka)
            return y

