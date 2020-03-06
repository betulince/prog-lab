#How to Implement Power Function in Python:

#1:find the power of a number using recursion
def power_recursive(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        if b%2==0:
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)*a

#2:find the power of a number using recursion/second method 
def power_rec(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    if b>1:
        return power(a,b-1)*a #power(a*a,b/2)


#3:use a for loop to create a power function
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        t=1
        for i in range(b):
            t=t*a
        return t;


~                        
