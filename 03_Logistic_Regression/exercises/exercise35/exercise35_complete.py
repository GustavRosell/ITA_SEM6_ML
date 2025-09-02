import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from pandas.plotting import scatter_matrix

# Indlæs Iris datasæt
print("=== IRIS DATASÆT ANALYSE ===\n")

# Metode 1: Fra URL (pandas)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

print(f"Datasæt form: {dataset.shape}")
print(f"Kolonner: {list(dataset.keys())}")
print("\nFørste 10 rækker:")
print(dataset.head(10))
print("\nStatistisk beskrivelse:")
print(dataset.describe())

# Vis histogrammer
print("\nViser histogrammer...")
dataset.hist(figsize=(12, 8))
plt.suptitle('Iris Datasæt - Histogrammer')
plt.tight_layout()
plt.show()

# Vis scatter plot matrix
print("Viser scatter plot matrix...")
scatter_matrix(dataset, figsize=(12, 8))
plt.suptitle('Iris Datasæt - Scatter Plot Matrix')
plt.tight_layout()
plt.show()

# === ANALYSE 1: KUN PETAL-WIDTH ===
print("\n=== ANALYSE 1: PETAL-WIDTH KLASSIFIKATION ===")

array = dataset.values
X_single = array[:,3]  # petal width
Y = array[:,4]         # classification

# Konverter labels til binær klassifikation (Virginica vs andre)
a_enc = pd.factorize(Y)
yvalues = a_enc[0]
y_binary = []
for i in yvalues: 
    if i == 2:  # Virginica
        y_binary = np.append(y_binary, [1])
    else:       # Setosa eller Versicolor
        y_binary = np.append(y_binary, [0])

# Test forskellige C værdier
C_values = [0.1, 1, 10, 100, 1000]  # ÆNDRE DISSE VÆRDIER HER
regularization_types = ['l1', 'l2']  # ÆNDRE REGULARIZATION TYPE HER

print(f"Tester C værdier: {C_values}")
print(f"Tester regularization: {regularization_types}")

for reg_type in regularization_types:
    plt.figure(figsize=(15, 10))
    
    for idx, C_val in enumerate(C_values):
        plt.subplot(2, 3, idx + 1)
        
        # Træn model
        model = LogisticRegression(penalty=reg_type, C=C_val, solver='liblinear', random_state=42)
        model.fit(X_single.reshape(-1, 1), y_binary)
        
        # Udtræk parametre i europæisk notation
        a = model.intercept_[0]  # konstant term
        b = model.coef_[0, 0]    # petal-width koefficient
        
        # Beregn sandsynligheder
        X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
        y_proba = model.predict_proba(X_new)
        
        # Plot resultater
        plt.plot(X_single, y_binary, "bo", alpha=0.6, markersize=4, label="Data punkter")
        plt.plot(X_new, y_proba[:,1], "r-", linewidth=2, label="Iris-Virginica")
        plt.plot(X_new, y_proba[:,0], "g--", linewidth=2, label="Ikke Iris-Virginica")
        
        plt.xlabel("Kronblad bredde (cm)")
        plt.ylabel("Sandsynlighed")
        plt.title(f'{reg_type.upper()} Reg., C={C_val}\na={a:.3f}, b={b:.3f}')
        plt.legend(fontsize=8)
        plt.grid(True, alpha=0.3)
        
        # Beregn nøjagtighed
        accuracy = model.score(X_single.reshape(-1, 1), y_binary)
        plt.text(0.05, 0.95, f'Nøjagtighed: {accuracy:.3f}', 
                transform=plt.gca().transAxes, fontsize=8, 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.suptitle(f'Petal-Width Klassifikation - {reg_type.upper()} Regularization', y=1.02)
    plt.show()

# === ANALYSE 2: PETAL-LENGTH OG PETAL-WIDTH ===
print("\n=== ANALYSE 2: PETAL-LENGTH OG PETAL-WIDTH ===")

# Brug sklearn dataset for lettere adgang
iris = datasets.load_iris()
X_dual = iris["data"][:, (2, 3)]  # petal length, petal width
yy = iris["target"]

y_dual = []
for i in yy: 
    if i == 2:  # Virginica
        y_dual = np.append(y_dual, [1])
    else:       # Setosa eller Versicolor
        y_dual = np.append(y_dual, [0])

# Test forskellige C værdier for 2D klassifikation
C_test_values = [1, 10, 100, 1000]  # ÆNDRE DISSE VÆRDIER HER

plt.figure(figsize=(16, 12))

for idx, C_val in enumerate(C_test_values):
    plt.subplot(2, 2, idx + 1)
    
    # Træn model
    model = LogisticRegression(C=C_val, random_state=42)
    model.fit(X_dual, y_dual)
    
    # Udtræk parametre i europæisk notation
    a = model.intercept_[0]   # konstant term
    b = model.coef_[0, 0]     # petal-length koefficient
    c = model.coef_[0, 1]     # petal-width koefficient
    
    # Plot datapunkter
    plt.scatter(X_dual[:, 0][y_dual==1], X_dual[:, 1][y_dual==1], 
               c='red', marker='o', s=50, alpha=0.7, label='Iris-Virginica')
    plt.scatter(X_dual[:, 0][y_dual==0], X_dual[:, 1][y_dual==0], 
               c='blue', marker='s', s=50, alpha=0.7, label='Setosa/Versicolor')
    
    # Beregn og plot beslutningsgrænse: a + b*x1 + c*x2 = 0 => x2 = -(a + b*x1)/c
    x1_linje = np.linspace(1, 7, 100)
    x2_linje = -(a + b * x1_linje) / c
    
    plt.plot(x1_linje, x2_linje, 'k-', linewidth=2, label='Beslutningsgrænse')
    
    plt.xlabel('Kronblad længde (cm)')
    plt.ylabel('Kronblad bredde (cm)')
    plt.title(f'C = {C_val}\na={a:.3f}, b={b:.3f}, c={c:.3f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Beregn nøjagtighed
    accuracy = model.score(X_dual, y_dual)
    plt.text(0.05, 0.95, f'Nøjagtighed: {accuracy:.3f}', 
            transform=plt.gca().transAxes, 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

plt.tight_layout()
plt.suptitle('2D Klassifikation - Petal Length vs Petal Width', y=1.02)
plt.show()

# === SAMMENLIGNING AF REGULARIZATION ===
print("\n=== REGULARIZATION SAMMENLIGNING ===")

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

for idx, reg_type in enumerate(['l1', 'l2']):
    ax = axes[idx]
    
    model = LogisticRegression(penalty=reg_type, C=100, solver='liblinear', random_state=42)
    model.fit(X_dual, y_dual)
    
    # Udtræk parametre
    a = model.intercept_[0]
    b = model.coef_[0, 0]  
    c = model.coef_[0, 1]
    
    # Plot
    ax.scatter(X_dual[:, 0][y_dual==1], X_dual[:, 1][y_dual==1], 
              c='red', marker='o', s=50, alpha=0.7, label='Iris-Virginica')
    ax.scatter(X_dual[:, 0][y_dual==0], X_dual[:, 1][y_dual==0], 
              c='blue', marker='s', s=50, alpha=0.7, label='Setosa/Versicolor')
    
    x1_linje = np.linspace(1, 7, 100)
    x2_linje = -(a + b * x1_linje) / c
    ax.plot(x1_linje, x2_linje, 'k-', linewidth=2, label='Beslutningsgrænse')
    
    accuracy = model.score(X_dual, y_dual)
    
    ax.set_xlabel('Kronblad længde (cm)')
    ax.set_ylabel('Kronblad bredde (cm)')
    ax.set_title(f'{reg_type.upper()} Regularization (C=100)\nNøjagtighed: {accuracy:.3f}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    print(f"{reg_type.upper()} regularization - a={a:.4f}, b={b:.4f}, c={c:.4f}, nøjagtighed={accuracy:.4f}")

plt.tight_layout()
plt.show()

print("\n=== ANALYSE FULDFØRT ===")
print("Se exercise35_findings.txt for detaljerede resultater og anbefalinger.")