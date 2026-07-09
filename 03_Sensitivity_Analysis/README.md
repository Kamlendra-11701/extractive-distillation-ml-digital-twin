# 03 – Sensitivity Analysis

## Overview

The objective of this phase was to identify the operating variables that have the greatest influence on the performance of the extractive distillation process.

Rather than directly optimizing all process variables simultaneously, a systematic sensitivity analysis was first performed to understand the influence of each operating parameter on separation performance, recovery, convergence behaviour, and energy consumption.

The results obtained from this stage were later used to define the operating ranges for validation, dataset generation, and machine learning optimization.

---

## Objectives

The sensitivity analysis was performed to:

- Understand the effect of individual operating variables.
- Determine physically meaningful operating ranges.
- Identify variables with the greatest influence on process performance.
- Eliminate variables that have negligible impact.
- Ensure stable convergence before optimization.
- Reduce the optimization search space.

---

## Methodology

The study was divided into two independent parts.

### Column 1 (Extractive Distillation Column)

The following operating variable was investigated:

- Boilup Ratio

Performance was evaluated using:

- Ethanol Recovery
- Total Energy Consumption
- Reboiler Duty
- Column Convergence

The sensitivity study identified the practical operating range of the boilup ratio and established the optimum value used for the subsequent validation study.

---

### Column 2 (Solvent Recovery Column)

The following operating variables were investigated independently:

- Bottom Flow
- Reflux Ratio
- Feed Stage
- Number of Stages
- Column Pressure

The response variables monitored were:

- Ethanol Recovery
- Ethylene Glycol Recovery
- Ethanol Purity
- Total Energy Consumption
- Column Convergence

The analysis determined which variables significantly affected process performance and which could be fixed during optimization.

---

## Folder Structure03_Sensitivity_Analysis
│
├── Column1_Sensitivity.xlsx
├── Column1_Sensitivity_Report.pdf
│
├── Column2_Sensitivity.xlsx
├── Column2_Sensitivity_Report.pdf
│
├── column 2 figures/
│   ├── Figure1_BottomFlow.png
│   ├── Figure2_RefluxRatio.png
│   ├── Figure3_FeedStage.png
│   ├── Figure4_NumberStages.png
│   └── Figure5_ColumnPressure.png
│
└── README.md---

## Key Findings

### Column 1

- Boilup ratio strongly influences ethanol recovery.
- Increasing boilup improves separation but increases energy consumption.
- Extremely high boilup ratios produce diminishing returns.
- A practical operating range was identified for further studies.

---

### Column 2

- Bottom Flow was found to be the most influential operating variable.
- Reflux Ratio primarily affects energy consumption.
- Feed Stage showed an optimum around Stage 8.
- Increasing the number of stages beyond 10 produced negligible improvement.
- Operating near atmospheric pressure minimized energy consumption without affecting separation.

---

## Engineering Outcome

The sensitivity analysis provided the engineering basis for all subsequent stages of this project.

It enabled:

- Selection of the validation operating conditions.
- Definition of realistic operating ranges.
- Elimination of non-influential variables.
- Reduction of computational effort during optimization.
- Generation of a physically meaningful dataset for machine learning.

---

## Next Stage

The optimized operating ranges obtained from this study were used to construct the validation matrix presented in the **04_Validation** directory, where simultaneous convergence of both columns was verified before generating the final optimization dataset.
