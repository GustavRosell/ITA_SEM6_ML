# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:54:51 2018

@author: Sila
"""

import matplotlib.pyplot as plt
import numpy as np
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
plt.plot(X,y, "b.")
plt.axis([0,2,0,15])
plt.plot()
plt.show()


""" -------------------------------------------------------------------------------- """
# Explanation
# This short script demonstrates how to generate synthetic linear-looking data and plot it.
#
# 1. Data generation:
#    X = 2 * np.random.rand(100, 1)
#       - Draws 100 random numbers uniformly in the interval [0, 2).
#       - Shape (100, 1) so each row is a single feature value.
#    y = 4 + 3 * X + np.random.randn(100, 1)
#       - Implements the linear model: y = β0 + β1 * X + ε
#       - Here β0 (intercept) = 4, β1 (slope) = 3.
#       - ε is Gaussian noise sampled by np.random.randn(100, 1), i.e. ε ~ N(0, 1).
#         This adds random vertical variation so points do not lie perfectly on a line.
#
# 2. Plotting:
#    plt.plot(X, y, "b.")
#       - Uses a blue dot ('.') style to make a scatter-like plot via plot().
#    plt.axis([0, 2, 0, 15])
#       - Fixes x-limits to [0, 2] matching the range of X and y-limits for a clear view
#         (since expected y values: 4 + 3*x with x in [0,2] gives noiseless range [4, 10];
#         we extend to 15 to leave headroom for noise outliers).
#
# 3. Why this matters for linear regression:
#    - The underlying true relationship is linear with parameters (β0, β1) = (4, 3).
#    - Real-world datasets often follow an approximate linear relation plus noise.
#    - Later, linear regression will estimate parameters (β̂0, β̂1) by minimizing the
#      sum of squared residuals:  min_{β0,β1} Σ_i (y_i - (β0 + β1 x_i))^2.
#
# 4. Noise term rationale:
#    - If ε were always 0, every point would fall exactly on the line y = 4 + 3x.
#    - Adding ε ~ N(0, 1) simulates measurement error or natural variability, making the
#      exercise more realistic for regression fitting.
#
# 5. Distribution summaries (conceptually):
#    - X ~ Uniform(0, 2).
#    - y | X = x  ~ Normal( 4 + 3x, 1 ).  (Mean 4 + 3x, variance 1 from the noise.)
#
# 6. Next steps you might try (not implemented here to keep the file simple):
#    - Fit a line using the normal equation: θ = (X_b^T X_b)^{-1} X_b^T y with X_b = [1  X].
#    - Use sklearn.linear_model.LinearRegression to compare results.
#    - Plot the fitted line over the scatter to visualize the model.
#
# Key math recap:
#   Model: y_i = β0 + β1 x_i + ε_i,   ε_i ~ N(0, σ^2)
#   Objective (Ordinary Least Squares): minimize J(β0,β1) = Σ_i (y_i - β0 - β1 x_i)^2
#   Closed form solution general form (vector/matrix): θ = (X^T X)^{-1} X^T y
#
# This file purposely stops at data creation + plotting so you can focus on
# recognizing the pattern before implementing the estimation step.
