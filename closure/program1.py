
x = 10
def fun():
    x = 30
    print("Fun x:",x)

    def gun():
        print("Gun x:",x)

    return gun

retRef = fun()
retRef()
print(x)
