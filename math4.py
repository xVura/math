# acest script calculeaza punctul de intersectie al graficelor a doua functii

import math

# afiseaza instructiuni de utilizare
print ("PUNCTUL DE INTERSECTIE AL GRAFICELOR A DOUA FUNCTII")
print ("Pentru a realiza acest lucru, functia trebuie sa se afle in forma generala f(x)=ax+b", end='\n')
print ("Programul de calcul gaseste intersectia egaland legile de corespondenta f(x) si g(x) si rezolvand ecuatia astfel obtinuta", end='\n')
print ("Ce ai de facut? Introduci, pe rand, coeficientul lui x si termenul liber din fiecare functie", end='\n')

# se introduc coeficientii  
a1 = float(input("Introdu coeficientul lui x din f(x): "))
b1 = float(input("Introdu termenul liber din f(x): "))
a2 = float(input("Introdu coeficientul lui x din g(x): "))
b2 = float(input("Introdu termenul liber din g(x): "))

# se determina variabilele x si f(x) sau g(x)
x = (b2-b1)/(a1-a2)
y = a1*x + b1

# afiseaza rezultatul
print ("Graficele functiilor se intersecteaza in punctul de coordonate: ", end= "\n")
print ("(", x, ", ", y, ")", end='\n')

# pastreaza programul deschis
input ("Apasa pe orice tasta ca sa iesi")