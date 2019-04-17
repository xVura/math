import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()

x = np.linspace(1, 4)
y = np.linspace(2, 5)


ax = plt.gca()

ax.plot(x, y)
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.xlim(-np.pi,np.pi)

plt.savefig("CenterOriginMatplotlib01.png")
plt.show()