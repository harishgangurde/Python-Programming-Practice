

def decorFun(funRef):

    def innerFun(*args,**kwargs):
        print("Start decoration")
        funRef(*args,**kwargs)
        print("End decoration")

    return innerFun

@decorFun
def add(x,y):
    print("x :",x)
    print("y :",y)
    print("add :",x+y)

add(10,20)
