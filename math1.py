# rezolva o ecuatie de tipul ax**2 + bx + c = 0



# importa modulul de matematica
import math
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

a = float(input("Introdu numarul a: "))
b = float(input("Introdu numarul b: "))
c = float(input("Introdu numarul c: "))

# calculeaza discriminantul
d = (b**2) - (4*a*c)

# gaseste cele 2 solutii 
x1 = (-b - d) / (2 * a)
x2 = (-b + d) / (2 * a)

# variabila pentru cea mai mare valoare
mare = -d/(4*a)
mica = -d/(4*a)

# variabila pentru a
x=-b/(2*a)

# curata ce s-a afisat inainte
cls()

# printeaza discriminantul
print(d)

# printeaza valorile 
if x1 == x2 :
    print('x1=x2=', end = '') 
    print(x1)
    
else :
    print('Solutia este {0} si {1}'.format(x1,x2))
    
if a < 0 :
    print("Cea mai mare valoare este : ", end = '')
    print(mare, end ='')
    print(' pentru x = ', end ='')
    print(x)
    
if a > 0 :
    print("Cea mai mica valoare este : ", end = '')
    print(mica, end ='')
    print(' pentru x = ', end ='')
    print(x)

    




