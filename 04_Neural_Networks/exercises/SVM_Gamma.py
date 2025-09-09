# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:48:45 2018

@author: Sila
"""

# Testing gamma and C values for SVM
# Effects of different gamma values for SVM with RBF kernel

""" Using the Sklearn Breast Cancer data set 
we will experiment with different settings for C and gamma 
Notice: The dataset is actually linearly inseparable, and therefore relatively simple """

"""
 the gamma value in an SVM with an RBF (Radial Basis Function) kernel controls 
 how far the influence of a single training point extends in the feature space.

    Low gamma (e.g., 0.01): Each training point has a wide area of influence, 
    meaning the model considers data points farther apart from each other to be more similar. 
    This results in a smoother decision boundary but might underfit the data, 
    not capturing its complexity well.

    High gamma (e.g., 10): Each training point has a narrow area of influence, 
    meaning the model is very sensitive to points close to it. 
    This creates a more complex, wiggly decision boundary, 
    but it can lead to overfitting because the model tries to 
    fit too closely to the training data, even including noise.

In short:

    Low gamma → Smoother, simpler decision boundaries.
    High gamma → More complex, specific decision boundaries.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

# Load the breast cancer dataset
#
bc = datasets.load_breast_cancer()
df = pd.DataFrame(data=bc.data)
df["label"] = bc.target

# Scatter plot shown in fig 1
#
plt.scatter(df[0][df["label"] == 0], df[1][df["label"] == 0],
            color='red', marker='o', label='malignant')
plt.scatter(df[0][df["label"] == 1], df[1][df["label"] == 1],
            color='green', marker='*', label='benign')
plt.xlabel('Malignant')
plt.ylabel('Benign')
plt.legend(loc='upper left')
plt.show()

X = bc.data
y = bc.target

# Standardize the features
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_std = sc.fit_transform(X)

# Reduce the dimensionality of the dataset to 2D using PCA
# I.e. use another coordinate system with focus on 2 important features
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)

from sklearn.svm import SVC

# Split the dataset into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.3, random_state=1)

# Train the SVM model with RBF kernel
svm = SVC(kernel='rbf', C=1.0, gamma=0.1, random_state=1)
svm.fit(X_train, y_train)

# Create a meshgrid for plotting the decision boundary
x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# Predict the values for each point in the meshgrid
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary and the data points
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='o', edgecolor='k', s=50, cmap=plt.cm.coolwarm, label='Training Data')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='x', edgecolor='k', s=50, cmap=plt.cm.coolwarm, label='Test Data')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('SVM with RBF Kernel (Breast Cancer Dataset, PCA-reduced)')
plt.legend()
plt.show()

# Define gamma values
gamma_values = [0.01, 0.1, 1, 10]

# Set up a plot grid
fig, axes = plt.subplots(1, len(gamma_values), figsize=(20, 5))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# Iterate over the gamma values
for i, gamma in enumerate(gamma_values):
    # Train the SVM model with RBF kernel for each gamma value
    svm = SVC(kernel='rbf', C=1.0, gamma=gamma, random_state=1)
    svm.fit(X_train, y_train)

    # Predict for the meshgrid points
    Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundary and data points
    ax = axes[i]
    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, marker='o', edgecolor='k', s=50, cmap=plt.cm.coolwarm,
               label='Training Data')
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='x', edgecolor='k', s=50, cmap=plt.cm.coolwarm,
               label='Test Data')
    ax.set_title(f'gamma={gamma}')
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')

plt.suptitle('SVM Decision Boundaries for Different Gamma Values (Breast Cancer Dataset)')
plt.show()