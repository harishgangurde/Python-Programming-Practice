
for i in range(1,6+1):
    for j in range(3):
        if i%3==1:
            print("#",end=" ")
        elif i%3==2:
            print("$",end=" ")
        else:
            print("@",end=" ")
    print()
            
