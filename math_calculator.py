# calculator v1.0

# importa module
import math
from math import sqrt as sqrt
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# ruleaza functia pana utilizatorul o inchide
while True:
    print ("Apasa Enter pentru a vedea optiunile")
    input()
    cls () # curata ce s-a afisat inainte

    # afiseaza optiunile
    print ("Optiuni:")
    print ("Introdu '+' ca sa aduni 2 nr")
    print ("Introdu '-' ca sa scazi 2 nr")
    print ("Introdu '*' ca sa inmultesti 2 nr")
    print ("Introdu '/' ca sa imparti 2 nr")
    print ("Introdu '^' ca sa ridici un nr la o putere")
    print ("Introdu 'rad' ca sa extragi radacina patrata dintr-un nr")
    print ("Introdu 'q' ca sa iesi")
    op_introd = input(": ")

# curata ce s-a afisat inainte
    cls()

    try:
        # optiune de iesire
        if op_introd == "q":
            break
    
        # adunare
        elif op_introd == "+":
            print ("Introdu cele 2 nr: ")
            a = float(input("I nr: "))
            b = float(input("II nr: "))
            rezultat = a+b
            print ("Rezultatul este: ", rezultat )
    
        # scadere
        elif op_introd == "-":
            print ("Introdu cele 2 nr: ")
            a = float(input("I nr: "))
            b = float(input("II nr: "))
            rezultat = a-b
            print ("Rezultatul este: ", rezultat )
        
        # inmultire
        elif op_introd == "*":
            print ("Introdu cele 2 nr: ")
            a = float(input("I nr: "))
            b = float(input("II nr: "))
            rezultat = a*b
            print ("Rezultatul este: ", rezultat )

        # impartire
        elif op_introd == "/":
            try:
                print ("Introdu cele 2 nr: ")
                a = float(input("I nr: "))
                b = float(input("II nr: "))
                rezultat = a/b
                print ("Rezultatul este: ", rezultat )

            # daca impartitorul e 0
            except ZeroDivisionError:
                print ("Eroare la impartirea la zero")

        # ridicare la putere
        elif op_introd == "^":
            print ("Introdu cele baza si exponentul: ")
            a = float(input("baza: "))
            b = float(input("exponentul: "))
            rezultat = a**b
            print ("Rezultatul este: ", rezultat )

        # radacina patrata*
        elif op_introd == "rad":
            a = float(input("Introdu nr de la care doresti radacina patrata:"))
            rezultat = sqrt(a)
            print ("Rezultatul este: ", rezultat )

        # daca ce e introdus nu se afla in optiuni
        else:
           print ("Operatie necunoscuta") 
    
    # daca nu se introduc valori "float"
    except TypeError:
        print ("Numerele introduse sunt invalide")
    
# *daca nr e negativ se afiseaza ca la exceptia TypeError