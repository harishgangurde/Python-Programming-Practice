
def decorFun(funRef):

    def innerFun():
        print("Buying shoes")
        print("Buying bag")
        funRef()

    return innerFun

@decorFun
def fun():
    print("GYM")

fun()
