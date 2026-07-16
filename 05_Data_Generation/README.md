# 05 – Machine Learning Dataset Generation

## Overview

This folder contains the final engineering dataset developed for training and evaluating machine learning models for the extractive distillation digital twin.

The dataset was generated from validated process simulations and systematic sensitivity analyses. Each data point represents a physically converged operating condition of the extractive distillation process. Unlike randomly generated synthetic datasets, every operating point follows the thermodynamic behaviour of the validated simulation model, making the dataset suitable for engineering-oriented machine learning applications.

---

## Objective

The primary objective of this stage is to generate a reliable engineering dataset that can be used to:

- Train machine learning regression models
- Predict process performance
- Estimate energy consumption
- Evaluate process efficiency
- Identify optimum operating conditions
- Develop a digital twin of the extractive distillation process

---

## Dataset Description

The final dataset consists of 73 simulation cases covering a wide range of operating conditions. Each simulation was performed using the validated process model.

- **Number of Samples:** 73
- **Number of Input Variables:** 5
- **Number of Output Variables:** 5

### Input Variables

| Variable | Unit | Description |
|:---|:---:|:---|
| **Boilup Ratio** | – | Column 1 boilup ratio |
| **Bottom Flow C2** | kg/h | Bottom product flow specification of Column 2 |
| **RR2** | – | Reflux ratio of Column 2 |
| **Pressure C2** | bar | Operating pressure of Column 2 |
| **Temp C1** | °C | Feed/solvent operating temperature for Column 1 |

### Output Variables

| Variable | Unit | Description |
|:---|:---:|:---|
| **Ethanol Purity** | wt% | Ethanol concentration in the distillate |
| **Ethanol Recovery** | % | Percentage recovery of ethanol |
| **EG Recovery** | % | Percentage recovery of ethylene glycol |
| **Total Energy** | kW | Total condenser and reboiler duty |
| **PPI** | – | Overall Process Performance Index |

---

## Data Generation Methodology

The dataset was developed using the following workflow:

1. Develop the extractive distillation process simulation.
2. Validate the simulation against published literature.
3. Perform one-factor sensitivity analyses for key operating variables.
4. Perform combined operating-condition studies.
5. Collect converged simulation results.
6. Calculate engineering performance indicators including:
   - Ethanol recovery
   - Ethylene glycol recovery
   - Total energy consumption
   - Process Performance Index (PPI)
7. Combine all valid simulation cases into a single machine learning dataset.

> **Data Quality Rule:** Only physically converged simulations were included.

---

## Data Quality

The generated dataset satisfies the following engineering constraints:

- All simulations successfully converged.
- No physically unrealistic operating conditions were included.
- Product purities remain within feasible limits.
- Energy values correspond to converged process simulations.
- Recovery values are calculated directly from material balances.
- PPI is computed using normalized engineering performance metrics.

---

## Dataset Statistics

| Property | Value |
|:---|:---|
| **Total Samples** | 73 |
| **Input Features** | 5 |
| **Output Variables** | 5 |
| **Simulation Software** | DWSIM + ChemSep |
| **Thermodynamic Model** | NRTL |
| **Process Type** | Extractive Distillation |
| **Solvent** | Ethylene Glycol |

---

## Files Included05_Data_Generation
│
├── Generated_Dataset.xlsx
├── Data_Generation_Report.pdf
├── README.md
├── generation.py (optional)
└── Figures
├── Input_Distributions.png
├── Output_Distributions.png
├── Correlation_Matrix.png
├── Scatter_Matrix.png
└── Dataset_Summary.png


---

## Engineering Significance

The generated dataset forms the foundation of the machine learning stage of this project. 

Unlike purely statistical datasets, every sample represents a physically validated process condition obtained from rigorous process simulation. Consequently, the trained machine learning models learn relationships that are consistent with chemical engineering principles rather than arbitrary numerical trends.

---

## Next Stage

The generated dataset is used in **06_Machine_Learning**, where regression models are developed to predict process performance, estimate energy consumption, and identify optimum operating conditions for the extractive distillation system.
