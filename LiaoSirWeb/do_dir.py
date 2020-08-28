print(dir('ABC'))

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(getattr(obj,'z',404))