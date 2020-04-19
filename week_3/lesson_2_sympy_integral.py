# E is the set of all grades possible between 11 and 12
# S is the set of all possible grades-that is all real numbers between 1 and 20.
# n(E) is infinite because it's impossible to ocunt all possible real numbers between 11 and 12.
# the same is true for n(S)
# Thus,we need a different approach to calculate the probability
"""
P(11<x<12) = n(E) / n(S)
A probability density function,P(x),expresses the probability of the value
of a random variable being close to x,an arbitrary value.

"""
from sympy import Symbol,exp,sqrt,pi,Integral
from sympy import pprint
x = Symbol('x')
p = exp (-(x-10)**2/2)/sqrt(2*pi)
#Integral(p ,(x , 11 , 12)).doit().evalf()
print(Integral(p , (x , 11 , 12)).doit().evalf())

