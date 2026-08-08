# 08 – AI-Assisted Process Optimization

## Overview

This stage uses the machine-learning surrogate model developed in Stage 07 to perform rapid screening of feasible operating conditions for the ethanol-water extractive distillation process.

Instead of running thousands of operating conditions directly in DWSIM, the trained ML model is used as a fast prediction layer to estimate the Process Performance Index (PPI) for newly generated operating conditions.

The purpose of this stage is:

- To explore the validated operating region computationally.
- To generate a large number of feasible operating conditions.
- To predict PPI using the trained ML model.
- To rank candidate operating conditions.
- To identify promising conditions for subsequent DWSIM validation.

The AI optimization stage therefore acts as a screening and candidate-generation layer rather than replacing rigorous process simulation.

---

## Optimization Workflow

The optimization workflow is:DWSIM Engineering Dataset
↓
Trained ML Model
↓
Generate Feasible Operating Conditions
↓
Predict PPI
↓
Remove Physically Infeasible Predictions
↓
Rank by Predicted PPI
↓
Select Top Candidate Conditions
↓
DWSIM Validation
↓
Final Results


Only the final DWSIM-validated conclusions are reported in Stage 09.

---

# 01 – Random Search Optimization

## Objective

The first optimization approach uses random sampling to explore the feasible operating region.

A total of approximately 100,000 operating conditions are generated within the engineering limits established from the DWSIM dataset.

### Optimization variables

| Variable | Operating Range |
|---|---:|
| Boilup | 0.35 – 0.59 |
| Bottom Flow C2 | 0.06 – 0.09 |
| RR2 | 1.0 – 3.0 |
| Pressure C2 | 0.8 – 2.0 |
| Temp C1 | 180 – 240 °C |

Each generated condition is passed through the trained ML model to obtain a predicted PPI.

The conditions are then ranked from highest to lowest predicted PPI.

## Outputs

### `All_AI_Predictions.xlsx`

Contains the complete set of generated operating conditions and their predicted PPI values.

### `Top100_AI_Operating_Conditions.xlsx`

Contains the 100 highest-ranked predicted operating conditions.

### `Top20_AI_Operating_Conditions.xlsx`

Contains the 20 highest-ranked predicted operating conditions.

### `Best_AI_Operating_Condition.xlsx`

Contains the single highest predicted operating condition from the random-search approach.

---

# 02 – Engineering-Guided AI Optimization

## Objective

The second approach refines the random-search strategy using engineering knowledge obtained from the sensitivity analysis and DWSIM simulation results.

Rather than sampling all variables uniformly, the candidate generation is biased toward operating regions that showed better process behaviour during engineering analysis.

This approach combines:

- Machine-learning prediction
- Engineering constraints
- Previously observed PPI limits
- Sensitivity-analysis findings
- Validated operating ranges

## Fixed Variables

For this optimization approach:

| Variable | Treatment |
|---|---|
| RR2 | Fixed at 2.5 |
| Pressure C2 | Fixed at 1.4 bar |

The remaining influential variables are explored using engineering-guided sampling.

## Guided Sampling

Approximately 80% of the generated candidates are sampled from promising regions identified from the engineering analysis, while the remaining candidates are sampled across the wider feasible range.

This maintains exploration of the operating space while increasing the density of candidates in potentially favourable regions.

### Sampling ranges

| Variable | Overall Range | Guided Region |
|---|---:|---:|
| Boilup | 0.35 – 0.59 | 0.45 – 0.58 |
| Bottom Flow C2 | 0.06 – 0.09 | 0.075 – 0.09 |
| Temp C1 | 180 – 240 °C | 220 – 240 °C |

## Prediction Filtering

The trained model predicts PPI for every generated candidate.

Predictions are then constrained to the PPI range observed in the original engineering dataset.

This prevents the optimization algorithm from selecting model predictions that extrapolate beyond the experimentally/simulated observed performance range.

The candidates are subsequently ranked according to predicted PPI.

---

## Outputs

### `All_AI_Predictions.xlsx`

Complete set of feasible engineering-guided operating conditions and their predicted PPI values.

### `Top100_AI_Operating_Conditions.xlsx`

Top 100 candidates ranked by predicted PPI.

### `Top20_AI_Operating_Conditions.xlsx`

Top 20 candidates ranked by predicted PPI.

### `Best_Operating_Condition.xlsx`

Highest-ranked operating condition identified by the engineering-guided AI optimization.

### `Top5_DWSIM_Validation.xlsx`

Contains the five highest-ranked AI candidates selected for subsequent DWSIM validation.

This file represents the **candidate selection stage**. The actual comparison between AI predictions and DWSIM results is reported in Stage 09.

---

# Comparison of the Two Optimization Approaches

| Feature | Random Search | Engineering-Guided |
|---|---|---|
| Candidate generation | Uniform random sampling | Biased engineering-guided sampling |
| Number of candidates | ~100,000 | ~100,000 |
| Engineering constraints | Yes | Yes |
| Uses sensitivity findings | No | Yes |
| RR2 | Variable | Fixed |
| Pressure C2 | Variable | Fixed |
| PPI range filtering | No | Yes |
| Purpose | Baseline exploration | Refined candidate generation |

The random-search approach provides a baseline for unrestricted exploration of the feasible operating space.

The engineering-guided approach incorporates information obtained from the preceding engineering analysis and therefore focuses computational effort on regions considered more promising.

---

# Important Interpretation

The AI-generated operating conditions are predictions from a surrogate machine-learning model.

They should not be interpreted as directly validated process operating conditions.

The optimization workflow is therefore:

**ML prediction → candidate ranking → DWSIM validation**

Only operating conditions subsequently simulated and verified in DWSIM are considered validated.

The final AI-versus-DWSIM comparison, validation results, selected operating condition, and overall project conclusions are intentionally excluded from this stage and are presented in:

`09_Final_Results/`

---

# Relationship with Previous Stages

### Stage 06 – Engineering Analysis

Identified:

- influential operating variables
- favourable operating regions
- process trade-offs
- PPI behaviour
- engineering constraints

↓

### Stage 07 – Machine Learning

Developed:

- prepared modelling dataset
- model comparison
- selected ML model
- trained surrogate model

↓

### Stage 08 – AI Optimization

Performs:

- large-scale candidate generation
- PPI prediction
- candidate ranking
- engineering-guided search
- selection of candidates for DWSIM validation

↓

### Stage 09 – Final Results

Contains:

- DWSIM validation
- AI vs DWSIM comparison
- final validated operating condition
- final performance improvement
- overall engineering conclusions
- project limitations
- final recommendations

---

# Software

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Excel
- DWSIM

DWSIM is used as the rigorous process-simulation environment, while the ML model is used as a computationally efficient surrogate for screening candidate operating conditions.
