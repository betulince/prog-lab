import sympy as sym
from sympy import Symbol
from sympy import pprint
import sympy.plotting as syp


sigma = Symbol('sigma')
x = Symbol('x')
mu = Symbol('mu')

pprint(2*sym.pi*sigma)
print(2*sym.pi*sigma)

print(sym.sqrt(2*sym.pi*sigma))
pprint(1/(sym.sqrt(2*sym.pi*sigma**2)))

#Gauss Dağılım Fonksiyonu
part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)**2/(2*sigma**2)))
my_gauss_function = part_1 * part_2
print("my gauss function is: ")
pprint(my_gauss_function)

syp.plot(my_gauss_function.subs({mu:10,sigma:30}),(x , -100 , 100),title = 'gauss distribution')

x_values = []
y_values = []
for value in range(-50,50):
    y = my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

plt.plot(x_values,y_values)
plt.show()


