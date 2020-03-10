def my_h(list_1):
    my_d=dict() 
    for i in list_1:
        if i in my_d: 
            my_d[i]=my_d[i]+1
        else:
            my_d[i]=1
    return my_d 
list_1=[0,5,25,100,5,5,0,100]
my_h(list_1)


def lookup(d,v):
     for k in d:
        if d[k]== v:
            return k
    return -1


#We prevent repetitive variables with "known"
known={0:0,1:1} #a hash structure,global variable
def fibo_rec(n): #recursive
   # if n<2:
        #return n
    #else:
        #return fibo_rec(n-1)+fibo_rec(n-2)
    if n in known:
        return known[n]
    else:
        result=fibo_rec(n-1)+fibo_rec(n-2)
        known[n]=result
        return result


from sympy import FiniteSet 
from fractions import Fraction
s=FiniteSet(1,1.5,Fraction(1,5),1,1.5) 
for member in s:
    print(member)
t=FiniteSet(Fraction(1,5),1.5,1,1)
if s==t:
    print("True")


