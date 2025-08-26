import matplotlib.pyplot as plt
import numpy as np

# Generer lineære data med støj
# Vi simulerer virkeligheden hvor data aldrig er perfekt
print("Genererer kunstige data...")

# Step 1: Lav X-værdier (input)
# np.random.rand(100, 1) giver 100 tilfældige tal mellem 0 og 1
# Vi ganger med 2 for at få tal mellem 0 og 2
X = 2 * np.random.rand(100, 1)
print(f"X-værdier: fra {X.min():.2f} til {X.max():.2f}")

# Step 2: Lav y-værdier (output) med en lineær sammenhæng
# y = 4 + 3*x  <-- Dette er den "sande" lineære sammenhæng
# Men vi tilføjer støj for at simulere virkeligheden
y_perfekt = 4 + 3 * X                    # Perfekt linje (ingen støj)
støj = np.random.randn(100, 1)           # Tilfældige tal fra normalfordeling
y = y_perfekt + støj                     # Tilføj støj til den perfekte linje
#   ^               ^
#   |               |
# Perfekt      Random støj
# linje        (std = 1.0)

print(f"y-værdier: fra {y.min():.2f} til {y.max():.2f}")
print(f"Støj niveau: mellem {støj.min():.2f} og {støj.max():.2f}")

# Step 3: Vis datapunkterne
# "b." betyder blå prikker
plt.plot(X, y, "b.", label="Datapunkter (med støj)")
plt.axis([0, 2, 0, 15])                  # Sæt aksegrænser
plt.xlabel("X")
plt.ylabel("y") 
plt.title("Lineære data med støj: y = 4 + 3x + støj")
plt.legend()
plt.grid(True, alpha=0.3)                # Tilføj gitter for bedre læsning
plt.show()

print("Bemærk: Punkterne ligger cirka på en lige linje, men ikke perfekt!")
print("Det er støjen der gør dataene realistiske.")