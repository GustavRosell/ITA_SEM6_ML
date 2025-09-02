import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

# Generer forge datasæt (specialt designet datasæt)
def lav_forge_datasæt():
    np.random.seed(4)
    # Generer to klumper af data
    centers = np.array([[2, 2], [-2, -2]])
    X = []
    y = []
    
    for i, center in enumerate(centers):
        # 15 punkter per klumpe
        points = np.random.normal(center, 0.8, (15, 2))
        X.extend(points)
        y.extend([i] * 15)
    
    X = np.array(X)
    y = np.array(y)
    
    # Tilføj nogle "svære" punkter for at gøre det interessant
    y[[7, 27]] = 0  # Skift nogle labels
    mask = np.ones(len(X), dtype=bool)
    mask[[0, 1, 5, 26]] = False  # Fjern nogle punkter
    X, y = X[mask], y[mask]
    
    return X, y

# Generer datasæt
X, y = lav_forge_datasæt()

# Find positive og negative klasser
pos = np.where(y == 1)
neg = np.where(y == 0)

# Træn logistisk regression
model = LogisticRegression(C=1000, random_state=42)  # ÆNDRE C-VÆRDI HER
model.fit(X, y)

# Udtræk parametre i europæisk notation
a = model.intercept_[0]  # konstant term
b = model.coef_[0, 0]    # x1 koefficient
c = model.coef_[0, 1]    # x2 koefficient

# Opret plot
plt.figure(figsize=(10, 8))

# Plot datapunkter
plt.scatter(X[pos[0], 0], X[pos[0], 1], c='red', marker='o', s=50, label='Positive klasser')
plt.scatter(X[neg[0], 0], X[neg[0], 1], c='blue', marker='o', s=50, label='Negative klasser')

# Opret grid til beslutningsområde
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx = np.linspace(x_min, x_max, 300)
yy = np.linspace(y_min, y_max, 300)
X1, X2 = np.meshgrid(xx, yy)
grid_punkter = np.c_[X1.ravel(), X2.ravel()]

# Beregn beslutningsfunktion for hele grid
beslutnings_værdier = model.decision_function(grid_punkter)

# Tegn beslutningsgrænse (hvor beslutningsfunktion = 0)
plt.contour(X1, X2, beslutnings_værdier.reshape(X1.shape), 
            levels=[0], colors='black', linestyles='solid', linewidths=2)

# Tilføj farvede områder for at vise klassifikationsområder
plt.contourf(X1, X2, beslutnings_værdier.reshape(X1.shape), 
             levels=50, alpha=0.3, cmap='RdBu')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Logistisk Regression med Forge Datasæt')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Print resultater
print(f"Fundne parametre:")
print(f"a (konstant) = {a:.6f}")
print(f"b (x1 koeff) = {b:.6f}")
print(f"c (x2 koeff) = {c:.6f}")
print(f"Beslutningsgrænse: {a:.6f} + {b:.6f}*x1 + {c:.6f}*x2 = 0")

# Beregn og vis nøjagtighed
nøjagtighed = model.score(X, y)
print(f"\nModel nøjagtighed: {nøjagtighed:.4f} ({nøjagtighed*100:.1f}%)")

# Vis antal punkter i hver klasse
print(f"Antal positive klasser (rød): {len(pos[0])}")
print(f"Antal negative klasser (blå): {len(neg[0])}")
print(f"Total antal punkter: {len(X)}")