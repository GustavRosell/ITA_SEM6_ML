import numpy as np
import matplotlib.pyplot as plt

# Generer data: y = 4 + 3*x + støj
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Lineær regression via normal equation
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Tilføj bias kolonne
params = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)

a = float(params[0, 0])  # skæringspunkt  
b = float(params[1, 0])  # hældning

# Lav forudsigelser for plotting
X_linje = np.linspace(0, 2, 100).reshape(-1, 1)
y_linje = a + b * X_linje

# Vis datapunkter og tilpasset linje
plt.plot(X, y, "b.", label="Datapunkter")
plt.plot(X_linje, y_linje, "r", linewidth=2, 
         label=f"Tilpasset linje: y = {a:.2f} + {b:.2f}x")
plt.axis([0, 2, 0, 15])
plt.legend()
plt.title("Lineær regression med normal equation")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

print(f"Fundne parametre: a = {a:.6f}, b = {b:.6f}")
print(f"Sande parametre: a = 4.0, b = 3.0")