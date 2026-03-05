
def fun(funcRef):
    funcRef()

def run():
    print("In run")

fun(run)
