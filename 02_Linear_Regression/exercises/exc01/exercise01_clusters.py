import matplotlib.pyplot as plt
import random

# Sæt fast seed for reproducerbare resultater
random.seed(42)

# Definer 3 klyngecentre
centre = [(0.0, 0.0), (6.0, 2.0), (3.0, 7.0)]
farver = ["blue", "orange", "green"]

# Generer punkter for hver klynge
xs, ys, cs = [], [], []

for (cx, cy), farve in zip(centre, farver):
    for _ in range(20):  # 20 punkter per klynge = 60 total
        x = random.gauss(cx, 0.8)  # Normalfordeling omkring centrum
        y = random.gauss(cy, 0.8)
        xs.append(x)
        ys.append(y)
        cs.append(farve)

# Vis klyngerne
plt.scatter(xs, ys, c=cs, edgecolor="black", linewidth=0.5)
plt.title("Tre separable klynger")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(alpha=0.3)
plt.show()