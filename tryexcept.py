num = int(input("enter number:"))

try:
    li =[1,2,3,4]
    i =int(input("enter index:"))
    print(li[i])
except:
    print("invalid data type")
finally:# this always executed no matter what it mainly used when try and except used in a function and return some value
    print("finished")


