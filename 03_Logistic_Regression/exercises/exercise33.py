import matplotlib.pyplot as plt
import numpy as np

# Generer simpel datasæt
np.random.seed(42)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Sigmoid funktion
def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -250, 250)))

# Kostfunktion (log-likelihood)
def kostfunktion(a, b, c, X, y):
    z = a + b * X[:, 0] + c * X[:, 1]
    h = sigmoid(z)
    return -np.mean(y * np.log(h + 1e-15) + (1 - y) * np.log(1 - h + 1e-15))

# Gradient descent implementation
def træn_logistisk_regression(X, y, læringsrate=0.1, iterationer=1000):  # ÆNDRE DISSE VÆRDIER HER
    # Initialiser parametre
    a = 0.0  # konstant term
    b = 0.0  # x1 koefficient  
    c = 0.0  # x2 koefficient
    
    m = len(X)
    
    for i in range(iterationer):
        # Forudsig med sigmoid
        z = a + b * X[:, 0] + c * X[:, 1]
        h = sigmoid(z)
        
        # Beregn gradienter
        grad_a = np.mean(h - y)
        grad_b = np.mean((h - y) * X[:, 0])
        grad_c = np.mean((h - y) * X[:, 1])
        
        # Opdater parametre
        a -= læringsrate * grad_a
        b -= læringsrate * grad_b
        c -= læringsrate * grad_c
        
        # Vis kostfunktion hver 200. iteration
        if i % 200 == 0:
            cost = kostfunktion(a, b, c, X, y)
            print(f"Iteration {i}: Kostfunktion = {cost:.6f}")
    
    return a, b, c

# Træn modellen
print("Træner logistisk regression manuelt...")
a, b, c = træn_logistisk_regression(X, y)

# Plot resultater
pos = np.where(y == 1)
neg = np.where(y == 0)

plt.figure(figsize=(10, 6))
plt.plot(X[pos[0], 0], X[pos[0], 1], 'ro', label='Positive klasser')
plt.plot(X[neg[0], 0], X[neg[0], 1], 'bo', label='Negative klasser')

# Beregn beslutningsgrænse: a + b*x1 + c*x2 = 0 => x2 = -(a + b*x1)/c
x1_linje = np.linspace(-3, 3, 100)
x2_linje = -(a + b * x1_linje) / c

plt.plot(x1_linje, x2_linje, 'k-', linewidth=2, label='Beslutningsgrænse (Manuel)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Manuel Logistisk Regression')
plt.grid(True, alpha=0.3)
plt.show()

print(f"\nFundne parametre:")
print(f"a (konstant) = {a:.6f}")
print(f"b (x1 koeff) = {b:.6f}") 
print(f"c (x2 koeff) = {c:.6f}")
print(f"Beslutningsgrænse: {a:.6f} + {b:.6f}*x1 + {c:.6f}*x2 = 0")