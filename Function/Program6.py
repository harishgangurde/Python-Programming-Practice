
#Variable length argument:

def fun(*data):
    for i in data:
        print(i)

fun()
fun(10)
fun(10,20)
