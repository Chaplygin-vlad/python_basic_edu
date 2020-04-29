import time


class Loggable:

    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


# создаем класс, который наследует класс "list" и класс "Loggable"
class LoggableList(list, Loggable):
    def append(self, elem):
        # метод super супер позволяет вызвать функцию у прямого потомка
        super(LoggableList, self).append(elem)
        super(LoggableList, self).log(str(elem))


a = LoggableList()
a.append(1)
print(a)
