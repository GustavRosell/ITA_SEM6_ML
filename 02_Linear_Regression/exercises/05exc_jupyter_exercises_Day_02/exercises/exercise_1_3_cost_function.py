import numpy as np
import matplotlib.pyplot as plt

def kostfunktion(a, b, X, y):
    # Beregn kostfunktionen (Mean Square Error)
    m = len(y)
    error = a + b*X - y
    J = np.sum(error ** 2)/(2*m)
    return J

# Generer data: y = 4 + 3*x + støj
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Definer intervaller for parametre
a_interval = np.arange(1, 10, 0.05)
b_interval = np.arange(0.5, 5, 0.05)

# Find bedste parametre
lavest_kost = kostfunktion(0, 0, X, y)
bedste_a = 0
bedste_b = 0

for a in a_interval:
    for b in b_interval:
        nuværende_kost = kostfunktion(a, b, X, y)
        if nuværende_kost < lavest_kost:
            lavest_kost = nuværende_kost
            bedste_a = a
            bedste_b = b

print(f"Bedste a (skæringspunkt): {bedste_a:.6f}, Bedste b (hældning): {bedste_b:.6f}")
print(f"Minimum kostfunktion: {lavest_kost:.6f}")

# Vis datapunkter og bedste linje
plt.plot(X, y, "b.", label="Datapunkter")
X_linje = np.array([[0], [2]])
y_linje = bedste_a + bedste_b * X_linje
plt.plot(X_linje, y_linje, "r-", label=f"Bedste linje: y = {bedste_a:.2f} + {bedste_b:.2f}x")
plt.axis([0, 2, 0, 15])
plt.legend()
plt.show()