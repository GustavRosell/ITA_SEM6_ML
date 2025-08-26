"""Exercise 2.3
Generate the data and fit a linear regression line using the normal equation.
Plot the points and the fitted line.
"""
import numpy as np

try:
    import matplotlib.pyplot as plt  # type: ignore
except ImportError:
    print("Install matplotlib: pip install matplotlib")
    raise SystemExit(1)

np.random.seed(42)

# Data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term and solve normal equation: theta = (X^T X)^{-1} X^T y
X_b = np.c_[np.ones((X.shape[0], 1)), X]
theta_best = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)
intercept = float(theta_best[0, 0])
slope = float(theta_best[1, 0])

# Prepare line for plotting
X_line = np.linspace(0, 2, 100).reshape(-1, 1)
y_line = intercept + slope * X_line

plt.scatter(X, y, color="tab:green", s=25, label="Data")
plt.plot(X_line, y_line, color="black", linewidth=2, label=f"Fit: y = {intercept:.2f} + {slope:.2f}x")
plt.title("Linear Regression Fit (Exercise 2.3)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
