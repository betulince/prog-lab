from sympy import FiniteSet
FiniteSet(1,2,3) #üç elemanlı bir küme oluşuyor.
#intersect,union,**2
t=FiniteSet(1,2,3)
s=FiniteSet(2,4,6)
t==s
t.union(s)
t.intersect(s)
t**2


def probability(space,event): #TT,TF,FT,FF tf ft event,tt ff space
    return len(event)/len(space)


def check_prime(number): #10 için false,1 için false,7 girersen asal olduğu için true döner.
    if number!=1:
        for factor in range(2,number):
            if number%factor==0:
                return False
    else: # ==1 durumu
        return False
    return True
check_prime(73)



from sympy import FiniteSet
space=FiniteSet(*range(1,21)) 
primes=[] 
for num in space: 
    if check_prime(num):
        primes.append(num)
event=FiniteSet(*primes)
p=probability(space,event)
print(p)


