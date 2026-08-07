# 07 – Machine Learning

## Overview
This stage develops a machine-learning surrogate model for the extractive distillation process.
The objective is to learn the relationship between selected process operating conditions and the Process Performance Index (PPI) obtained from the DWSIM simulation dataset.
The trained surrogate model is intended to provide a fast prediction of process performance and will subsequently be used in `08_AI_Optimization` for searching and ranking new operating conditions.

**Scope:** This stage covers dataset preparation, feature analysis, model comparison, and final model training.
AI-based operating-condition generation and optimization are intentionally excluded and are performed in Stage 08.

## Machine Learning Workflow
The workflow implemented in this stage is:Engineering Dataset
│
▼
Exploratory Data Analysis
│
▼
Dataset Preparation
│
▼
Feature Importance Analysis
│
▼
Train/Test Split
│
▼
Model Comparison
│
▼
Cross-Validation
│
▼
Best Model Selection
│
▼
Final Model Training
│
▼
Best_Model.pkl
│
▼
08 – AI Optimization


## Dataset
The machine-learning dataset contains 73 DWSIM simulation runs.

### Input Features
The following five process operating variables are used as model inputs:

| Feature | Description |
|---|---|
| **Boilup** | Column 1 boilup ratio |
| **Bottom Flow C2** | Bottom flow rate of Column 2 |
| **RR2** | Reflux ratio of Column 2 |
| **Pressure C2** | Pressure of Column 2 |
| **Temp C1** | Feed temperature of Column 1 |

### Target Variable
The machine-learning target is:
* **PPI** – Process Performance Index

PPI combines the major process-performance objectives identified during the engineering analysis, including product purity, recovery, and energy consumption.

---

## 01 – Exploratory Data Analysis
`01_EDA.py` performs an initial investigation of the simulation dataset.
The analysis includes:
* Descriptive statistics
* Histograms
* Box plots
* Correlation analysis
* Outlier identification
* Distribution analysis

### Important EDA Findings
The dataset covers the following operating ranges:
* **Boilup:** 0.35–0.59
* **Bottom Flow C2:** 0.06–0.09 kg/s
* **RR2:** 0.5–3.0
* **Pressure C2:** 0.8–2.0 bar
* **Temp C1:** 180–256°C
* **PPI:** 0.441–0.951

The correlation analysis showed that:
* Total Energy has a strong negative relationship with PPI.
* EG Recovery has a strong positive relationship with PPI.
* Ethanol Recovery also has a positive relationship with PPI.
* Bottom Flow C2 has an extremely strong relationship with EG Recovery.
* Feed Temperature has a strong relationship with Ethanol Recovery.
* Pressure C2 has comparatively weak linear relationships with most performance variables.

The EDA therefore confirmed that the dataset contains meaningful engineering relationships that can be learned by a surrogate model.

---

## 02 – Dataset Preparation
`02_Dataset_Preparation.py` prepares the dataset for machine-learning applications.
The preparation stage includes:
* Loading the engineering dataset
* Checking missing values
* Checking data types
* Selecting model inputs
* Separating input features and target variable
* Preparing the dataset for model training

The prepared dataset is then supplied to the subsequent feature-analysis and model-selection stages.

---

## 03 – Feature Importance
`03_Feature_Importance.py` investigates the relative influence of the operating variables on PPI.
Feature analysis is used to support the engineering interpretation of the machine-learning model and to identify which operating variables are most relevant for process optimization.
This stage is not used to generate new operating conditions. Its purpose is to understand the structure of the available simulation data.

---

## 04 – Model Comparison
`04_Model_Comparison.py` compares multiple regression algorithms using the prepared dataset.
The investigated models were:
* Linear Regression
* Extra Trees
* Gradient Boosting
* Random Forest

An 80/20 train-test split was used during the model-development workflow.
Cross-validation was used for model selection rather than relying only on performance from a single split. Cross-validation provides a more robust estimate of model performance by evaluating the estimator across multiple train/test partitions.

### Cross-Validation Results

| Model | Mean R² | Standard Deviation |
|---|---|---|
| **Linear Regression** | **0.7212** | **0.1680** |
| Extra Trees | 0.6625 | 0.1991 |
| Gradient Boosting | 0.6590 | 0.2099 |
| Random Forest | 0.6263 | 0.2088 |

### Model Selection
Linear Regression was selected as the final surrogate model because it achieved the highest mean cross-validation R² among the evaluated models.
The result also indicates that, for the present dataset, the more complex ensemble models did not provide better cross-validated performance than the simpler linear model.
Linear regression models the target as a linear combination of the input features and estimates the coefficients by minimizing the residual sum of squares.

---

## 05 – Final Model
`05_Final_Model.py` trains the selected model using the complete available dataset after the model-selection stage.
The final model consists of a preprocessing and regression pipeline:

Input Features
│
▼
StandardScaler
│
▼
Linear Regression
│
▼
Predicted PPI


The fitted pipeline is stored as:
`Models/Best_Model.pkl`

Keeping preprocessing and the regression model together in a single pipeline ensures that the same transformation applied during model development is automatically applied when the model is later used for prediction.

### Final Model Summary
* **Selected algorithm:** Linear Regression
* **Preprocessing:** StandardScaler
* **Target:** PPI
* **Dataset size:** 73 simulation runs
* **Train/Test split used during development:** 80/20
* **Model selection:** Cross-validation
* **Final training:** Complete available dataset

The final model is not intended to replace DWSIM. It acts as a surrogate model that provides rapid estimates of PPI within the operating domain represented by the simulation dataset.

---

## Repository Structure
```text
07_Machine_Learning/
│
├── Figures/
│   ├── EDA/
│   │   ├── Histograms/
│   │   ├── Boxplots/
│   │   └── Correlation_Heatmap.png
│   ├── Model_Comparison.png
│   ├── Cross_Validation.png
│   ├── Feature_Importance.png
│   ├── Predicted_vs_Actual.png
│   └── Residual_Plot.png
│
├── Models/
│   ├── Best_Model.pkl
│   └── Model_Metadata.txt
│
├── Results/
│   ├── Correlation_Matrix.xlsx
│   ├── Descriptive_Statistics.xlsx
│   ├── Outlier_Summary.xlsx
│   ├── Model_Comparison.xlsx
│   ├── Feature_Importance.xlsx
│   └── CrossValidation_Results.xlsx
│
├── 01_EDA.py
├── 02_Dataset_Preparation.py
├── 03_Feature_Importance.py
├── 04_Model_Comparison.py
├── 05_Final_Model.py
└── README.md
Key Conclusions
The machine-learning stage established the following:

The DWSIM dataset contains sufficient variation in operating conditions and process performance for surrogate modelling.

The engineering analysis identified meaningful relationships between the operating variables and PPI.

Several regression algorithms were evaluated rather than selecting a model arbitrarily.

Cross-validation was used to obtain a more reliable basis for model selection.

Linear Regression achieved the highest mean cross-validation R² of 0.7212 among the tested models.

The final Linear Regression model was retrained using the complete dataset to maximize the information available to the surrogate model.

The trained model was saved as Best_Model.pkl and serves as the prediction engine for the next stage.

Transition to Stage 08
The output of this stage is the trained surrogate model: Best_Model.pkl

This model is carried forward into 08_AI_Optimization. In Stage 08, the trained surrogate model will be used to:

Generate candidate operating conditions within the validated engineering ranges.

Predict PPI for the candidate conditions.

Rank the predicted operating conditions.

Identify high-performing candidate conditions.

Select a small number of promising conditions.

Validate the selected conditions using DWSIM.

Therefore, no AI-generated operating conditions or optimization results are included in this stage.

Important Limitation
The surrogate model is trained from only 73 DWSIM simulation runs. Therefore, predictions should primarily be interpreted within the operating domain represented by the training dataset.
The machine-learning model is used as a computationally efficient surrogate, while final engineering decisions and candidate operating conditions are verified through DWSIM simulation.

Technologies
Python

Pandas

NumPy

Matplotlib

Scikit-learn

Joblib

Excel

Scikit-learn's model-selection tools provide cross-validation functionality for evaluating estimator performance and supporting model selection.

Next Stage
07 – Machine Learning → 08 – AI Optimization
The trained surrogate model now becomes the computational engine for the optimization stage.
