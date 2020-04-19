#from sympy import Symbol,Limit
from sympy import *
t = Symbol('t')
St = 5*t**2 + 2*t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St1 = St.subs({t : t1})
St1_delta = St.subs({t:t1 + delta_t})

#Limit((St1_delta-St1)/delta_t , delta_t ,0).doit()
"""
doit() : using the doit() method in sympy module,we can evaluate objects that are not
evaluated by default like limits,integrals,sums and products.All objects of this kind 
will be evalueated recursively.
"""
print(limit((St1_delta-St1)/delta_t , delta_t ,0).doit())

#another example:

x = Symbol('x')
my_limit_material = sin(x)/x;
print("equation that i want to find its derivative {}".format(my_limit_material))
my_limit = limit(my_limit_material,x,0) #get the derivative by x.
print("outcome is: {}".format(my_limit))

