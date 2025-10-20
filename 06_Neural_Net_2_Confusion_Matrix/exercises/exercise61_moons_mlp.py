# Exercise 61 - MLP klassificering af Moons dataset
# Neural Network til at forudsige datapunkter fra Moons dataset

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np

# Generer Moons dataset
X, y = make_moons(n_samples=1000, noise=0.1)

# Visualiser dataset
df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
colors = {0:'red', 1:'blue'}
fig, ax = plt.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
plt.title("Moons Dataset")
plt.show()

# Split i træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Feature scaling
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Træn MLP
mlp = MLPClassifier(hidden_layer_sizes=(4), max_iter=1000)
mlp.fit(X_train, y_train)

# Forudsigelser
predictions = mlp.predict(X_test)
print("Forudsigelser:", predictions)
print("Accuracy:", mlp.score(X_test, y_test))

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
plt.title("MLP Klassificering - Moons")
plt.show()

# Eksperimenter:
# a) Hvad er minimum antal hidden layers?
# b) Hvad er minimum antal neuroner per layer?
# c) Prøv andre værdier for n_samples og noise
#    Eksempel: n_samples=500, noise=0.3
#    Gentag derefter a) og b)
