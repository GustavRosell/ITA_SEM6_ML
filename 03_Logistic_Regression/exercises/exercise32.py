import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Større datasæt med klassifikation
X = np.array(np.matrix('34.62365962451697,78.0246928153624;30.28671076822607,43.89499752400101; 35.84740876993872,72.90219802708364;60.18259938620976,86.30855209546826;79.0327360507101,75.3443764369103;45.08327747668339,56.3163717815305; 61.10666453684766,96.51142588489624; 75.02474556738889,46.55401354116538; 76.09878670226257,87.42056971926803;84.43281996120035,43.53339331072109; 95.86155507093572,38.22527805795094; 75.01365838958247,30.60326323428011; 82.30705337399482,76.48196330235604; 69.36458875970939,97.71869196188608; 39.53833914367223,76.03681085115882; 53.9710521485623,89.20735013750205; 69.07014406283025,52.74046973016765; 67.94685547711617,46.67857410673128; 70.66150955499435,92.92713789364831; 76.97878372747498,47.57596364975532;67.37202754570876,42.83843832029179'))
y = np.array(np.matrix('0;0;0;1;1;0;1;1;1;1;0;0;1;1;0;1;1;0;1;1;0'))[:,0]

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
x_linje = np.linspace(30, 100)
y_linje = -(b * x_linje + a) / c

plt.plot(x_linje, y_linje, 'k-', label='Beslutningsgrænse')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

print(f"Parametre: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
print(f"Beslutningsgrænse: {b:.4f}*x + {c:.4f}*y + {a:.4f} = 0")