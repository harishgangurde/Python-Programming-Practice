
class Demo:

    x = 10

    def __new__(cls):
        print("In new method")
        return super().__new__(cls)

    def __init__(self):
        print("In init: Constructor")

    def disp(self):
        print("In disp")

obj = Demo()
print(obj.x)
obj.disp()
