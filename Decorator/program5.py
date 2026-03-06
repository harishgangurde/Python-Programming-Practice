
def decorFun1(funRef1):

    def innerFun1():
        print("Start decoration 1")
        funRef1()
        print("End decoration 1")

    return innerFun1


def decorFun2(funRef2):

    def innerFun2():
        print("Start decoration 2")
        funRef2()
        print("End decoration 2")

    return innerFun2

@decorFun1
@decorFun2

def fun():
    print("In fun")

fun = decorFun1(decorFun2(fun))
fun()

