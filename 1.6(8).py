class ExtendedStack(list):

    def append(self, elem):
        super(ExtendedStack, self).append(elem)

    def pop(self):
        super(ExtendedStack, self).pop(-1)

    def sum(self):
        a = self[-1]
        super(ExtendedStack, self).pop(-1)
        b = self[-1]
        super(ExtendedStack, self).pop(-1)
        super(ExtendedStack, self).append(a+b)

    def sub(self):
        a = self[-1]
        super(ExtendedStack, self).pop(-1)
        b = self[-1]
        super(ExtendedStack, self).pop(-1)
        super(ExtendedStack, self).append(a-b)

    def mul(self):
        a = self[-1]
        super(ExtendedStack, self).pop(-1)
        b = self[-1]
        super(ExtendedStack, self).pop(-1)
        super(ExtendedStack, self).append(a*b)

    def div(self):
        a = self[-1]
        super(ExtendedStack, self).pop(-1)
        b = self[-1]
        super(ExtendedStack, self).pop(-1)
        super(ExtendedStack, self).append(a//b)



a = ExtendedStack()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
print(a)
a.sum()
print(a)