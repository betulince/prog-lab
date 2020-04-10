from sympy import Symbol,pprint
from sympy import factor,expand

print("Symbol example: ")
x = Symbol('x')
y = Symbol('y')
p = x*(x+x) #Symbol kütüphanesi olmasaydı x'in bir sayısal değeri olacaktı ve kendisiyle toplayıp,kendisiyle çarpacaktı.
print(p)
p = (x + 2)*(x + 3)
print(p)

print("expand() and factor() examples: ")
expr = x**2 - y**2
print("factor: "+str(factor(expr)))
factors = factor(expr)
print("expand: "+str(expand(factors)))
expand = expand(factors)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
print(factors)

expr = x**2 + 2*x*y + y**2
pprint(expr)
pprint(factors)

#printing a Series
x = Symbol('x')
series = x
n = 5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)

#Substituting in Values:
expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2})
print(res)

r = expr.subs({x:1-y})
print(r)

x = Symbol('x')
series = x
n = 5
x_value = 5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)
#Evaluate the series at x_value:
series_value = series.subs({x:x_value})
print(series_value)

