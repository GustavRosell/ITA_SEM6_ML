# Exercise 77 - MNIST Digit Classification
# Klassificer håndskrevne cifre med Random Forest og Decision Tree

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Indlæs MNIST digits dataset
mnist = load_digits()

print("Dataset info:")
print(f"Data shape: {pd.DataFrame(mnist.data).shape}")
print(f"Image shape: {mnist.images[0].shape}")
print(f"Number of classes: {len(np.unique(mnist.target))}")
print(f"Classes: {np.unique(mnist.target)}")

# Visualiser eksempler
fig, axes = plt.subplots(2, 10, figsize=(16, 4))
fig.suptitle('MNIST Samples', fontsize=16)
for i in range(20):
    row, col = i // 10, i % 10
    axes[row, col].imshow(mnist.images[i], cmap='gray')
    axes[row, col].axis('off')
    axes[row, col].set_title(f"Label: {mnist.target[i]}")

plt.tight_layout()
plt.show()

# Split i train og test
X_train, X_test, y_train, y_test = train_test_split(
    mnist.data,
    mnist.target,
    test_size=0.2,
    random_state=0
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# ============================================
# MODEL 1: RANDOM FOREST
# ============================================

print("\n" + "="*50)
print("RANDOM FOREST CLASSIFIER")
print("="*50)

# Baseline Random Forest
rf_clf = RandomForestClassifier(n_estimators=10, max_depth=None, random_state=0)
rf_clf.fit(X_train, y_train)
y_pred_rf = rf_clf.predict(X_test)

acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"\nBaseline RF Accuracy: {acc_rf:.4f} ({acc_rf*100:.2f}%)")

# Confusion Matrix
conf_mat_rf = confusion_matrix(y_test, y_pred_rf)
print("\nConfusion Matrix:")
print(conf_mat_rf)

# Visualiser confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(conf_mat_rf, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title(f'Random Forest - Confusion Matrix (Acc: {acc_rf:.4f})')
plt.show()

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))

# ============================================
# MODEL 2: DECISION TREE
# ============================================

print("\n" + "="*50)
print("DECISION TREE CLASSIFIER")
print("="*50)

dt_clf = DecisionTreeClassifier(max_depth=None, random_state=0)
dt_clf.fit(X_train, y_train)
y_pred_dt = dt_clf.predict(X_test)

acc_dt = accuracy_score(y_test, y_pred_dt)
print(f"\nDecision Tree Accuracy: {acc_dt:.4f} ({acc_dt*100:.2f}%)")

# Confusion Matrix
conf_mat_dt = confusion_matrix(y_test, y_pred_dt)
print("\nConfusion Matrix:")
print(conf_mat_dt)

# Visualiser confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(conf_mat_dt, annot=True, fmt='d', cmap='Greens',
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title(f'Decision Tree - Confusion Matrix (Acc: {acc_dt:.4f})')
plt.show()

# ============================================
# ANALYSE: HVILKE CIFRE ER SVÆREST?
# ============================================

print("\n" + "="*50)
print("ERROR ANALYSIS")
print("="*50)

# Find per-class accuracy for Random Forest
class_accuracies = []
for digit in range(10):
    mask = y_test == digit
    if mask.sum() > 0:
        acc = (y_pred_rf[mask] == digit).sum() / mask.sum()
        class_accuracies.append((digit, acc))
        print(f"Digit {digit}: {acc:.4f} ({acc*100:.2f}%)")

# Sorter efter sværeste
class_accuracies.sort(key=lambda x: x[1])
print(f"\nSværeste ciffer at genkende: {class_accuracies[0][0]} ({class_accuracies[0][1]*100:.2f}%)")
print(f"Lettest ciffer at genkende: {class_accuracies[-1][0]} ({class_accuracies[-1][1]*100:.2f}%)")

# Visualiser nogle fejl
errors = np.where(y_pred_rf != y_test)[0][:10]  # Første 10 fejl

if len(errors) > 0:
    fig, axes = plt.subplots(2, 5, figsize=(15, 6))
    fig.suptitle('Random Forest - Misclassifications', fontsize=16)
    for idx, error_idx in enumerate(errors):
        row, col = idx // 5, idx % 5
        test_idx = error_idx
        axes[row, col].imshow(X_test[test_idx].reshape(8, 8), cmap='gray')
        axes[row, col].axis('off')
        axes[row, col].set_title(f"Real: {y_test[test_idx]}\nPred: {y_pred_rf[test_idx]}",
                                  color='red')
    plt.tight_layout()
    plt.show()

# ============================================
# SAMMENLIGNING
# ============================================

print("\n" + "="*50)
print("MODEL COMPARISON")
print("="*50)
print(f"Random Forest:   {acc_rf:.4f} ({acc_rf*100:.2f}%)")
print(f"Decision Tree:   {acc_dt:.4f} ({acc_dt*100:.2f}%)")
print(f"Difference:      {abs(acc_rf - acc_dt):.4f}")

if acc_rf > acc_dt:
    print("\nRandom Forest er bedre!")
    print("Forklaring: Ensemble af mange træer → lavere variance → bedre generalisering")
else:
    print("\nDecision Tree er overraskende bedre!")

# ============================================
# OPGAVER
# ============================================

print("\n" + "="*50)
print("OPGAVER")
print("="*50)
print("""
a) Forbedre Random Forest accuracy:
   - Prøv n_estimators=50, 100, 200
   - Prøv max_depth=10, 20, None
   - Hvilken configuration giver bedst resultat?

b) Forbedre Decision Tree:
   - Prøv max_depth=5, 10, 15, 20
   - Prøv min_samples_split=2, 5, 10
   - Kan du matche Random Forest?

c) Se på confusion matrix:
   - Hvilke cifre forveksles med hinanden?
   - Eksempel: Bliver 3 forvekslet med 8?
   - Hvorfor tror du det sker?

d) Timing:
   - Mål trænings- og inference tid
   - Hvad er hurtigst? Random Forest eller Decision Tree?

e) Feature importance (Random Forest):
   - Hvilke pixels er vigtigst for klassifikation?
   - Hint: rf_clf.feature_importances_

f) Prøv andre algoritmer:
   - Logistic Regression
   - K-Nearest Neighbors
   - Neural Network (MLPClassifier)
   - Sammenlign alle!

Log dine resultater!
""")
