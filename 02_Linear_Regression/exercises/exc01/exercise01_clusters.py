"""Exercise 1
Generate ~60 random 2D points in three clearly separated clusters and plot them.
Only the required functionality (no extras).
"""
import random

try:
    import matplotlib.pyplot as plt  # type: ignore
except ImportError:  # fallback friendly message
    print("matplotlib not installed. Install with: pip install matplotlib")
    raise SystemExit(1)

# Fixed seed for reproducibility (change or remove if you want fresh randomness)
random.seed(42)

# Define 3 cluster centers (manually chosen to be well separated)
centers = [
    (0.0, 0.0),   # Cluster 1
    (6.0, 2.0),   # Cluster 2
    (3.0, 7.0),   # Cluster 3
]
colors = ["tab:blue", "tab:orange", "tab:green"]
points_per_cluster = 20  # 3 * 20 = 60 points total
std_dev = 0.8            # Spread of each cluster

xs = []
ys = []
cs = []

for (cx, cy), col in zip(centers, colors):
    for _ in range(points_per_cluster):
        x = random.gauss(cx, std_dev)
        y = random.gauss(cy, std_dev)
        xs.append(x)
        ys.append(y)
        cs.append(col)

plt.scatter(xs, ys, c=cs, edgecolor="black", linewidth=0.5)
plt.title("Three Separable Clusters (Exercise 1)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(alpha=0.3)
plt.show()
