import matplotlib.pyplot as plt
import numpy as np

# Generer kvadratisk data: y = 0.5*x² + x + 2 + støj
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X * X + X + 2 + np.random.randn(100, 1)

# Vis oprindelige datapunkter
plt.plot(X, y, "g.", label="Datapunkter")
plt.axis([-3, 3, 0, 10])

# Lav polynomielle features manuelt: [x, x²]
X_poly = np.c_[X, X**2]

# Brug normal equation til at finde parametre
X_b = np.c_[np.ones((100, 1)), X_poly]  # Tilføj bias kolonne
parametre = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)

a = parametre[0, 0]  # konstant term
b = parametre[1, 0]  # x koefficient
c = parametre[2, 0]  # x² koefficient

# Lav forudsigelser for glat kurve
X_plot = np.linspace(-3, 3, 300).reshape(-1, 1)
y_plot = a + b * X_plot + c * X_plot**2

plt.plot(X_plot, y_plot, "b-", label=f"Polynomial fit")
plt.legend()
plt.show()

print(f"Parametre: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
print(f"Model: y = {a:.4f} + {b:.4f}*x + {c:.4f}*x²")