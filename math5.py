# acest script determina intersectia unei functii liniare cu axele de coordonate si o reprezinta

import math
import numpy as np
import matplotlib.pyplot as plt

# defineste variabilele
a = float(input("Introdu coeficientul lui x: "))
b = float(input("Introdu termenul liber: "))
x = -b/a

# afiseaza coordonatele punctelor determinate de intersectiile cu sistemul ortogonal de axe
print ("Graficul functiei f(x) intersecteaza axa Ox in punctul: ")
print ("(", end="")
print(x, end="")
print('; ', end="")
print("0)")
print ("Graficul functiei f(x) intersecteaza axa Oy in punctul: ")
print ("(", end="")
print(0, end="")
print('; ', end="")
print(b, end="")
print(")")

# punctele pana la care se traseaza graficul
A = np.linspace(x, 0)
B = np.linspace(0, b)

# Trasarea propriu zisa
ax = plt.gca()
ax.plot(A, B)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.savefig("CenterOriginMatplotlib01.png")
plt.show()

# pastreaza programul deschis in consola
input ("Apasa pe orice tasta ca sa iesi: ")