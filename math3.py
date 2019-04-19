# acest script lasa utilizatorul sa introduca x si y si cu ele face un grafic
# ajutator pentru math4

# importa modulele necesare
import numpy as np
import matplotlib.pyplot as plt
import math
fig = plt.figure()


# momentan lasa utilizatorul sa introduca x si y
x = float(input("Introdu numarul x: "))
y = float(input("Introdu numarul y: "))


# stabileste daca axa este pozitiva sau negativa
if x > 0 and y > 0 :
    #x1 = np.linspace(x, math.inf)
    #y1 = np.linspace(y, math.inf)
    x1 = np.linspace(x, 0)
    y1 = np.linspace(y, 0)
if x < 0 and y < 0 :
    #x1 = np.linspace(-math.inf, x)
    #y1 = np.linspace(-math.inf, y)
    x1 = np.linspace(0, x)
    y1 = np.linspace(0, y)

# stabileste situatii intercalate
if x > 0 and y < 0 :
    #x1 = np.linspace(x, math.inf)
    #y1 = np.linspace(-math.inf, y)
    x1 = np.linspace(x, 0)
    y1 = np.linspace(0, y)
if x < 0 and y > 0 :
    #x1 = np.linspace(-math.inf, x)
    #y1 = np.linspace(y, math.inf)
    x1 = np.linspace(0, x)
    y1 = np.linspace(y, 0)


# trasarea propriu zisa
ax = plt.gca()
ax.plot(x1, y1)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.savefig("CenterOriginMatplotlib01.png")
plt.show()

# pastreaza programul deschis in consola
input ("Apasa pe orice tasta ca sa iesi: ")