"""
Løsning og Forklaring til SVM Øvelse 1

**Spørgsmål: Hvad er intuitionen bag en SVM?**

**Svar:**
Kerneintuitionen bag en Support Vektor Maskine (SVM), især for data der ikke er lineært separerbare, er følgende:

1.  **Problemet:** Nogle gange kan dine data ikke adskilles af en enkelt lige linje (eller et fladt plan i højere dimensioner). `make_circles`-datasættet i dette script er et perfekt eksempel; du kan ikke tegne én linje for at placere de blå prikker på den ene side og de gule på den anden.

2.  **"Løftet":** SVM'ens magiske trick er at projicere dataene ind i et højere-dimensionelt rum, hvor de *kan* adskilles af et lineært plan (et hyperplan). Dette script demonstrerer dette ved at tage 2D-data `(x1, x2)` og mappe dem til et 3D-rum ved hjælp af funktioner som `(x1, x2, x1^2 + x2^2)`. Når du ser på 3D-plottet, kan du se, at de to cirkler nu er adskilt i højden, så et fladt plan let kan skubbes ind imellem dem.

3.  **Kerne-tricket (The Kernel Trick):** At udføre denne transformation for hvert datapunkt kan være beregningsmæssigt dyrt. "Kerne-tricket" er en matematisk genvej, der lader SVM'en opnå det samme resultat, *som om* den havde projiceret dataene ind i en højere dimension, men uden nogensinde rent faktisk at udføre transformationen. Den beregner relationerne (prikprodukterne) mellem punkter i det højere-dimensionelle rum, mens den stadig arbejder i det oprindelige, lavere-dimensionelle rum.

Kort sagt er intuitionen: **Hvis du ikke kan adskille dataene med en linje, så løft dem op i en højere dimension, hvor du kan, og brug kerne-tricket til at gøre det effektivt.**

Dette script viser visuelt "løftet" og bruger derefter en brugerdefineret kerne til at vise det endelige resultat af kerne-tricket: en ren, ikke-lineær grænse i det oprindelige 2D-rum.
"""

# -*- coding: utf-8 -*-
"""
Oprettet ons aug 11 21:03:42 2021

@author: Sila
"""

# Hvad gør man med eksempler, der ikke er lineært separerbare?
#
# Et visuelt eksempel for at hjælpe med intuitionen
#

# Hvis vi kunne finde et højere-dimensionelt rum, hvor vores punkter var lineært separerbare, kunne vi gøre følgende:
#
#    Map de oprindelige features til det højere, transformerede rum (feature mapping)
#    Udfør lineær SVM i dette højere rum
#    Find et sæt vægte, der svarer til beslutningsgrænsens hyperplan
#    Map dette hyperplan tilbage til det oprindelige 2D-rum for at få en ikke-lineær beslutningsgrænse


import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

from sklearn.datasets import make_circles
from sklearn.svm import SVC

def feature_map_1(X):
    return np.asarray((X[:,0], X[:,1], X[:,0]**2 + X[:,1]**2)).T

# Generer datasæt og feature-map
X, y = make_circles(100, factor=.1, noise=.1)
Z = feature_map_1(X)

# 2D scatter plot
fig = plt.figure(figsize = (16,8))
ax = fig.add_subplot(1, 2, 1)
ax.scatter(X[:,0], X[:,1], c = y, cmap = 'viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Oprindeligt datasæt')

# 3D scatter plot
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.scatter3D(Z[:,0],Z[:,1], Z[:,2],c = y, cmap = 'viridis' )
ax.set_xlabel('$z_1$')
ax.set_ylabel('$z_2$')
ax.set_zlabel('$z_3$')
ax.set_title('Transformeret datasæt')

plt.show()

def feature_map_2(X):
    return np.asarray((X[:,0], X[:,1], np.exp( -( X[:,0]**2 + X[:,1]**2)))).T

# Generer datasæt og feature-map
X, y = make_circles(100, factor=.1, noise=.1)
Z = feature_map_2(X)

# 2D scatter plot
fig = plt.figure(figsize = (16,8))
ax = fig.add_subplot(1, 2, 1)
ax.scatter(X[:,0], X[:,1], c = y, cmap = 'viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Oprindeligt datasæt')

# 3D scatter plot
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.scatter3D(Z[:,0],Z[:,1], Z[:,2],c = y, cmap = 'viridis' )
ax.set_xlabel('$z_1$')
ax.set_ylabel('$z_2$')
ax.set_zlabel('$z_3$')
ax.set_title('Transformeret datasæt')

plt.show()

def feature_map_3(X):
    return np.asarray(( np.sqrt(2) *X[:,0] * X[:,1], X[:,0]**2, X[:,1]**2)).T

# Generer datasæt og feature-map
X, y = make_circles(100, factor=.1, noise=.1, random_state = 0)
Z = feature_map_3(X)

# 2D scatter plot
fig = plt.figure(figsize = (16,8))
ax = fig.add_subplot(1, 2, 1)
ax.scatter(X[:,0], X[:,1], c = y, cmap = 'viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Oprindelige data')

# 3D scatter plot
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.scatter3D(Z[:,0],Z[:,1], Z[:,2],c = y, cmap = 'viridis' )
ax.set_xlabel('$z_1$')
ax.set_ylabel('$z_2$')
ax.set_zlabel('$z_3$')
ax.set_title('Transformerede data: ')

# SVM ved brug af klassen SVC er forklaret her:
# https://www.tutorialspoint.com/scikit_learn/scikit_learn_support_vector_machines.htm

# SVM ved brug af kerne 3 - feature map 3
clf = SVC(C = 1, kernel = 'linear')
clf.fit(Z, y)

w = clf.coef_.flatten()
b = clf.intercept_.flatten()
print('vægte (w)=',w,'bias (b)=',b)

# Opret x,y
xx, yy = np.meshgrid(np.linspace(-1,1), np.linspace(0,1))

# Beregn korresponderende z
boundary = (-w[0] * xx - w[1] * yy - b) * 1. /w[2]


# Plot overfladen
ax.plot_surface(xx, yy, boundary, alpha = .3)
ax.set_ylim(.2,1.2)
ax.set_zlim(-.9,1.1)

plt.show()

# Brug en brugerdefineret kerne til SVC

def my_kernel_1(X,Y):
    return np.dot(feature_map_1(X),feature_map_1(Y).T )

def my_kernel_2(X,Y):
    return np.dot(feature_map_2(X),feature_map_2(Y).T )

def my_kernel_3(X,Y):
    return np.dot(feature_map_3(X),feature_map_3(Y).T )

# SVM ved brug af klassen SVC er forklaret her:
# https://www.tutorialspoint.com/scikit_learn/scikit_learn_support_vector_machines.htm

clf = SVC(kernel=my_kernel_3, C = 1)
# Kerne-beregning
clf.fit(X, y)

# Initialiser data
h = .01 # Skridtstørrelse i mesh-gridet
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Forudsig på mesh-grid
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Vis resultatet i et farveplot
Z = Z.reshape(xx.shape)
plt.figure(figsize = (7,7))
plt.contourf(xx, yy, Z,1, colors = ['darkblue','yellow'], alpha = .1)
plt.contour(xx, yy, Z, cmap = 'viridis')

# Plot også træningspunkterne
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors = 'k')
plt.title('Support Vektor Maskine med polynomisk kerne')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')

plt.show()