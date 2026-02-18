

day = input("Enter Day: ")

match day :

    case "Mon" :
        print("Start of the week")

    case "Fri" :
        print("Weekend is coming...")

    case "Sat" :
        print("Weekend Started")

    case "Sun" :
        print("Relax, its sunday")

    case _:
        print("Weekday")
