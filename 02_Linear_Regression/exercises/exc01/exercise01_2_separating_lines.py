"""Exercise 1.2
Generate the same three clusters and plot two lines that separate them.

Improvement: Instead of two hand‑tuned approximate lines, we automatically
compute separating lines between the clusters based on the data actually
generated. For each pair of clusters we:
    1. Project all their points onto the vector between their centroids.
    2. If there is a gap between the projections, we place the separating line
         midway inside that gap (guaranteed separation for that pair).
    3. Otherwise we fall back to the perpendicular bisector of the centroids.
Then we pick two of the three pairwise lines whose sign patterns uniquely
distinguish all three centroids (so only two lines are drawn, as requested).

Still kept minimal and self‑contained.
"""
import random
import math

try:
    import matplotlib.pyplot as plt  # type: ignore
except ImportError:
    print("matplotlib not installed. Install with: pip install matplotlib")
    raise SystemExit(1)

random.seed(42)

centers = [
    (0.0, 0.0),
    (6.0, 2.0),
    (3.0, 7.0),
]
colors = ["tab:blue", "tab:orange", "tab:green"]
points_per_cluster = 20
std_dev = 0.8

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

fig, ax = plt.subplots()
ax.scatter(xs, ys, c=cs, edgecolor="black", linewidth=0.5)
ax.set_title("Clusters With Two Separating Lines (Exercise 1.2)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(alpha=0.3)

# Build per-cluster lists
cluster_points = {i: [] for i in range(3)}
for (x, y), col_idx in zip(zip(xs, ys), [0]*points_per_cluster + [1]*points_per_cluster + [2]*points_per_cluster):
    cluster_points[col_idx].append((x, y))

centroids = {}
for i, pts in cluster_points.items():
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    centroids[i] = (cx, cy)

def separating_line(i, j):
    """Return line (a,b,c) for a*x + b*y + c = 0 separating clusters i and j.
    Strategy: project onto vector v between centroids. If projections do not
    overlap we find exact gap midpoint. Else use perpendicular bisector.
    """
    (x1, y1) = centroids[i]
    (x2, y2) = centroids[j]
    vx, vy = x2 - x1, y2 - y1
    norm = math.hypot(vx, vy) or 1.0
    ux, uy = vx / norm, vy / norm  # unit vector along v

    # Projections of points onto v (scalar distance from origin along v)
    proj_i = [(px * ux + py * uy) for (px, py) in cluster_points[i]]
    proj_j = [(px * ux + py * uy) for (px, py) in cluster_points[j]]
    max_i = max(proj_i)
    min_i = min(proj_i)
    max_j = max(proj_j)
    min_j = min(proj_j)

    disjoint = False
    if max_i < min_j:
        gap_low, gap_high = max_i, min_j
        disjoint = True
    elif max_j < min_i:
        gap_low, gap_high = max_j, min_i
        disjoint = True

    if disjoint:
        # threshold projection in the gap midpoint
        t = (gap_low + gap_high) / 2.0
        # Point on line having projection t: start from origin along u
        # A point p satisfying p·u = t is p = t*u (sufficient)
        px, py = t * ux, t * uy
    else:
        # Fallback perpendicular bisector midpoint
        px, py = (x1 + x2) / 2.0, (y1 + y2) / 2.0

    # Line normal is v (vx, vy); line passes through (px, py)
    a, b = vx, vy
    c = -(a * px + b * py)
    return a, b, c

def eval_line(a, b, c, x, y):
    return a * x + b * y + c

pair_lines = {}
pairs = [(0, 1), (1, 2), (0, 2)]
for (i, j) in pairs:
    pair_lines[(i, j)] = separating_line(i, j)

# Choose two lines giving unique sign patterns at centroids
best = None
import itertools
for (p1, p2) in itertools.combinations(pair_lines.items(), 2):
    signatures = set()
    ok = True
    for idx, (cx, cy) in centroids.items():
        sig = []
        for (_, (a, b, c)) in [p1, p2]:
            sig.append(1 if eval_line(a, b, c, cx, cy) >= 0 else -1)
        sig = tuple(sig)
        if sig in signatures:
            ok = False
            break
        signatures.add(sig)
    if ok and len(signatures) == 3:
        best = [p1, p2]
        break

if best is None:
    # fallback: first two
    best = list(pair_lines.items())[:2]

x_min, x_max = min(xs) - 1, max(xs) + 1
for (i_j, (a, b, c)) in best:
    if abs(b) < 1e-9:
        x_line = -c / a if abs(a) > 1e-9 else (x_min + x_max) / 2
        ax.plot([x_line, x_line], [min(ys) - 1, max(ys) + 1], linestyle="--", color="gray")
    else:
        xv = [x_min, x_max]
        yv = [(-a * x - c) / b for x in xv]
        ax.plot(xv, yv, linestyle="--", color="gray")

# Mark centroids
for idx, (cx, cy) in centroids.items():
    ax.scatter([cx], [cy], c=colors[idx], marker="X", s=120, edgecolor="black")
    ax.text(cx + 0.1, cy + 0.1, f"C{idx}", fontsize=8)

plt.show()
