ch = input("Enter R/G/B: ")

match ch.upper():
    case "R": print("Red")
    case "G": print("Green")
    case "B": print("Blue")
    case _: print("Invalid")
