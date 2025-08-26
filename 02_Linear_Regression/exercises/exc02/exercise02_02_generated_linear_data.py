"""Exercise 2.2
Generate linear-looking data from the given formula and plot it.
"""
import numpy as np

try:
    import matplotlib.pyplot as plt  # type: ignore
except ImportError:
    print("Install matplotlib: pip install matplotlib")
    raise SystemExit(1)

np.random.seed(42)

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

plt.scatter(X, y, color="tab:orange", s=25)
plt.title("Generated Linear Data (Exercise 2.2)")
plt.xlabel("X")
plt.ylabel("y")
plt.grid(alpha=0.3)
plt.show()
