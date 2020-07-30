class LoggableList(list, Loggable):
    def append(self, strok):
        y = super(LoggableList, self).append(strok)
        self.log(strok)
        return y

