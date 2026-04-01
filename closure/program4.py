
def fun():
    x = 10
    print(hex(id(x)))
    print("fun x:",x)

    def gun():
        x = 20
        print("gun x:",x)

    return gun

retRef = fun()
retRef()
print(retRef.__closure__)
