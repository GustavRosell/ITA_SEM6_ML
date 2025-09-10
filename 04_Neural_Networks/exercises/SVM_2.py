# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:50:22 2018

@author: Sila
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
 
# Importer data til at lege med
iris = datasets.load_iris()
X = iris.data[:, :2]  # Vi tager kun de første to features. Vi kunne undgå
                      # denne grimme slicing ved at bruge et 2D datasæt
yvalues = iris.target
 
y = []

# Konverter til binær klassifikation (klasse 2 vs resten)
for i in yvalues: 
  if i == 2:
     y = np.append(y,[1])  # Virginica
  else:
     y = np.append(y,[0])  # Setosa og Versicolor


h = .02  # skridtstørrelse i mesh-gridet
 
# Vi opretter en instans af SVM og fitter vores data. Vi skalerer ikke vores
# data da vi vil plotte support vektorerne
C = 10000 # SVM regulariseringsparameter
# Lineær SVM
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
# RBF (Radial Basis Function) SVM
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
# Polynomisk SVM
poly_svc = svm.SVC(kernel='poly', degree=5, C=C).fit(X, y)
# Lineær SVM (alternativ implementation)
lin_svc = svm.LinearSVC(C=C).fit(X, y)
 
# Opret et mesh-grid til at plotte i
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Opret subplots for forskellige kernels
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('SVM med forskellige kernels', fontsize=16)

# Titler for hver kernel
titles = ['Lineær kernel', 'RBF kernel', 'Polynomisk kernel (grad 5)', 'Lineær SVM']
models = [svc, rbf_svc, poly_svc, lin_svc]

for i, (model, title) in enumerate(zip(models, titles)):
    # Beregn subplot position
    row = i // 2
    col = i % 2
    ax = axes[row, col]
    
    # Forudsig på mesh-grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Vis resultatet i et farveplot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    
    # Plot også træningspunkterne
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    ax.set_xlabel('Bægerblad længde')
    ax.set_ylabel('Bægerblad bredde')
    ax.set_title(title)

plt.tight_layout()
plt.show()