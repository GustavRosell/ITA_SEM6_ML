"""Exercise 2.1
Generate 20 random (x, y) points and plot them.
Minimal solution.
"""
import random

try:
    import matplotlib.pyplot as plt  # type: ignore
except ImportError:
    print("Install matplotlib: pip install matplotlib")
    raise SystemExit(1)

random.seed(42)

points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(20)]
xs = [p[0] for p in points]
ys = [p[1] for p in points]

plt.scatter(xs, ys, color="tab:blue")
plt.title("20 Random Points (Exercise 2.1)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(alpha=0.3)
plt.show()
