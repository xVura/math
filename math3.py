# ACEST SCRIPT TRASEAZA INTERSECTIA GRAFICULUI FUNCTIEI CU AXA OX SI OY

# Importa modulele necesare
import numpy as np
import matplotlib.pyplot as plt
import math
fig = plt.figure()


# Momentan lasa utilizatorul sa introduca x si y
x = float(input("Introdu numarul x: "))
y = float(input("Introdu numarul y: "))


# Stabileste daca axa este pozitiva sau negativa
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

# Stabileste situatii intercalate
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


# Trasarea propriu zisa
ax = plt.gca()
ax.plot(x1, y1)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
def extended(ax, x, y, **args):

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    x_ext = np.linspace(xlim[0], xlim[1], 100)
    p = np.polyfit(x, y , deg=1)
    y_ext = np.poly1d(p)(x_ext)
    ax.plot(x_ext, y_ext, **args)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax

plt.savefig("CenterOriginMatplotlib01.png")
plt.show()