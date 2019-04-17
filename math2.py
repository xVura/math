# acest script rezolva sisteme de ecuatii
# importa modulul de matematica

import math

a1 = float(input("Introdu coeficientul lui x din prima ecuatie: "))

b1 = float(input("Introdu coeficientul lui y din prima ecuatie: "))

c1 = float(input("Introdu termenul liber din prima ecuatie: "))

a2 = float(input("Introdu coeficientul lui x din a 2-a ecuatie: "))

b2 = float(input("Introdu coeficientul lui y din a 2-a ecuatie: "))

c2 = float(input("Introdu termenul liber din a 2-a ecuatie "))


# defineste x si y
x = (b2*c1 - b1*c2)/(b1*a2-a1*b2)

y = (-a1*x - c1)/b1

print('X este ' , end='')
print(x)

print('Y este ' , end='')
print(y)

# pastreaza programul deschis in consola
input ("Apasa pe orice tasta ca sa iesi")
