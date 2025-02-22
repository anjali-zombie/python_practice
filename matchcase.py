x=int(input("enter the value:"))

match x:

    case 0:
        print("zero")

    case 1:
        print("one")

    case _ if x!= 2:
        print(x, "is not 2")#if condition in switch case

    case _ if x!= 3:
        print(x," is not 3")

    case _:
        print("no match")

