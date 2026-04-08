
x = 30

def fun():
    global x
    x = x + 1
    print("In fun")
    print("Fun:",x)

print(x)
fun()
print(x)
