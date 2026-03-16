
class Player:

    team = "India"

    def __new__(cls,*args,**kargs):
        print("Memory Allocation")
        return super().__new__(cls)

    def __init__(self,playerName,jerNo):
        print("In Constructor")
        print(self)
        self.playerName = playerName
        self.jerNo = jerNo

obj1 = Player("Virat",18)
print(obj1.playerName)

obj2 = Player("Rohit",45)
print(obj2.playerName)

obj3 = Player("Max",3)
print(obj3.playerName)

