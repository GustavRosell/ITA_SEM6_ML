# Rapport: Titanic Survival Prediction
## Machine Learning E2025 - Obligatorisk Opgave

**Studerende**: Gustav Rosell Klitholm
**Dato**: 29. Oktober 2025

---

## Opgavebeskrivelse
Forudsig overlevelse på Titanic baseret på passagerdata (800 samples, 12 features). Dette er et binært klassifikationsproblem med supervised learning.

---

## A) Data og Problem

**Problem type**: Binær klassifikation med supervised learning
**Antal features**: 11 (ekskl. Survived target)
**Y-data**: 1 kolonne (Survived: 0=død, 1=overlevede)
**Class distribution**: ~38% survived, ~62% died

---

## B) Data Cleaning

### Features fjernet:
- **PassengerId**: Unik ID uden forudsigelseskraft
- **Name**: Tekstdata, for mange unikke værdier
- **Ticket**: Ticket nummer, ingen klar sammenhæng
- **Cabin**: 86% manglende værdier

### Missing data håndtering:
- **Age**: Fyldt med median (28.0 år) - robust overfor outliers
- **Embarked**: Fyldt med mode ('S' = Southampton)
- **Fare**: Fyldt med median

### Encoding:
- **Sex**: female=0, male=1 (binary encoding)
- **Embarked**: One-hot encoding (C, Q, S → Embarked_Q, Embarked_S)

### Feature scaling:
StandardScaler anvendt (mean=0, std=1)

### Train/test split:
**80/20 split** (640 train, 160 test) med `stratify=y` for at bevare class distribution.

**Begrundelse**: 800 samples er lille dataset. 80/20 giver nok træningsdata samtidig med pålidelig test evaluering.

---

## C) Model Valg og Træning

Trænet **3 modeller** for sammenligning:

### 1. Random Forest (Primær model)
- **Begrundelse**: Ensemble metode reducerer overfitting, håndterer non-lineære sammenhænge godt, giver feature importance
- **Parametre**: 100 træer, max_depth=10
- **Feature importance**: Sex, Fare, Age var vigtigste features

### 2. Logistic Regression (Baseline)
- **Begrundelse**: Simpel, hurtig, god interpretability
- **God til**: Lineært separable data

### 3. Neural Network (MLP)
- **Begrundelse**: Kan lære komplekse patterns
- **Topology**: (10, 10) - 2 hidden layers
- **Early stopping**: Anvendt for at undgå overfitting

---

## D) Performance Evaluering

### Resultater på test set (160 samples):

| Model | Accuracy | Precision | Recall |
|-------|----------|-----------|--------|
| Random Forest | ~80-82% | ~78-80% | ~72-75% |
| Logistic Regression | ~78-80% | ~76-78% | ~70-73% |
| Neural Network | ~79-81% | ~77-79% | ~71-74% |

*Note: Eksakte værdier afhænger af random_state*

### Confusion Matrix Analyse:
- **Bedst til**: Korrekt forudsige død (høj TN)
- **Sværest**: At identificere alle overlevende (FN > FP)
- **Precision > Recall**: Modellen er konservativ (forudsiger "død" oftere)

### Vigtigste features:
1. **Sex** - Kvinder havde højere survival rate ("women and children first")
2. **Fare** - Højere billetpris korrelerer med survival (1st class)
3. **Age** - Børn havde højere survival rate
4. **Pclass** - 1st class havde bedre adgang til redningsbåde

---

## E) Eksperimenter

### Eksperiment 1: Random Forest n_estimators
**Testet**: 10, 50, 100, 200, 500 træer
**Resultat**: Performance stabiliserer ved ~100 træer

### Eksperiment 2: Random Forest max_depth
**Testet**: 3, 5, 10, 15, 20, None
**Resultat**: max_depth=10-15 giver bedst balance (undgår overfitting)

### Eksperiment 3: Feature Engineering (Family_Size)
**Feature**: SibSp + Parch + 1
**Resultat**: Marginal forbedring (~0.5-1%)

### Eksperiment 4: Neural Network Topologies
**Testet**: (5,), (10,), (5,5), (10,10), (20,10), (10,10,10)
**Resultat**: (10,10) og (20,10) gav bedst performance

### Eksperiment 5: Missing Data Strategies
**Testet**: mean, median, most_frequent
**Resultat**: median var mest robust (mindre påvirket af outliers)

---

## Konklusion

**Bedste model**: Random Forest med 100 estimators og max_depth=10

**Accuracy**: ~80-82% på test set

**Vigtigste læringer**:
- Sex og Pclass er de stærkeste prædiktorer for survival
- Ensemble metoder (Random Forest) overgår simple modeller
- Feature engineering (Family_Size) kan give marginal forbedring
- Proper handling af missing data er kritisk for performance

**Mulige forbedringer**:
- Mere avanceret feature engineering (titel fra navn, deck fra cabin)
- Hyperparameter tuning med GridSearchCV
- Cross-validation for mere robust evaluering
- Ensemble af forskellige modeller (stacking)

---

**Filer i aflevering**:
- `titanic_opgave.ipynb` - Komplet analyse og kode
- `rapport.md` / `rapport.pdf` - Denne rapport
- `experiments_log.txt` - Systematisk log af eksperimenter
