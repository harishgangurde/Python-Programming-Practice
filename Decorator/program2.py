
def outerFunc(funcRef):

    def innerFunc():
        print("Start inner Function")
        funcRef()
        print("End inner Function")

    return innerFunc

def run():
    print("In run")

retRef = outerFunc(run)
retRef()
