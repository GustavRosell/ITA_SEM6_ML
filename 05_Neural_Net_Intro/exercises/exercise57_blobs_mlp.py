# Exercise 57 - MLP klassificering af Blobs dataset
# Brug MultiLayer Perceptron til at klassificere syntetisk blob-data

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np

# Generer blob dataset
n_samples = 200
blob_centers = ([1, 1], [3, 4], [1, 3.3], [3.5, 1.8])
X, y = make_blobs(n_samples=n_samples,
                  centers=blob_centers,
                  cluster_std=0.5,
                  random_state=0)

# Visualiser dataset
colours = ('green', 'orange', 'blue', 'magenta')
plt.figure()
for n_class in range(len(blob_centers)):
    plt.scatter(X[y==n_class][:, 0],
                X[y==n_class][:, 1],
                c=colours[n_class],
                s=30,
                label=str(n_class))
plt.legend()
plt.title("Blob Dataset")
plt.show()

# Split i træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Feature scaling
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Træn MLP
mlp = MLPClassifier(hidden_layer_sizes=(5), max_iter=100)
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
plt.xlabel('X')
plt.ylabel('Y')
plt.title("MLP Klassificering - Blobs")
plt.show()

# Eksperimenter:
# A) Juster hidden layers og max_iter for at få korrekt klassificering
#    Prøv fx (10), (10,10), (20,20), etc. og max_iter=500, 1000
# B) Prøv uden StandardScaler - fungerer det stadig?
# C) Eksperimentér med blob_centers og n_samples
#    Prøv fx flere centers eller anderledes placeringer
