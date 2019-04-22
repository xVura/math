
import math
import numpy as np
import matplotlib.pyplot as plt

print("INTERSECTIA REPREZENTARII GRAFICE A UNEI FUNCTII LINIARE CU AXELE DE COORDONATE", end='\n')

# defineste variabilele necesare pt calcul
a = float(input("Introdu coeficientul lui x: "))
b = float(input("Introdu termenul liber: "))
m = -b/a
aria = abs(-b**2/a)
h = abs((-b**2/a)/(b**2-b**2/a**2))

# defineste functia
def f(x):
  return a*x+b

# transforma intervale in segmente
A = np.linspace (m, 0)
B = np.linspace (0, b)
C = np.linspace (100, -100)
D = np.linspace (f(100), f(-100))

# afiseaza coordonatele punctelor determinate de intersectiile cu sistemul ortogonal de axe
print("Graficul functiei f(x) intersecteaza axa Ox in punctul: ")
print ("(", m, ", ", 0, ")", end='\n')
print ("Graficul functiei f(x) intersecteaza axa Oy in punctul: ")
print ("(", 0, ", ", b, ")", end='\n')
print ("Aria triunghiului: ", aria, " u^2")
print ("d(O; Gf): ", h, "u")

# traseaza graficul
ax = plt.gca()
ax.plot(C, D) ##### #####
ax.plot(A, B) ##### #####
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.savefig("Graficul unei functii.png")
plt.show()

# pastreaza programul deschis in consola
input ("Apasa orice tasta pentru a iesi")