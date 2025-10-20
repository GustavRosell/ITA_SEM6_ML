# Exercise 56 - MLP klassificering af Iris dataset
# Brug MultiLayer Perceptron til at klassificere petal length og width

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Indlæs Iris dataset
iris = load_iris()
X = iris.data[:,(2,3)]  # Petal length og width
y = iris.target

print("Antal samples: " + str(len(y)))

# Visualiser dataset
plt.figure()
colormap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=colormap, edgecolor='black', s=20)
plt.show()

# Split i træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Feature scaling
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Træn MLP
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train)

# Forudsigelser
predictions = mlp.predict(X_test)
print("Forudsigelser:", predictions)

# Visualiser resultat med decision boundaries
h = .02
x_min, x_max = X_test[:, 0].min() - 1, X_test[:, 0].max() + 1
y_min, y_max = X_test[:, 1].min() - 1, X_test[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure()
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolor='black')
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title("MLP Klassificering")
plt.show()

# Eksperimenter:
# A) Ændr test_size til 0.05 og 0.90 - hvad sker der?
# B) Fjern StandardScaler - kan klassificatoren stadig fungere?
# C) Ændr max_iter til 100 - var det en god idé?
# D) Eksperimentér med hidden_layer_sizes - prøv (2), (5), (10), (10,10), etc.
#    Hvad giver bedste resultater?
