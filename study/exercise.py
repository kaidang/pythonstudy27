# coding:utf-8

nestlist = [[1,2],[3,4],[5,6]]
def flatten(nested):
    for sublist in nested:
        for subsublist in sublist:
            yield subsublist

yy = flatten(nestlist)

for num in yy:
    print num

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()


for f in fibs:
    if f > 1000:
        print f
        break

class Testiter:
    def __init__(self):
        self.a = 1
        self.b = 0
    def next(self):
        self.a += 1
        self.b = self.a**2
        return self.b
    def __iter__(self):
        return self


newtest = Testiter()

for x in newtest:
    if x > 10000:
        print x

