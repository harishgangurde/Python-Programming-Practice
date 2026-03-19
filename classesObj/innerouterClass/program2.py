
class Outer:
    
    def __init__(self):
        print("Outer Constructor")

    class Inner:
        
        def __init__(self):
            print("Inner constructor")

        def innerFun(self):
            print("Inner instance method")

    def outerFun(self):
        print("outer instance method")

obj = Outer()
obj.outerFun()

obj2 = obj.Inner()
obj2.innerFun()
