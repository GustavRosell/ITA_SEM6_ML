import matplotlib.pyplot as plt
import numpy as np

def lineær_regression(X, y, a=0, b=0, epoker=1000, læringsrate=0.01):
    # Gradient descent algoritme
    N = float(len(y))
    
    for i in range(epoker):
        # Beregn forudsigelser
        y_forudsigelse = a + b * X
        
        # Beregn gradienter
        a_gradient = -(2/N) * np.sum(y - y_forudsigelse)
        b_gradient = -(2/N) * np.sum(X * (y - y_forudsigelse))
        
        # Opdater parametre
        a = a - (læringsrate * a_gradient)
        b = b - (læringsrate * b_gradient)
    
    return a, b

# Generer data: y = 4 + 3*x + støj
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Find parametre med gradient descent
a, b = lineær_regression(X, y)

print(f"Fundne parametre: a = {a:.6f}, b = {b:.6f}")

# Vis resultat
plt.plot(X, y, "b.", label="Datapunkter")
X_linje = np.array([[0], [2]])
y_forudsigelse = a + b * X_linje
plt.plot(X_linje, y_forudsigelse, "r-", label=f"Tilpasset linje: y = {a:.2f} + {b:.2f}x")
plt.axis([0, 2, 0, 15])
plt.legend()
plt.show()