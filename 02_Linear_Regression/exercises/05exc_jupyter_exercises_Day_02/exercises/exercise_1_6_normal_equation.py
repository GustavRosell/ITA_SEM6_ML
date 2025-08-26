import matplotlib.pyplot as plt
import numpy as np

# Generer data: y = 4 + 3*x + støj
X = 2 * np.random.rand(50, 1)
y = 4 + 3 * X + np.random.randn(50, 1)

# Normal equation: θ = (X^T X)^(-1) X^T y
X_b = np.c_[np.ones((50, 1)), X]  # Tilføj bias kolonne
parametre = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)

a = parametre[0, 0]  # skæringspunkt
b = parametre[1, 0]  # hældning

print(f"Normal equation resultater: a = {a:.6f}, b = {b:.6f}")

# Vis resultat
X_linje = np.array([[0], [2]])
y_forudsigelse = a + b * X_linje

plt.plot(X, y, "g.", label="Datapunkter")
plt.plot(X_linje, y_forudsigelse, "r-", label=f"Normal equation: y = {a:.2f} + {b:.2f}x")
plt.axis([0, 2, 0, 15])
plt.legend()
plt.show()