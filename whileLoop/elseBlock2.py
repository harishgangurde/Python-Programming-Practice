
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))

while x<=y :
    x += 1
    if x % 5 == 0:
        continue
    print(x)
else:
    print("In else block")
    print(x)
