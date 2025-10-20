# Exercise 75 - K-Means Clustering på Iris Dataset
# Test unsupervised learning på sepal og petal features

from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Indlæs Iris dataset
iris_df = datasets.load_iris()

print("Feature names:", iris_df.feature_names)
print("Target names:", iris_df.target_names)
print("Antal samples:", len(iris_df.target))

# Organiser data i Pandas DataFrame
x = pd.DataFrame(iris_df.data)
x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

y = pd.DataFrame(iris_df.target)
y.columns = ['Targets']

# Visualiser original classification
plt.figure(figsize=(14, 7))
colormap = np.array(['red', 'lime', 'black', 'blue', 'yellow', 'green'])

# Plot Sepal features
plt.subplot(1, 2, 1)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c=colormap[y.Targets], s=40)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal - Original Classification')

# Plot Petal features
plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal - Original Classification')

plt.tight_layout()
plt.show()

# Vælg features til clustering
x_sepal = x[['Sepal_Length', 'Sepal_Width']]
x_petal = x[['Petal_Length', 'Petal_Width']]

# K-Means clustering
k = 2  # EKSPERIMENTÉR: Prøv k=2, 3, 4, 5

# Kør K-Means på petal data
kmeans = KMeans(n_clusters=k, random_state=0).fit(x_petal)

# Resultater
labels = kmeans.labels_  # Predicted cluster labels
clusters = kmeans.cluster_centers_  # Cluster centers

print(f"\nK-Means med k={k}")
print("Cluster centers:")
print(clusters)

# Sammenlign original vs K-Means classification
plt.figure(figsize=(14, 7))

# Original classification
plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal - Real Classification')

# K-Means classification
plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[labels], s=40)
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', marker='X', s=200, label='Centers')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title(f'Petal - K-Means (k={k})')
plt.legend()

plt.tight_layout()
plt.show()

# OPGAVER:
# a) Juster k til bedre værdi (prøv k=2, 3, 4, 5)
#    Hvilken k giver bedst match med original classification?
#
# b) Skift til sepal dataset (x_sepal)
#    Kør K-Means på sepal features
#    Hvilken k-værdi virker bedst for sepal?
#
# c) Sammenlign:
#    - Fungerer K-Means bedre på petal eller sepal?
#    - Hvorfor tror du det er sådan?
#
# HINT: Iris har 3 species, så k=3 burde være optimalt!
