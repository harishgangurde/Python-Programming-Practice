
class Demo:
     
    def __init__(self):
        print("In Constructor")
        self.x = 10
        self.y = 20

    def fun(self):
        print("In fun")
        print(self.x)
        print(self.y)

obj = Demo()

Demo.fun(obj)
