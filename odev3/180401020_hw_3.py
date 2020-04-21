"""
UNIFORM DISTRIBUTION
Uniform Distribution(Tekdüze Dağılım) , belirli sınırlar arasındaki keyfi bir sonucun olduğu bir deneyi açıklar.
Sınırlar minimum ve maksimum değerler olan a ve b parametreleri tarafından tanımlanır.Aralık kapalı veya açık olabilir.
Sınırlar arasındaki fark aralık uzunluğunu tanımlar.Dağıtımın desteğindeki aynı uzunluktaki tüm aralıklar eşit dercede olasıdır.
[a,b] aralığında sürekli düzgün dağılım için olasılık yoğunluk fonksiyonu(probability density function) :
        1/b-a  for a<=x<=b
f(x) =
         0     for x<a or x>b
Görüldüğü üzere,uniform distribution sabit olasılıklı bir dağılımdır

"""
import sympy as sym
from sympy import Symbol,Piecewise
import sympy.plotting as syp
import matplotlib.pyplot as plt
import numpy as np

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
my_uni_dist_func = 1/(b-a)

def uniform_distribution_with_sympy():
    while True :
        n = int(input("enter the min value: ")) # n : lower
        v = int(input("enter the max value: ")) # v : upper
        if n>v: # lower > upper ise 1/(b-a) fonksiyonunun değeri negatif olur böyle bir durumda grafiği çizmemeli.
            print("you have entered values with wrong properties")
            continue
        else: # lower ve upper (n ve v) değerleri uygun girildiyse syp.plot ile grafiği çizdiriyor.
            syp.plot(Piecewise((0, (x < n) | (x > v)), (my_uni_dist_func.subs({a: n, b: v}), (x >= n) & (x <= v))),
                     (x, -10, 10), title="uniform distribution")
            # Piecewise,parçalı tanımlanmış fonksiyonlar için kullanılır.
        break
uniform_distribution_with_sympy() # fonksiyon çağrısı

def uniform_distribution_with_matplotlib():
    while True:
        lower = int(input("enter the min value: ")) 
        upper = int(input("enter the max value: "))
        if lower > upper:
            print("you have entered values with wrong properties...")
            continue
        else:
            x_values = [] # x eksenini oluşturan değerlerin listesi
            y_values = [] # y eksenini oluşturan değerlerin listesi
            for value in np.arange(-10,30,0.1): # grafiğin tekdüze dağılım grafiğine daha yakın olabilmesi için value'nun artış değerini olabildiğince azalttım.
                if lower<=value and upper>=value: # eğer value değeri benim girdiğim değerler arasında ise:
                    y = my_uni_dist_func.subs({a:lower, b:upper ,x:value}).evalf()
                    y_values.append(y)
                    x_values.append(value)
                else: # eğer value değeri girdiğim lower ve upper değerleri arasında değilse y ekseninde hep 0 değerini alıyor.
                    y_values.append(0)
                    x_values.append(float(value))
            plt.plot(x_values,y_values)
            plt.show()
        break
uniform_distribution_with_matplotlib() # fonksiyon çağrısı
