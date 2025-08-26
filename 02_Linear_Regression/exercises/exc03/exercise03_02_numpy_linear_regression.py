# -*- coding: utf-8 -*-
"""
Created for Linear Regression Exercise (extension of exercise03_01_numpy.py)

Generates synthetic linear data and fits a line using the Normal Equation.
"""

import numpy as np
import matplotlib.pyplot as plt

# Data generation (same pattern as previous script)
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# --- Linear Regression via Normal Equation ---
# Add bias term (column of 1s) so model is y = theta0 + theta1 * x
X_b = np.c_[np.ones((X.shape[0], 1)), X]
# theta_best = (X^T X)^{-1} X^T y
theta_best = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)
intercept = float(theta_best[0, 0])
slope = float(theta_best[1, 0])

# Prepare line for visualization
X_line = np.linspace(0, 2, 100).reshape(-1, 1)
y_line = intercept + slope * X_line

# Plot data points
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
# Plot fitted regression line
plt.plot(X_line, y_line, "r", linewidth=2, label=f"Fit: y = {intercept:.2f} + {slope:.2f}x")
plt.legend()
plt.title("Linear Regression Fit")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

""" -------------------------------------------------------------------------------- """
# Explanation
# This script extends the previous one by computing and drawing the best-fit line
# for the generated noisy linear data.
#
# MODEL:
#   y = β0 + β1 x + ε,  with ε ~ N(0, σ²)
# True underlying parameters used to create the data: β0 = 4, β1 = 3.
# We add Gaussian noise (np.random.randn) so points are scattered.
#
# NORMAL EQUATION DERIVATION (brief):
#   Given design matrix X_b (first column all 1s), parameters θ = [β0, β1]^T.
#   Objective (Ordinary Least Squares): minimize J(θ) = ||X_b θ - y||².
#   Setting gradient to zero: 2 X_b^T (X_b θ - y) = 0  ->  X_b^T X_b θ = X_b^T y.
#   If X_b^T X_b is invertible: θ = (X_b^T X_b)^{-1} X_b^T y.
#
# IMPLEMENTATION STEPS:
# 1. Build X_b with bias: np.c_[ones, X].
# 2. Compute theta_best using matrix operations.
# 3. Extract intercept & slope for readability.
# 4. Create a dense range of X values (X_line) and compute corresponding predictions.
# 5. Plot original data (blue points) and fitted line (red line).
#
# WHY THIS WORKS:
# - The closed form gives the least squares optimal parameters for linear regression
#   under assumptions of linear model with additive noise.
# - Even with noise, the estimated parameters should be close to (4, 3) for large enough samples.
#
# TRY YOURSELF:
# - Print theta_best to inspect the numeric values.
# - Change sample size or noise scale (e.g., multiply np.random.randn by 2) and observe impact.
# - Compare with sklearn.linear_model.LinearRegression for validation.
