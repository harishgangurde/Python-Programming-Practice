
x = 10

def fun():
    x = 20
    print("In fun")
    print("Local:",x)
    print("global:",globals()['x'])

print(x)
fun()
print(x)
