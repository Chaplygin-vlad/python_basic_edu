class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        for i in a:
            self.lst.append(i)
        while len(self.lst) >= 5:
            print(sum(self.lst[:5]))
            self.lst = self.lst[5:]

    def get_current_part(self):
        return self.lst


a = Buffer()
a.add(1, 2, 3)

print(a.get_current_part())
a.add(4, 5, 6)
print(a.get_current_part())
a.add(7, 8, 9, 10)
print(a.get_current_part())
a.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(a.get_current_part())
