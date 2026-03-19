
class Outer:

    def __init__(self):
        print("Outer Constructor")

    class Inner:

        def __init__(self):
            print("Inner constructor")

Outer().Inner()
