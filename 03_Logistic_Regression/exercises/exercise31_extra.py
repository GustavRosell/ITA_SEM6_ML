import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Udvidet datasæt med klassifikation
X = np.array(np.matrix('4,450;5,600;6,700;4.5,550;4.9,500;5,650;5.5,500; 5.25,525; 4.25,625; 4.75,575'))
y = np.array(np.matrix('0;1;1;0;0;1;0;1;1;1'))[:,0]

# Find positive og negative klasser
pos = np.where(y==1)
neg = np.where(y==0)

# Plot datapunkter
plt.plot(X[pos[0],0], X[pos[0],1], 'ro', label='Positive klasser')
plt.plot(X[neg[0],0], X[neg[0],1], 'bo', label='Negative klasser')
plt.xlim([min(X[:,0]),max(X[:,0])])
plt.ylim([min(X[:,1]),max(X[:,1])])

# Træn logistisk regression
model = linear_model.LogisticRegression(C=1000)
model.fit(X, y)

# Udtræk parametre i europæisk notation
a = model.intercept_[0]  # konstant term
b = model.coef_[0,0]     # x koefficient
c = model.coef_[0,1]     # y koefficient

# Beregn beslutningsgrænse: b*x + c*y + a = 0 => y = -(b*x + a)/c
x_linje = np.linspace(4, 6.5)
y_linje = -(b * x_linje + a) / c

plt.plot(x_linje, y_linje, 'k-', label='Beslutningsgrænse')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

print(f"Parametre: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
print(f"Beslutningsgrænse: {b:.4f}*x + {c:.4f}*y + {a:.4f} = 0")