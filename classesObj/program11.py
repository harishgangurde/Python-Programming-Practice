
class Demo:

    x = 10
    y = 20

    def __init__(self):
        self.a = 50
        self.b = 80

    @classmethod
    def fun(cls):
        print("In class method")
        print(cls.x)
        print(cls.y)

    def run(self):
        print("In instance method")
        print(self.a)
        print(self.b)

Demo.fun()

obj = Demo()
Demo.run(obj)
