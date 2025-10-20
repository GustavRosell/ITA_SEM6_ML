# Exercise 76 - PCA og K-Means på Iris Dataset
# Reducer 4D data til 2D for visualisering, derefter K-Means clustering

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Indlæs Iris dataset
iris_df = datasets.load_iris()
X, y = iris_df.data, iris_df.target

print("Original data shape:", X.shape)  # (150, 4) - 4 features
print("Features:", iris_df.feature_names)

# PCA: Reducer fra 4D til 2D
pca = PCA(n_components=2)
X_proj = pca.fit_transform(X)

print("\nPCA reduceret shape:", X_proj.shape)  # (150, 2) - 2 principal components

# Vis hvor meget variance hver component forklarer
print("\nExplained variance ratio:")
print(f"PC1: {pca.explained_variance_ratio_[0]:.4f} ({pca.explained_variance_ratio_[0]*100:.2f}%)")
print(f"PC2: {pca.explained_variance_ratio_[1]:.4f} ({pca.explained_variance_ratio_[1]*100:.2f}%)")
print(f"Total: {sum(pca.explained_variance_ratio_):.4f} ({sum(pca.explained_variance_ratio_)*100:.2f}%)")

# Vis PCA components (hvordan blev PC1 og PC2 lavet?)
print("\nPCA components (contribution from each feature):")
print("              Sepal_L  Sepal_W  Petal_L  Petal_W")
for i, component in enumerate(pca.components_):
    print(f"PC{i+1}:", " ".join([f"{val:8.4f}" for val in component]))

# Visualiser PCA-reduceret data med original labels
plt.figure(figsize=(10, 5))

# Plot med original classification
plt.subplot(1, 2, 1)
colormap = np.array(['red', 'lime', 'blue'])
plt.scatter(X_proj[:, 0], X_proj[:, 1], c=colormap[y], s=40)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Iris - PCA Reduction (Original Labels)')

# K-Means clustering på PCA-reduceret data
k = 3  # EKSPERIMENTÉR: Prøv forskellige k-værdier

kmeans = KMeans(n_clusters=k, random_state=0).fit(X_proj)
labels = kmeans.labels_
clusters = kmeans.cluster_centers_

print(f"\nK-Means clusters (k={k}):")
print(clusters)

# Plot med K-Means classification
plt.subplot(1, 2, 2)
colormap_kmeans = np.array(['red', 'orange', 'blue', 'green', 'yellow', 'magenta', 'cyan'])
plt.scatter(X_proj[:, 0], X_proj[:, 1], c=colormap_kmeans[labels], s=40)
plt.scatter(clusters[:, 0], clusters[:, 1], c='black', marker='X', s=200, label='Cluster Centers')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title(f'Iris - K-Means Clustering (k={k})')
plt.legend()

plt.tight_layout()
plt.show()

# OPGAVER:
#
# a) Forstå PCA components:
#    - Hvilke features bidrager mest til PC1?
#    - Hvilke features bidrager mest til PC2?
#
# b) Explained variance:
#    - Hvor meget af original data forklares af PC1+PC2?
#    - Er det nok? Prøv n_components=3 og sammenlign
#
# c) Eksperimentér med K-Means:
#    - Prøv k=2, 3, 4, 5
#    - Hvilken k giver bedst clustering?
#    - Sammenlign med original labels
#
# d) Overraskende resultater?
#    - Matcher K-Means clusters med original species?
#    - Hvor går det galt? (hvilke species forveksles?)
#
# e) Prøv uden PCA:
#    - Kør K-Means direkte på original 4D data (X)
#    - Sammenlign accuracy med PCA-version
#    - Er PCA nødvendigt her?
#
# KONKLUSION:
# PCA er kraftfuldt til:
# - Visualisering af højdimensionel data
# - Forståelse af data struktur
# - Noise reduction (drop sidste components)
# Men trade-off: Tab af information og interpretability!
