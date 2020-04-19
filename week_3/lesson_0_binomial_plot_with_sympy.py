import sympy as sym
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plt

p = Symbol('p')
x = Symbol('x')
n = Symbol('n')
my_function_3_part_0 = sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
#pprint(my_function_3_part_0)

my_function_3_part_1 = p**x
#pprint(my_function_3_part_1)

my_function_3_part_2 = (1-p)**(n-x)
#pprint(my_function_3_part_2)

my_function_3 = my_function_3_part_0 * my_function_3_part_1 * my_function_3_part_2
pprint(my_function_3)

sym.plot(my_function_3.subs( {p:0.5 , n:50} ) , (x,0,50) , title = "binomial distribution plot for n = 50")

x_values = []
y_values = []
for value in range (50):
    y = my_function_3.subs( {p:0.5 , n:50  , x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)
plt.plot(x_values,y_values)
plt.show()
