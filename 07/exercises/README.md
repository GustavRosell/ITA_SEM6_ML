# Week 7 Exercises - ML Pipelines, K-Means & Real-World Projects

## Overview
Denne uge fokuserer på:
- ML pipelines og best practices
- Unsupervised learning (K-Means clustering)
- Dimensionality reduction (PCA)
- Real-world projekt exercises med komplekse datasets

## Exercise List

### Theory & Discussion Exercises (Groups of 2-3)

#### **Exercise 71 - Anomaly Detection** 📊
```
exercise71_anomaly_detection.txt
```
**Diskutér**: Hvordan spotter man anomalier? Hvad gør man ved dem?
**Nøglepunkter**:
- Visualisering, statistik, ML metoder
- Fjern vs behold vs transformér
- Domain knowledge er kritisk

---

#### **Exercise 72 - Underfitting & Overfitting** 🎯
```
exercise72_underfitting_overfitting.txt
```
**Diskutér**: Hvordan fikser man underfitting og overfitting?
**Nøglepunkter**:
- Underfitting: Øg kompleksitet, flere features, træn længere
- Overfitting: Mere data, regularization, cross-validation
- Learning curves til diagnosticering

---

#### **Exercise 73 - Data Compression & PCA** 📉
```
exercise73_data_compression_pca.txt
```
**Diskutér**: Hvorfor compression? Altid godt? Kan PCA reduce overfitting?
**Nøglepunkter**:
- Fordele: Visualisering, hastighed, noise reduction
- Ulemper: Information loss, interpretability
- Trade-offs at overveje

---

#### **Exercise 74 - ML Pipelines** 🚗
```
exercise74_ml_pipelines.txt
```
**Diskutér**: ML pipeline steps for selvkørende biler
**Scenarios**:
- Holde på vejen (lane detection)
- Læse trafikskilte (sign recognition)
- Spotte fodgængere (pedestrian detection)
**Nøglepunkter**: Data → Preprocessing → Features → Training → Deployment → Monitoring

---

### Coding Exercises

#### **Exercise 75 - Iris K-Means Clustering** 🌸
```bash
python3 exercise75_iris_kmeans.py
```
**Formål**: Unsupervised learning på Iris dataset
**Tasks**:
- a) Find optimal k for petal features (k=2,3,4,5)
- b) Test på sepal features
- c) Sammenlign: Petal vs sepal clustering quality

**Key Concepts**:
- K-Means algorithm
- Unsupervised vs supervised learning
- Cluster evaluation uden labels

---

#### **Exercise 76 - Iris PCA + K-Means** 📊
```bash
python3 exercise76_iris_pca.py
```
**Formål**: Dimensionality reduction med PCA, derefter clustering
**Tasks**:
- a) Forstå PCA components (hvilke features bidrager?)
- b) Explained variance (hvor meget info bevares?)
- c) K-Means på reduced data
- d) Sammenlign med original 4D data

**Key Concepts**:
- PCA for visualization
- Variance explained
- Feature combinations
- Trade-off: Simplicity vs information loss

---

#### **Exercise 77 - MNIST Digit Classification** 🔢
```bash
python3 exercise77_mnist.py
```
**Formål**: Klassificér håndskrevne cifre (0-9)
**Models**: Random Forest vs Decision Tree
**Tasks**:
- Baseline performance
- Improve accuracy (hyperparameter tuning)
- Confusion matrix analysis
- Identify hardest digits to recognize
- Compare algorithms

**Key Metrics**:
- Accuracy
- Per-class performance
- Confusion matrix
- Training/inference time

**Experiments**:
- n_estimators (RF): 10, 50, 100, 200
- max_depth: 5, 10, 15, 20, None
- Try other algorithms: Logistic Regression, KNN, Neural Network

---

### Project Exercises (Jupyter Notebooks)

#### **Exercise 78 - Bank Loan Approval** 🏦
```bash
jupyter notebook exercise78_bank_loan.ipynb
```
**Dataset**: bank_loan_data.csv (614 samples, 12 features)
**Target**: Loan approved (Yes/No)
**Features**: Gender, Married, Income, Credit History, Property Area, etc.

**Pipeline**:
1. EDA & visualization
2. Handle missing data
3. One-hot encoding (categorical → numerical)
4. Train/test split
5. Imputation (SimpleImputer)
6. Models: Logistic Regression, Random Forest
7. Threshold sweeping analysis
8. Compare performances

**Key Skills**:
- Real-world messy data
- Feature encoding
- Imbalanced classes
- Threshold tuning

---

#### **Exercise 79 - Student Grades Predictor** 📚
```bash
jupyter notebook exercise79_student_grades.ipynb
```
**Dataset**: StudentGrades.csv
**Target**: Final grade
**Features**: Study time, absences, previous grades, family background

**Focus**:
- Regression problem (continuous target)
- Feature importance analysis
- Predict student performance

---

#### **Exercise 80 - Student Absence & Grades** 📅
```bash
jupyter notebook exercise80_student_absence.ipynb
```
**Dataset**: StudentAbsenceGrade.csv
**Analysis**: Correlation between absence and grades
**Visualization**: Scatter plots, trend lines

---

## Running Exercises

### Setup
```bash
cd "/Users/rosell/IT-A/6. Sem/1_ML/07/exercises"
source "/Users/rosell/IT-A/6. Sem/1_ML/.venv/bin/activate"
```

### Theory Exercises (Read & Discuss)
```bash
cat exercise71_anomaly_detection.txt
cat exercise72_underfitting_overfitting.txt
cat exercise73_data_compression_pca.txt
cat exercise74_ml_pipelines.txt
```

### Python Exercises
```bash
python3 exercise75_iris_kmeans.py        # K-Means
python3 exercise76_iris_pca.py           # PCA + K-Means
python3 exercise77_mnist.py              # MNIST classification
```

### Jupyter Notebooks
```bash
jupyter notebook exercise78_bank_loan.ipynb
jupyter notebook exercise79_student_grades.ipynb
jupyter notebook exercise80_student_absence.ipynb
```

---

## Key Concepts Week 7

### Unsupervised Learning
- **K-Means Clustering**: Group data uden labels
- **Elbow method**: Find optimal k
- **Evaluation**: Silhouette score, visual inspection

### Dimensionality Reduction
- **PCA**: Reduce features mens variance bevares
- **Explained variance ratio**: Hvor meget info bevares?
- **Components**: Linear combinations af original features
- **Trade-off**: Simplicity vs interpretability

### Real-World ML
- **Data cleaning**: Missing values, outliers, errors
- **Feature engineering**: One-hot encoding, scaling, imputation
- **Model comparison**: Logistic Regression vs Random Forest
- **Threshold tuning**: Balance precision vs recall
- **Pipeline**: End-to-end workflow

### ML Pipelines
```
Problem → Data → Clean → Features → Split →
Train → Validate → Evaluate → Deploy → Monitor
```

---

## Resources

See `../resources/` for:
- **MachineLearning_Week_07.pdf** - Main lecture notes
- **Exercises_Week_07.pdf** - Original exercise descriptions
- **Exercises_BankLoan.pdf** - Bank loan project guide
- **Exercise_StudentGradePredictor.pdf** - Student grades guide
- **Exercise_StudentAbsenceGrade.pdf** - Student absence guide
- **Ita_ML_Titanic.pdf** - Titanic project reference
- **4 CSV datasets** (bank_loan_data, student grades, titanic)

---

## Success Criteria

- ✓ Forstå unsupervised learning (K-Means)
- ✓ Anvend PCA til dimensionality reduction
- ✓ Evaluér clustering uden labels
- ✓ Håndter real-world messy data
- ✓ Build complete ML pipeline (data → model → evaluation)
- ✓ Compare multiple algorithms systematically
- ✓ Analyze confusion matrices
- ✓ Tune hyperparameters
- ✓ Document experiments and findings

---

## Exercise Progression

### Week 7 Track:
```
Theory (71-74) → K-Means (75) → PCA (76) →
MNIST (77) → Projects (78-80)
```

**Recommended Order**:
1. Start with theory exercises (groups discussion)
2. Hands-on: K-Means og PCA (75-76) for unsupervised learning
3. Classification: MNIST (77) for supervised learning practice
4. Projects: Choose 1-2 notebooks to work through completely

**Time Allocation**:
- Theory: 30 min
- K-Means & PCA: 1 hour
- MNIST: 1 hour
- Projects: 2-3 hours each

---

## Tips

1. **K-Means**: Clustering quality depends on data structure - Iris petal works better than sepal!
2. **PCA**: Always visualize explained variance - aim for 90%+ retention
3. **MNIST**: Random Forest usually beats Decision Tree (ensemble power!)
4. **Bank Loan**: Missing data handling strategy matters - experiment!
5. **Document everything**: Keep notes on experiments and findings

---

## Comparison: Weeks 5-7

| Week | Topic | Focus | Key Algorithms |
|------|-------|-------|----------------|
| 5 | Neural Nets Intro | Basics, activation functions | MLP |
| 6 | Performance Eval | Confusion matrix, real data | MLP, Pandas |
| 7 | Pipelines & Unsupervised | K-Means, PCA, projects | K-Means, PCA, RF, DT |

Week 7 = Bringing it all together! 🎉
