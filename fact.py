def fact(n):
    if n == 1:
        return 1
#    else:
#        return n*fact(n-1)
#
#print(fact(1))
    elif n >= 2:
        num = 1
        for i in range(1, n+1):
            num *= i 
        return num 
print(fact(5))
