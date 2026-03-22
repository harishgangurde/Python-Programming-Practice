
#Method Overloading

class Demo:
    def __init__(self):
        print("Demo Constructor")

    def disp(self,x,y):
        print("First Display")

    def disp(self,*arg):
        print("Second Display")

obj = Demo()
obj.disp(10)
obj.disp(20,30)

#Python chya class madhe same same navache method exist karu shakat nhi mahanun python madhe method overloading hot nhi
