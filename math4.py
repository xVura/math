
import math
import numpy as np
import matplotlib.pyplot as plt

# afiseaza instructiuni de utilizare
print ("PUNCTUL DE INTERSECTIE AL GRAFICELOR A DOUA FUNCTII liniare")
print ("Pentru a realiza acest lucru, functia trebuie sa se afle in forma generala f(x)=ax+b", end='\n')
print ("Intersectia se gaseste egaland legile de corespondenta f(x) si g(x) si rezolvand ecuatia astfel obtinuta", end='\n')
print ("Ce ai de facut? Introduci, pe rand, coeficientul lui x si termenul liber din fiecare functie", end='\n')
print ("Se vor afisa coordonatele punctului de intersectie si reprezentarile graficelor functiilor in sistemul xOy", end='\n')

# se introduc coeficientii  
a1 = float(input("Introdu coeficientul lui x din f(x): "))
b1 = float(input("Introdu termenul liber din f(x): "))
a2 = float(input("Introdu coeficientul lui x din g(x): "))
b2 = float(input("Introdu termenul liber din g(x): "))

# se definesc variabilele
def f(x):
    return a1*x + b1
def g(x):
    return a2*x + b2

if a1 == a2:
    print ("Graficele celor doua functii reprezinta drepte paralele")

else:
    x1 = (b2-b1)/(a1-a2)
    # afiseaza rezultatul
    print ("Graficele functiilor se intersecteaza in punctul de coordonate: ", end= "\n")
    print ("(", x1, ", ", f(x1), ")", end='\n')

    # pune conditi pt capetele intervalelor
    if abs(x1) < 100:
        m1 = 100
        m2 = -100
    elif abs(x1) < 10000:
        m1 = 10000
        m2 = -10000
    else:
        m1 = 1000000
        m2 = -1000000

# atribuie intervale
A = np.linspace(m1, m2)
B1 = np.linspace(f(m1), f(m2))
B2 = np.linspace(g(m1), g(m2))

# traseaza graficul
ax = plt.gca()
ax.plot(A, B1)  #####  #####
ax.plot(A, B2)  #####  #####
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.savefig("Intersectie G 2 functii.png")
plt.show()

# pastreaza programul deschis in consola
input ("Apasa orice tasta pentru a iesi")