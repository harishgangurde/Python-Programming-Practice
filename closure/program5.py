
def fun():
    x = 30
    print("Fun x:",x)

    def gun():
        nonlocal x
        x = x + 1
        print("Gun x:",x)

    def run():
        nonlocal x
        x = x + 1
        print("Run x:",x)


    return gun,run

retRef = fun()

for data in retRef:
    data()
