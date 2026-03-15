
class Demo:

    def __new__(cls):
        print("Memory Allocation")
        return super().__new__(cls)

    def __init__(self):
        print("Constructor")

obj = Demo()


#obj = __new__(Demo)          memory allocation
#__init__(obj)                instance variable Initialization
