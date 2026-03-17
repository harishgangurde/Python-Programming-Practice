
class Demo:

    a = 50

    def __init__(self,x,y):
        print("Constructor")
        self.x = x
        self.y = y
    
    @classmethod
    def clasFun(cls):
        print("In class method")

    def instaFun(self):
        print("In instance method")


obj = Demo(10,20)

obj.clasFun()
obj.instaFun()
