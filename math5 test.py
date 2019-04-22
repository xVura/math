
# importa librariile necesare
import math
import numpy as np
import matplotlib.pyplot as plt

# defineste variabilele necesare pt calcul
a = float(input("Introdu coeficientul lui x: "))
b = float(input("Introdu termenul liber: "))
m = -b/a

# defineste functia
def f(x):
  return a*x+b

# defineste variabilele necesare pt grafic
# defineste variabilele folosite pt |b|<100*
x1 = 100
x2 = f(100)
y1 = -100
y2 = f(-100)

# transforma intervale in "puncte"
A = np.linspace (m, 0)
B = np.linspace (0, b)
C = np.linspace (x1, y1)
D = np.linspace (x2, y2)
<<<<<<< HEAD

=======
E = np.linspace (z1, t1)
F = np.linspace (z2, t2)
G = np.linspace (g1, h1)
H = np.linspace (g2, h2)
>>>>>>> ea05e04b304ce1a995f82fe5b36dbe56f05281da
# afiseaza coordonatele punctelor determinate de intersectiile cu sistemul ortogonal de axe
print ("Graficul functiei f(x) intersecteaza axa Ox in punctul: ")
print ("(", end="")
print(m, end="")
print('; ', end="")
print("0)")
print ("Graficul functiei f(x) intersecteaza axa Oy in punctul: ")
print ("(", end="")
print(0, end="")
print('; ', end="")
print(b, end="")
print(")")

# traseaza graficul
ax = plt.gca()

<<<<<<< HEAD
ax.plot(C, D)
ax.plot(A, B)

=======
if abs(b) < 100:
    ax.plot(C, D)

elif abs(b) < 10000:
    ax.plot(E, F)

else:
    ax.plot(G, H)
ax.plot(A,B)
>>>>>>> ea05e04b304ce1a995f82fe5b36dbe56f05281da
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.savefig("Graficul unei functii.png")
plt.show()
