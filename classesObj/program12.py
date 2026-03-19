
class Demo:

    z = 30

    def __init__(self):
        self.x = 10
        self.y = 20

obj = Demo()

print(Demo.__dict__)
print("----------------------------------------------")
print(obj.__dict__)
print(Demo.z)

print(obj.x)
