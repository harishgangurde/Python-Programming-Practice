
class Demo:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.__z = 30

obj = Demo()

#Name Mangling
print(obj.__dict__)

print(obj.x)
print(obj.y)
print(obj.__z)
