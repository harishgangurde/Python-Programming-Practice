
class DemoChild1 :
    def __init__(self):
        super().__init__()
        print("DemoChild1 Constructor")
        self.y = 10

class DemoChild2 :
    def __init__(self):
        super().__init__()
        print("DemoChild2 Constructor")
        self.z = 20

class Demo(DemoChild1, DemoChild2):
    def __init__(self):
        super().__init__()
        print("Demo Constructor")

obj = Demo()
print(obj.y)
print(obj.z)
