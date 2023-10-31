'''
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print(factorial())
'''
'''
def countdown(p):
    while p > 0:
        print(p)
        p=p-1

countdown(20)
'''
def countdown(h):
    if h>=1:
        print(h)
        countdown(h-1)

countdown(20)

    
