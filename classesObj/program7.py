
class Employee:

    def __new__(cls,*args,**kargs):
        
        print("Memory Allocation")
        return super().__new__(cls)

    def __init__(self,empId,empName):
        print("Constructor")
        self.empId = empId
        self.empName = empName

obj1 = Employee(10,"Kanha")
obj2 = Employee(15,"Ashish")

print(obj1.empId)
print(obj1.empName)

print(obj2.empId)
print(obj2.empName)


