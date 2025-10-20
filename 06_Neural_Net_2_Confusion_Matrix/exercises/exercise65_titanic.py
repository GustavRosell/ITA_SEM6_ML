# Exercise 65 - Titanic Survival Prediction
# Brug Pandas og MLP til at forudsige overlevelse på Titanic
# Mål: Opnå > 64% accuracy (baseline = altid forudsige "død")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Indlæs Titanic data
data = pd.read_csv('../resources/titanic_train_500_age_passengerclass.csv', sep=',', header=0)

# Vis overview af data
print(data.describe(include='all'))
print("\nAntal samples:", len(data))
print("\nMissing values:\n", data.isnull().sum())

# Håndter missing data - EKSPERIMENTÉR MED FORSKELLIGE METODER:
# Metode 1: Fyld med gennemsnit
data["Pclass"].fillna(3, inplace=True)
data["Age"].fillna(data["Age"].mean(), inplace=True)  # Gennemsnitsalder: ~29

# Gem Survived kolonne separat
yvalues = pd.DataFrame(dict(Survived=[]), dtype=int)
yvalues["Survived"] = data["Survived"].copy()

# Visualiser data
x = data["Age"]
y = data["Pclass"]
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.scatter(x.values, y.values, color='black', s=20)
plt.xlabel('Age')
plt.ylabel('Pclass')
plt.title('Age vs Pclass')

plt.subplot(1, 3, 2)
plt.scatter(x.values, yvalues["Survived"].values, color='blue', s=20)
plt.xlabel('Age')
plt.ylabel('Survived')
plt.title('Age vs Survived')

plt.subplot(1, 3, 3)
plt.scatter(data["Pclass"].values, yvalues["Survived"].values, color='green', s=20)
plt.xlabel('Pclass')
plt.ylabel('Survived')
plt.title('Pclass vs Survived')

plt.tight_layout()
plt.show()

# Rens data - fjern unødvendige kolonner
data.drop('Survived', axis=1, inplace=True)
data.drop('PassengerId', axis=1, inplace=True)  # PassengerId er ikke relevant

print("\nData efter rensning:")
print(data.describe(include='all'))

# Split i træning og test (400 train, 100 test)
xtrain = data.head(400)
xtest = data.tail(100)
ytrain = yvalues.head(400)
ytest = yvalues.tail(100)

print("\nTræningsdata samples:", len(ytrain))
print("Test data samples:", len(ytest))
print("\nDistribution i test set:")
print("Døde (0):", (ytest == 0).sum().values[0], "=", (ytest == 0).sum().values[0], "%")
print("Overlevede (1):", (ytest == 1).sum().values[0], "=", (ytest == 1).sum().values[0], "%")

# Feature scaling (vigtigt for neural networks!)
scaler = StandardScaler()
scaler.fit(xtrain)
xtrain_scaled = scaler.transform(xtrain)
xtest_scaled = scaler.transform(xtest)

# Byg og træn MLP
mlp = MLPClassifier(hidden_layer_sizes=(8, 8), max_iter=1000, random_state=0)
mlp.fit(xtrain_scaled, ytrain.values.ravel())

# Forudsig på test set
predictions = mlp.predict(xtest_scaled)

# Evaluer performance
matrix = confusion_matrix(ytest, predictions)
print("\nConfusion Matrix:")
print(matrix)
print("\nClassification Report:")
print(classification_report(ytest, predictions))

# Beregn accuracy manuelt
tn, fp, fn, tp = matrix.ravel()
accuracy = (tp + tn) / (tp + tn + fp + fn)
print(f"\nManuel accuracy beregning:")
print(f"TP={tp}, TN={tn}, FP={fp}, FN={fn}")
print(f"Accuracy = (TP + TN) / Total = ({tp} + {tn}) / {tp + tn + fp + fn} = {accuracy:.2%}")

# EKSPERIMENTER (vær systematisk og notér resultater!):
# a) Netværkstopologi: Prøv (5), (10), (5,5), (10,10,10), etc.
# b) Missing data: Prøv fillna(0), fillna(median), dropna()
# c) Uden scaler: Fjern StandardScaler - virker det?
# d) Batch size: Prøv batch_size parameter
# e) Epochs: Prøv max_iter=100, 500, 2000
# f) Activation: Prøv activation='tanh', 'relu', 'logistic'
#
# Baseline: Random predictor = ~64% (altid forudsige "død")
# Mål: > 64% accuracy!
