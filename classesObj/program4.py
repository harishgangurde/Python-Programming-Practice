
class Player:
    team = "India"

    def __new__(cls):
        print("Memory Allocation")
        return super().__new__(cls)

    def __init__(self):
        self.playerName = "Virat"
        self.jerNo = 18
        print("Constructor")

obj = Player()
print(globals())
print("************************************************")
print(Player.__dict__)
print("************************************************")
print(obj.__dict__)
