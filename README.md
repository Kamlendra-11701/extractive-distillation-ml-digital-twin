# AI-Assisted Extractive Distillation: DWSIM Digital Twin, Machine Learning and Process Optimization

<p align="center">

**A simulation-driven chemical engineering framework for ethanol-water extractive distillation using ethylene glycol**

</p>

<p align="center">

`DWSIM` · `ChemSep` · `Python` · `Machine Learning` · `AI-Assisted Optimization` · `Chemical Engineering`

</p>

---

## 📌 Project Overview

This project develops a **simulation-driven workflow for analysing and screening operating conditions in ethanol-water extractive distillation using ethylene glycol (EG) as the entrainer**.

The project combines:

* Rigorous process simulation using **DWSIM/ChemSep**
* Engineering sensitivity analysis
* Performance Index development
* Exploratory Data Analysis (EDA)
* Feature importance analysis
* Machine learning model comparison
* Surrogate-model-based process screening
* AI-assisted generation of new operating conditions
* Validation of AI-recommended conditions using DWSIM

The central idea is to use **chemical engineering simulation to generate process knowledge and data**, followed by machine learning to rapidly screen a large number of feasible operating conditions.

The machine-learning model is therefore treated as a **surrogate for rapid screening**, rather than as a replacement for thermodynamic process simulation.

---

# 🎯 Motivation

Ethanol-water separation is an important industrial separation problem because the ethanol-water system forms an azeotrope, making conventional distillation insufficient for obtaining highly pure ethanol.

Extractive distillation can overcome this limitation by introducing a selective entrainer such as **ethylene glycol**, which modifies the vapour-liquid equilibrium and changes the relative volatility of the components.

The motivation for this project was to understand:

> **How can process simulation, engineering analysis and machine learning be combined to identify promising operating conditions for an extractive distillation system?**

Instead of evaluating only one operating condition, the project investigates how important process variables influence:

* Ethanol purity
* Ethanol recovery
* Ethylene glycol recovery
* Energy consumption
* Overall process performance

---

# 🧪 Process Studied

### Separation system

**Ethanol + Water + Ethylene Glycol**

### Process

**Extractive Distillation**

### Simulation platform

**DWSIM v8.7**

### Column simulation

Two-column separation/recovery system with ethylene glycol used as the entrainer.

---

# 🏗️ Overall Project Architecture

```text
                 ┌─────────────────────────┐
                 │ Literature / Process    │
                 │ Understanding           │
                 └────────────┬────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ DWSIM Process Model     │
                 │ + ChemSep               │
                 └────────────┬────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ 73 Simulation Runs      │
                 └────────────┬────────────┘
                              ↓
              ┌───────────────┴────────────────┐
              ↓                                ↓
   ┌─────────────────────┐          ┌─────────────────────┐
   │ Engineering         │          │ Machine Learning    │
   │ Analysis            │          │                     │
   └──────────┬──────────┘          └──────────┬──────────┘
              ↓                                ↓
       Sensitivity Analysis             Surrogate Model
       PPI Analysis                     Model Comparison
              │                                │
              └───────────────┬────────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ AI-Assisted Screening   │
                 │ 100,000 Candidates      │
                 └────────────┬────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ Top AI Candidates       │
                 └────────────┬────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ DWSIM Validation        │
                 └────────────┬────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ Final Engineering       │
                 │ Findings & Conclusions  │
                 └─────────────────────────┘
```

---

# 📂 Repository Structure

The repository is organised into nine sequential stages:

```text
Project/
│
├── 01_EDA/
│   ├── 01_EDA.py
│   ├── Figures/
│   ├── Results/
│   └── README.md
│
├── 02_Dataset_Preparation/
│   ├── 02_Dataset_Preparation.py
│   ├── Prepared_Data/
│   └── README.md
│
├── 03_DWSIM_Validation/
│   ├── DWSIM simulation files
│   ├── Validation data
│   └── README.md
│
├── 04_Engineering_Analysis/
│   ├── Engineering_Analysis.py
│   ├── Sensitivity plots
│   ├── Correlation analysis
│   ├── PPI analysis
│   └── README.md
│
├── 05_Performance_Index/
│   ├── PPI calculations
│   ├── PPI results
│   └── README.md
│
├── 06_Engineering_Analysis/
│   ├── Sensitivity analysis
│   ├── Correlation analysis
│   ├── Engineering findings
│   └── README.md
│
├── 07_Machine_Learning/
│   ├── 01_EDA.py
│   ├── 02_Dataset_Preparation.py
│   ├── 03_Feature_Importance.py
│   ├── 04_Model_Selection.py
│   ├── Best_Model.pkl
│   ├── Model_Comparison.xlsx
│   ├── Figures/
│   ├── Models/
│   ├── Results/
│   └── README.md
│
├── 08_AI_Optimization/
│   ├── Random / baseline optimization
│   ├── Engineering-guided optimization
│   ├── Top20 results
│   ├── Top100 results
│   ├── All predictions
│   ├── AI vs DWSIM validation
│   └── README.md
│
├── 09_Final_Results/
│   ├── Final findings
│   ├── Final tables
│   ├── Final figures
│   ├── AI validation
│   ├── Conclusions
│   └── README.md
│
└── README.md
```

> The exact folder/file names may differ slightly depending on the current repository version. The numbered stages represent the intended workflow.

---

# ⚙️ Thermodynamic and Simulation Setup

The process model was developed using DWSIM/ChemSep.

The thermodynamic framework used during the project included:

| Setting              | Model            |
| -------------------- | ---------------- |
| K-value approach     | Gamma-Phi        |
| EOS                  | Peng-Robinson 78 |
| Activity coefficient | NRTL             |
| Vapour pressure      | Extended Antoine |
| Enthalpy             | Excess           |
| Simulation tool      | DWSIM v8.7       |
| Column engine        | ChemSep          |

The process was configured to study the influence of several operating variables on separation performance.

---

# 📊 Simulation Dataset

A total of:

> **73 converged process simulations**

were used for the engineering and machine-learning workflow.

The principal process variables were:

| Variable       | Description                  |
| -------------- | ---------------------------- |
| Boilup         | Column 1 boilup ratio        |
| Bottom Flow C2 | Column 2 bottom/recycle flow |
| RR2            | Column 2 reflux ratio        |
| Pressure C2    | Column 2 operating pressure  |
| Temp C1        | Column 1 feed temperature    |

The principal outputs were:

| Output           | Description                         |
| ---------------- | ----------------------------------- |
| Ethanol Purity   | Ethanol concentration in product    |
| Ethanol Recovery | Ethanol recovered to product        |
| EG Recovery      | Ethylene glycol recovery            |
| Total Energy     | Combined process energy requirement |
| PPI              | Overall process performance index   |

---

# 📐 Process Performance Index

A combined Performance Index was developed to evaluate the process using three major criteria:

* Product purity
* Recovery
* Energy consumption

The basic PPI formulation used was:

```text
PPI = 0.4(Purity Score)
    + 0.4(Recovery Score)
    + 0.2(Energy Score)
```

Recovery was treated as a combined measure of ethanol and ethylene glycol recovery:

```text
Average Recovery =
(Ethanol Recovery + EG Recovery) / 2
```

The individual quantities were normalized before being incorporated into the final performance metric.

The purpose of the PPI was not to replace individual engineering metrics, but to provide a **single screening metric for comparing operating conditions**.

---

# 🔎 Engineering Analysis

The engineering analysis was performed before machine learning so that the ML results could be interpreted using process knowledge.

The analysis included:

* Descriptive statistics
* Histograms
* Box plots
* Correlation analysis
* Sensitivity analysis
* Purity analysis
* Recovery analysis
* Energy analysis
* PPI analysis

---

# 📈 Major Engineering Findings

## 1. Column 1 Feed Temperature is the Dominant Variable

Feature importance analysis identified **Column 1 feed temperature (Temp C1)** as the most influential variable for PPI.

Its feature importance was approximately:

```text
Temp C1       0.506
Bottom Flow   0.364
Boilup        0.081
RR2           0.026
Pressure C2   0.023
```

This indicates that temperature and solvent-recycle behaviour dominate the observed variation in process performance within the investigated operating range.

---

## 2. Bottom Flow Strongly Controls EG Recovery

The correlation between Column 2 bottom flow and EG recovery was approximately:

```text
r = 0.994
```

This was the strongest observed relationship in the correlation matrix.

Increasing the Column 2 bottom flow therefore has a very strong relationship with solvent recovery.

An operating value around:

```text
Bottom Flow C2 ≈ 0.09 kg/s
```

was associated with approximately 100% EG recovery in the investigated data.

---

## 3. Temperature Creates a Purity-Recovery Trade-Off

The temperature study revealed an important multi-objective behaviour.

Within the investigated range:

```text
180°C → 240°C
```

ethanol purity remained comparatively stable.

However, at the upper investigated temperature:

```text
250°C
```

a major reduction in ethanol purity was observed.

At the same time, ethanol recovery continued to increase.

This demonstrates a classic chemical-engineering trade-off:

> Increasing thermal input can improve ethanol recovery while simultaneously damaging product purity beyond a certain operating region.

Therefore, maximizing recovery alone is not an appropriate operating strategy.

---

## 4. Boilup Has a Clear Operating Trade-Off

The Boilup sensitivity analysis identified a purity maximum around:

```text
Boilup ≈ 0.44
```

with approximately:

```text
Ethanol Purity ≈ 97.68 wt%
```

Increasing boilup beyond this region improved recovery but reduced ethanol purity.

This indicates that excessive vapour generation does not necessarily improve overall separation performance.

The result demonstrates why an energy/recovery/purity-based performance metric is more informative than optimizing one output independently.

---

## 5. Column 2 Reflux Ratio Has an Energy Penalty

The investigated Column 2 reflux ratio showed that increasing RR2 does not automatically translate into better overall process performance.

The best observed PPI in the original simulation dataset occurred at approximately:

```text
Boilup          = 0.47
Bottom Flow C2  = 0.09
RR2             = 1.0
Pressure C2     = 1.0
Temp C1         = 256°C

PPI             = 0.95127
```

with:

```text
Ethanol Purity       = 96.15 wt%
Ethanol Recovery     ≈ 98.69%
EG Recovery          ≈ 99.88%
Total Energy         ≈ 8611.7 kW
```

This operating point represents the **best observed DWSIM PPI in the available dataset**, rather than an extrapolated AI optimum.

---

# 🧠 Machine Learning

The machine-learning stage was developed after engineering analysis.

The objective was:

> **To learn the relationship between process operating variables and the calculated PPI so that large numbers of feasible operating conditions could be screened rapidly.**

The five input variables were:

```text
Boilup
Bottom Flow C2
RR2
Pressure C2
Temp C1
```

The target variable was:

```text
PPI
```

---

# 🤖 Model Comparison

Four regression algorithms were evaluated using cross-validation.

| Model                 |      Mean R² | Std. Dev. |
| --------------------- | -----------: | --------: |
| **Linear Regression** | **0.721206** |  0.168005 |
| Extra Trees           |     0.662479 |  0.199093 |
| Gradient Boosting     |     0.658997 |  0.209922 |
| Random Forest         |     0.626257 |  0.208761 |

### Selected model

**Linear Regression**

was selected because it produced the highest mean cross-validated R² among the tested models.

The model was then retrained using the complete available dataset before the AI screening stage.

---

# 🔬 Feature Importance

The engineering-guided analysis identified the following relative importance:

| Feature        | Importance |
| -------------- | ---------: |
| Temp C1        | **0.5061** |
| Bottom Flow C2 | **0.3642** |
| Boilup         |     0.0809 |
| RR2            |     0.0262 |
| Pressure C2    |     0.0226 |

The result is consistent with the engineering analysis, where temperature and solvent recovery behaviour showed the strongest relationships with PPI.

---

# 🤖 AI-Assisted Optimization

The AI optimization stage was designed as a **candidate screening problem**.

Instead of asking the ML model to replace DWSIM, the trained model was used to evaluate a very large number of feasible operating conditions at low computational cost.

Two approaches were investigated.

---

## Approach 1 — Random Feasible Sampling

The first approach generated approximately:

```text
100,000
```

random feasible operating conditions within the investigated engineering ranges.

The trained ML model predicted PPI for each candidate.

The candidates were then ranked according to predicted PPI.

The highest-ranking conditions were exported as:

* Top 20
* Top 100
* Best operating condition
* Complete prediction dataset

---

## Approach 2 — Engineering-Guided AI Screening

The second approach incorporated engineering knowledge into candidate generation.

The following variables were allowed to vary:

```text
Boilup
Bottom Flow C2
Temp C1
```

while:

```text
RR2 = 2.5
Pressure C2 = 1.4 bar
```

were kept fixed for this screening strategy.

The sampling distribution was biased toward regions identified during the engineering analysis as potentially promising.

The candidate predictions were also constrained to the observed training-data PPI range.

This approach was used as the **main AI-assisted optimization/screening approach**.

---

# 🧮 AI Candidate Results

The top AI-predicted operating conditions were:

| Rank | Boilup | Bottom Flow C2 | RR2 | Pressure C2 | Temp C1 | Predicted PPI |
| ---: | -----: | -------------: | --: | ----------: | ------: | ------------: |
|    1 |  0.588 |           0.09 | 2.5 |         1.4 |     239 |   **0.93637** |
|    2 |  0.578 |           0.09 | 2.5 |         1.4 |     240 |       0.93305 |
|    3 |  0.580 |           0.09 | 2.5 |         1.4 |     239 |       0.93172 |
|    4 |  0.588 |           0.09 | 2.5 |         1.4 |     237 |       0.93139 |
|    5 |  0.579 |           0.09 | 2.5 |         1.4 |     239 |       0.93114 |

The AI screening therefore identified a region characterised by:

```text
High Boilup
High Bottom Flow
High Column 1 Feed Temperature
```

within the constrained search space.

---

# 🧪 DWSIM Validation of AI Candidates

The top AI-generated candidates were subsequently tested against DWSIM.

The purpose of this stage was critical:

> **To determine whether the ML-predicted performance was reproduced by the underlying process simulator.**

The validation results showed PPI values approximately in the range:

```text
0.900 – 0.905
```

for the five tested AI candidates.

The best validated AI candidate produced approximately:

```text
PPI ≈ 0.9053
```

The corresponding engineering quantities included approximately:

```text
Ethanol Purity      ≈ 94–95 wt%
Ethanol Recovery    ≈ 99.9%
EG Recovery         ≈ 99.9%
Specific Energy     ≈ 3.05 kWh/kg ethanol
```

---

# ⚖️ AI Prediction vs DWSIM

The comparison demonstrates an important limitation of the current surrogate model.

The best AI prediction was:

```text
Predicted PPI ≈ 0.9364
```

while DWSIM validation of the shortlisted conditions produced approximately:

```text
Validated PPI ≈ 0.9053
```

The difference indicates that the surrogate model does not perfectly reproduce the nonlinear thermodynamic behaviour of the simulated process in all regions of the operating space.

This is expected given the relatively small training dataset of only 73 simulations.

Therefore:

> **AI predictions should be treated as screening results and must be verified using DWSIM before being considered engineering recommendations.**

---

# 🏆 Best Observed DWSIM Operating Condition

The strongest operating condition directly observed in the original simulation dataset was:

| Variable         |       Value |
| ---------------- | ----------: |
| Boilup           |        0.47 |
| Bottom Flow C2   |        0.09 |
| RR2              |         1.0 |
| Pressure C2      |     1.0 bar |
| Temp C1          |       256°C |
| Ethanol Purity   |   96.15 wt% |
| Ethanol Recovery |      98.69% |
| EG Recovery      |      99.88% |
| Total Energy     |   8611.7 kW |
| **PPI**          | **0.95127** |

This operating point is important because it represents the **best experimentally/simulation-observed condition in the available 73-run dataset**.

It should not be confused with the AI-generated candidates, which represent model-based screening results.

---

# 🔍 Key Engineering Insights

The complete workflow produced several important engineering observations.

### 1. Purity alone is not enough

The highest ethanol purity condition was not necessarily the condition with the highest overall PPI.

This demonstrates the importance of considering:

* purity
* recovery
* solvent recovery
* energy consumption

simultaneously.

---

### 2. Solvent recovery is a critical process variable

The extremely strong relationship between:

```text
Bottom Flow C2
```

and:

```text
EG Recovery
```

shows that solvent-loop behaviour is one of the most important aspects of the process.

---

### 3. Temperature dominates the surrogate model

Temperature had the highest feature importance:

```text
≈ 50.6%
```

This suggests that thermal conditions strongly influence the calculated process performance within the studied operating region.

---

### 4. High recovery can hide poor product quality

At high feed temperatures, ethanol recovery increased substantially while ethanol purity could deteriorate.

Therefore:

> A process operating point cannot be judged from recovery alone.

---

### 5. Increasing reflux does not automatically improve the process

Higher RR2 values can increase energy consumption without providing sufficient improvement in the combined performance metric.

This highlights the importance of energy-aware optimization.

---

### 6. Machine learning is useful as a screening tool

The ML model can evaluate tens of thousands of candidate operating conditions almost instantly compared with repeatedly solving a rigorous process simulation.

However, the DWSIM validation results show why the surrogate model should remain inside a **simulation-in-the-loop workflow**.

---

# 📊 Project Results at a Glance

| Category                       |                           Result |
| ------------------------------ | -------------------------------: |
| DWSIM simulations              |                           **73** |
| ML input variables             |                            **5** |
| ML algorithms compared         |                            **4** |
| Best mean CV R²                |                       **0.7212** |
| Dominant ML feature            |                      **Temp C1** |
| Temp C1 importance             |                       **0.5061** |
| Bottom Flow importance         |                       **0.3642** |
| Strongest observed correlation | **Bottom Flow C2 ↔ EG Recovery** |
| Correlation coefficient        |                       **0.9944** |
| Best observed DWSIM PPI        |                      **0.95127** |
| AI candidates screened         |                     **~100,000** |
| Best AI predicted PPI          |                      **0.93637** |
| Best validated AI PPI          |                      **~0.9053** |

---

# ⚠️ Limitations

The current study has several important limitations.

### Limited simulation dataset

Only 73 converged DWSIM simulations were available for machine learning.

This limits the ability of the surrogate model to learn highly nonlinear process behaviour.

### Surrogate-model error

The difference between AI predictions and DWSIM validation demonstrates that the surrogate model is not sufficiently accurate to replace rigorous simulation.

### Operating-space limitations

AI candidate generation was restricted to the investigated engineering ranges.

Predictions outside these ranges should not be interpreted as reliable.

### Simplified optimization target

PPI combines several process objectives into one metric.

Changing the weights assigned to purity, recovery and energy would change the resulting optimum.

### Thermodynamic uncertainty

Some simulation specifications, including certain condenser/reboiler assumptions, were based on available information and engineering assumptions.

These assumptions should be refined when detailed industrial process information becomes available.

---

# 🚀 Future Work

The most important next improvement is **additional DWSIM data generation**.

A stronger workflow would be:

```text
Current 73 DWSIM runs
        ↓
Train surrogate model
        ↓
Identify uncertain / promising regions
        ↓
Generate additional DWSIM simulations
        ↓
Add new data
        ↓
Retrain model
        ↓
Repeat
```

This iterative approach would create an **active-learning / simulation-in-the-loop optimization framework**.

Future improvements could include:

* 20–30+ additional multivariable DWSIM simulations
* Nonlinear surrogate models
* Gaussian Process regression
* Random Forest / Gradient Boosting with a larger dataset
* Neural-network surrogate models
* Genetic Algorithm optimization
* Bayesian optimization
* Uncertainty estimation
* Multi-objective optimization
* Pareto-front analysis
* Automated DWSIM validation
* Economic objective functions
* Solvent-loss minimization
* Heat-integration analysis

---

# 🧠 Engineering Significance

The main contribution of this project is not simply the use of machine learning.

The important part is the **integration of process simulation, engineering analysis and data-driven modelling**.

The workflow demonstrates how:

```text
Chemical Engineering Knowledge
            +
Thermodynamic Simulation
            +
Engineering Sensitivity Analysis
            +
Machine Learning
            +
AI Candidate Screening
            +
Rigorous Simulation Validation
```

can be combined into a practical process-development framework.

The ML model provides computational speed, while DWSIM provides the physics-based reference.

This creates a **digital-twin-inspired workflow** in which machine learning assists process engineers without removing the need for rigorous process simulation.

---

# 🛠️ Technology Stack

### Process Simulation

* DWSIM
* ChemSep
* CAPE-OPEN

### Programming

* Python

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Linear Regression
* Extra Trees
* Gradient Boosting
* Random Forest

### Model Management

* Joblib

### Data Storage

* Excel
* CSV

---

# ▶️ Reproducing the Workflow

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
cd <YOUR-REPOSITORY>
```

Install the Python dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn openpyxl joblib
```

The recommended workflow is to execute the numbered stages sequentially.

```text
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09
```

Each stage contains its own README explaining its purpose and outputs.

---

# 📁 Stage-by-Stage Workflow

| Stage                     | Purpose                                           |
| ------------------------- | ------------------------------------------------- |
| `01_EDA`                  | Understand the dataset and identify data patterns |
| `02_Dataset_Preparation`  | Clean and standardise the ML dataset              |
| `03_DWSIM_Validation`     | Establish the simulation/validation basis         |
| `04_Engineering_Analysis` | Study process sensitivity and engineering trends  |
| `05_Performance_Index`    | Calculate and analyse PPI                         |
| `06_Engineering_Analysis` | Consolidated engineering interpretation           |
| `07_Machine_Learning`     | Compare and train surrogate models                |
| `08_AI_Optimization`      | Generate and rank feasible AI candidates          |
| `09_Final_Results`        | Consolidate findings, validation and conclusions  |

---

# 📚 Important Files

Some of the key outputs generated during the project include:

```text
07_Machine_Learning/
├── Model_Comparison.xlsx
├── Best_Model.pkl
├── Figures/
└── Results/

08_AI_Optimization/
├── Top20_AI_Operating_Conditions.xlsx
├── Top100_AI_Operating_Conditions.xlsx
├── All_AI_Predictions.xlsx
└── AI_vs_DWSIM_Validation.xlsx

09_Final_Results/
├── Final_Findings
├── Final_Tables
├── Final_Figures
└── Conclusions
```

---

# 📌 Final Conclusion

This project developed an end-to-end workflow for analysing ethanol-water extractive distillation using ethylene glycol.

The study began with rigorous DWSIM simulation and engineering analysis, followed by the construction of a combined performance index. Machine learning was then used to build a surrogate model capable of rapidly screening large numbers of feasible operating conditions.

The engineering analysis showed that **Column 1 feed temperature and Column 2 bottom flow were the dominant variables within the investigated dataset**, while the relationship between Column 2 bottom flow and EG recovery was particularly strong.

The best directly observed DWSIM operating condition achieved:

> **PPI = 0.95127**

The AI-assisted screening stage evaluated approximately **100,000 candidate operating conditions** and identified promising regions of the operating space. However, DWSIM validation demonstrated that the surrogate predictions were not perfectly accurate.

Therefore, the final conclusion is:

> **Machine learning can significantly accelerate operating-condition screening, but rigorous process simulation remains necessary for final engineering validation.**

The next stage toward a more reliable optimization framework is to expand the DWSIM dataset, improve the surrogate model, and iteratively validate AI-generated candidates.

---

# 👨‍💻 Author

**Kamlendra Singh**
Chemical Engineering
National Institute of Technology Calicut

---

# 📌 Project Status

**Completed:**
DWSIM modelling → Engineering analysis → PPI development → ML model comparison → AI candidate screening → DWSIM validation → Final analysis

**Future development:**
Expanded simulation dataset → Improved surrogate model → Active learning → Multi-objective optimization

---

## ⭐ Key Takeaway

> **The project demonstrates a simulation-first approach to AI-assisted chemical process optimization: use engineering knowledge and rigorous simulation to create the data, use machine learning to accelerate the search, and return to rigorous simulation to validate the result.**
