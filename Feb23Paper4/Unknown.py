def Unknown(x, y):
    if x < y:
        print(x + y)
        return (Unknown(x+1, y)*2)
    else:
        if x == y:
            return 1 
        else:
            print (x+y)
            return (Unknown(x-1, y)//2)

Unknown(10, 15)
Unknown(10, 10)
Unknown(15, 10)
    

def IterativeUnknown(x, y):
    while x != y:
        if x < y:
            print(x + y)
            return (Unknown(x+1, y)*2)
        else:
            print(x + y)
            return (Unknown(x-1, y)//2)

    return 1

IterativeUnknown(10, 15)
IterativeUnknown(10, 10)
IterativeUnknown(15, 10)