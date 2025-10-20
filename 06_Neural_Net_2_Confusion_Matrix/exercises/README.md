# Week 6 Exercises - Neural Networks & Confusion Matrix

## Overview
Denne uge fokuserer på performance evaluering af neural networks og arbejde med real-world data ved hjælp af Pandas.

## Exercise List

### Theory Exercises (✓ Complete)
- **Exercise 62**: Confusion Matrix beregninger
- **Exercise 63**: Prediction Accuracy formler
- **Exercise 64**: Recall vs Precision (zip code eksempel)

### Coding Exercises

#### **Exercise 61 - Moons MLP** (Warmup)
```bash
python3 exercise61_moons_mlp.py
```
**Formål**: Klassificér Moons dataset
**Spørgsmål**:
- Minimum antal hidden layers?
- Minimum neuroner per layer?
- Effekt af noise og sample size?

---

#### **Exercise 65 - Titanic** (⭐ MAIN EXERCISE)
```bash
python3 exercise65_titanic.py
```
**Formål**: Forudsig Titanic overlevelse (Age, Pclass → Survived)
**Dataset**: 400 train, 100 test samples
**Baseline**: 64% (altid forudsige "død")
**Mål**: > 64% accuracy!

**Key Skills**:
- Pandas data loading og manipulation
- Missing data handling (fillna, dropna)
- Feature scaling med StandardScaler
- Confusion matrix tolkning
- Systematisk hyperparameter tuning

**Experimentér med**:
- Network topology
- Missing data strategies
- With/without scaler
- Batch sizes
- Epochs
- Activation functions

**Log resultater i**: `exercise65_experiments.txt`

---

#### **Exercise 66a - Spine Dataset**
```bash
python3 exercise66a_spine_dataset.py
```
**Formål**: Klassificér Normal vs Abnormal spine conditions
**Features**: 6 spine measurements
**Output**: Confusion matrix heatmap (seaborn)

---

#### **Exercise 66b - Own Dataset** (Project)
Se `exercise66b_create_dataset.txt` for instruktioner.
Find eller skab eget dataset og træn MLP.

---

## Key Concepts

### Confusion Matrix
```
                Predicted: 0    Predicted: 1
Actual: 0           TN              FP
Actual: 1           FN              TP
```

### Performance Metrics
- **Accuracy** = (TP + TN) / Total
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN)
- **F1-score** = 2 × (Precision × Recall) / (Precision + Recall)

### Pandas Basics
```python
import pandas as pd

# Load CSV
data = pd.read_csv('file.csv', header=0)

# Handle missing data
data.fillna(value, inplace=True)  # Fill with value
data.dropna(inplace=True)         # Remove rows

# Split data
train = data.head(400)
test = data.tail(100)

# Drop columns
data.drop('column_name', axis=1, inplace=True)
```

---

## Running Exercises

### Setup
```bash
cd "/Users/rosell/IT-A/6. Sem/1_ML/06_Neural_Net_2_Confusion_Matrix/exercises"
source "/Users/rosell/IT-A/6. Sem/1_ML/.venv/bin/activate"
```

### Run Individual Exercises
```bash
python3 exercise61_moons_mlp.py
python3 exercise65_titanic.py
python3 exercise66a_spine_dataset.py
```

---

## Resources
Se `../resources/` for:
- Exercises_Week_06.pdf (alle opgaver)
- ML_Syllabus_Week_06.pdf (litteratur)
- titanic_train_500_age_passengerclass.csv
- dataset_spine.csv
- Pandas tutorials og guides

---

## Success Criteria
- ✓ Forstå confusion matrix (TP, TN, FP, FN)
- ✓ Beregn accuracy, precision, recall
- ✓ Håndtér missing data med Pandas
- ✓ Systematisk eksperimentering med hyperparametre
- ✓ Opnå > 64% på Titanic dataset
- ✓ Visualisér confusion matrix med heatmap

---

## Tips
1. **Start med theory (62-64)** - forstå metrics først!
2. **Moons (61)** - warmup for at genopfriske Week 5
3. **Titanic (65)** - brug mest tid her, eksperimentér systematisk
4. **Spine (66a)** - øv confusion matrix visualization
5. **Brug exercise65_experiments.txt** - dokumentér ALT!
