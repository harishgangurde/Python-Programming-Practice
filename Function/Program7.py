
#Keywords var args

def fun(**data):
    for i,j in data.items():
        print(i,":",j)

fun(jerNo=45)
fun(jerNo=45,run = 7, pName = "Hardik")
