import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Generer kubisk data: y = 0.1*x³ + 0.5*x² + x + 2 + støj
X = 6 * np.random.rand(100, 1) - 3
y = 0.1 * X**3 + 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

# Vis oprindelige datapunkter
plt.plot(X, y, "g.", label="Datapunkter")
plt.axis([-3, 3, -5, 15])

# Lav polynomial features med sklearn
poly_features = PolynomialFeatures(degree=3, include_bias=False)
X_poly = poly_features.fit_transform(X)

# Træn lineær regression model
model = LinearRegression()
model.fit(X_poly, y)

# Udtræk parametre i europæisk notation
a = model.intercept_[0]  # konstant term
b = model.coef_[0][0]    # x koefficient  
c = model.coef_[0][1]    # x² koefficient
d = model.coef_[0][2]    # x³ koefficient

# Lav forudsigelser for glat kurve
X_plot = np.linspace(-3, 3, 300).reshape(-1, 1)
X_plot_poly = poly_features.transform(X_plot)
y_plot = model.predict(X_plot_poly)

plt.plot(X_plot, y_plot, "b-", label="Kubisk fit (sklearn)")
plt.legend()
plt.show()

print(f"Parametre: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, d = {d:.4f}")
print(f"Model: y = {a:.4f} + {b:.4f}*x + {c:.4f}*x² + {d:.4f}*x³")