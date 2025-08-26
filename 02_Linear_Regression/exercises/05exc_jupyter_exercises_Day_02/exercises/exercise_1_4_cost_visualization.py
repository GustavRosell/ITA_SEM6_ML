import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def kostfunktion(a, b):
    # Beregn kostfunktionen for givne parametre
    m = len(Ydots)
    error = a + b*Xdots - Ydots
    J = np.sum(error ** 2)/(2*m)
    return J

# Generer data: y = -5 + 7*x + støj  
Xdots = 2 * np.random.rand(100, 1)
Ydots = -5 + 7 * Xdots + np.random.randn(100, 1)

# Lav 3D plot af kostfunktionen
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definer parameterområde
a_interval = np.arange(-10, 10, 0.05)
b_interval = np.arange(-10, 10, 0.05)

# Beregn kostfunktion for alle kombinationer
A, B = np.meshgrid(a_interval, b_interval)
zs = np.array([kostfunktion(a, b) for a, b in zip(np.ravel(A), np.ravel(B))])
Z = zs.reshape(A.shape)

# Vis 3D overfladen
ax.plot_surface(A, B, Z)
ax.set_xlabel('a (skæringspunkt)')
ax.set_ylabel('b (hældning)')
ax.set_zlabel('Kostfunktion')
plt.show()