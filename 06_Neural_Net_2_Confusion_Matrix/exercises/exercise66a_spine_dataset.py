# Exercise 66a - Spine Dataset Classification
# Lower Back Pain Symptoms Dataset - klassificer Normal vs Abnormal

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Indlæs Spine dataset
df = pd.read_csv('../resources/dataset_spine.csv')

# Fjern ubrugelig kolonne
df = df.drop(['Unnamed: 13'], axis=1)

print("Første rækker af data:")
print(df.head())
print("\nDataset beskrivelse:")
print(df.describe())
print("\nTag et øjeblik at kigge på describe() resultatet...")

# Fjern irrelevante kolonner (Col7-12)
df = df.drop(['Col7','Col8','Col9','Col10','Col11','Col12'], axis=1)

print("\nData efter fjernelse af irrelevante kolonner:")
print(df.head())

# Konvertér class labels til numeriske værdier
df = df.replace(to_replace="Abnormal", value="1")
df = df.replace(to_replace="Normal", value="0")

# Split features og target
y = df['Class_att'].astype(int)
X = df.drop(['Class_att'], axis=1)

print("\nTarget values (y):")
print(y.value_counts())
print(f"\nNormal (0): {(y == 0).sum()}")
print(f"Abnormal (1): {(y == 1).sum()}")

# Split i træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=27)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nBegynder træning...")

# Træn MLP
clf = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=1000, random_state=0)
clf.fit(X_train_scaled, y_train)

# Forudsigelser
y_pred = clf.predict(X_test_scaled)

print("Træning færdig!\n")

# Evaluer performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2%}")

# Confusion matrix
con_mat = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(con_mat)

tn, fp, fn, tp = con_mat.ravel()
print(f"\nTP={tp}, TN={tn}, FP={fp}, FN={fn}")

# Visualiser confusion matrix med heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(con_mat, annot=True, fmt='d', cmap='Blues', center=True)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Spine Dataset')
plt.show()

# OPGAVE: Forbedre MLP classifier for at få bedre accuracy!
# Eksperimenter med:
# - hidden_layer_sizes: (5,5), (10,10), (8,8,8)
# - max_iter: 500, 1000, 2000
# - activation: 'relu', 'tanh', 'logistic'
# - solver: 'adam', 'sgd', 'lbfgs'
# - alpha (regularization): 0.0001, 0.001, 0.01
#
# Se Exercise_DataSetSpine.pdf for mere info!
