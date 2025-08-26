import numpy as np
import matplotlib.pyplot as plt

# Generer data: y = 4 + 3*x + støj
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Normal equation: θ = (X^T X)^(-1) X^T y
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Tilføj bias kolonne
params = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)

a = float(params[0, 0])  # skæringspunkt
b = float(params[1, 0])  # hældning

# Lav linje til plotting
X_linje = np.linspace(0, 2, 100).reshape(-1, 1)
y_linje = a + b * X_linje

# Vis resultat
plt.scatter(X, y, color="green", s=25, label="Datapunkter")
plt.plot(X_linje, y_linje, color="black", linewidth=2, 
         label=f"Tilpasset linje: y = {a:.2f} + {b:.2f}x")
plt.title("Lineær regression med normal equation")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()