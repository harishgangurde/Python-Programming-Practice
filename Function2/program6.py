
x = 10

def fun():
    x = 20
    print("Fun:",x)

    def gun():
        nonlocal x
        x = x + 1
        print("gun x:",x)

    return gun

print(x)
retVal = fun()
retVal()
print(x)
