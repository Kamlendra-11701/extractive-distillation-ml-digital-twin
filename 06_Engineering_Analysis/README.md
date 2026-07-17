# 06 – Engineering Analysis

## Overview

This stage investigates how the major operating variables influence the performance of the extractive distillation process. 

Unlike the validation stage, which confirms that the simulation reproduces literature behaviour, this analysis explores the engineering behaviour of the process over a wide operating window. A structured sensitivity study was performed by systematically varying key operating parameters while monitoring product quality, component recovery, and energy consumption.

The objective was to identify operating trends, determine practical operating limits, and establish the most suitable conditions for subsequent machine learning optimisation.

---

## Operating Variables Investigated

The following process variables were analysed:

- Column 1 Boilup Ratio
- Column 2 Bottom Flow Rate
- Column 2 Reflux Ratio
- Column 2 Operating Pressure
- Column 1 Feed Temperature

In addition, multivariable simulations were performed to investigate the interaction between process variables within the stable operating region.

---

## Engineering Analyses Performed

### 1. Column 1 Boilup Ratio
The influence of boilup ratio on **Ethanol Purity**, **Ethanol Recovery**, and **Total Energy** was investigated. This study identifies the trade-off between separation quality, recovery, and utility consumption.

### 2. Column 2 Bottom Flow
The solvent recovery column was analysed by varying the bottom product flow rate. The corresponding responses evaluated were **Ethylene Glycol Recovery** and the **Process Performance Index (PPI)**. This determines the minimum solvent recycle required to maintain an efficient solvent loop.

### 3. Column 2 Reflux Ratio
The influence of reflux ratio on **Total Energy** and the **Process Performance Index (PPI)** was investigated to determine the most energy-efficient operating condition.

### 4. Column 1 Feed Temperature
Feed temperature was varied over a broad operating range to study **Ethanol Purity** and **Ethanol Recovery**. This analysis identifies the thermal operating window of the extractive distillation process and the temperature threshold at which separation performance begins to collapse.

### 5. Multivariable Analysis
Additional simulations were performed by simultaneously varying multiple operating variables around the stable operating region. These simulations provide insights into complex variable interactions, non-linear process trends, and realistic multi-dimensional dataset generation used directly for machine learning surrogate model training.

---

## Correlation Analysis

A Pearson correlation analysis was performed to investigate relationships between process variables and process responses. The correlation heatmap provides a quantitative assessment of:
- Variable dependency
- Sensitivity thresholds
- Process coupling loops

This directly identifies which operating parameters most strongly govern product purity, recovery, and structural energy consumption.

---

## Major Engineering Findings

### Column 1 Boilup Ratio
- Maximum ethanol purity (**97.68 wt%**) occurred at a boilup ratio of approximately **0.44**.
- Increasing boilup beyond this point improved ethanol recovery but reduced product purity due to solvent dilution.
- Higher boilup ratios within certain windows reduced overall specific energy consumption.
- This demonstrates the classical non-linear trade-off between purity and recovery in extractive distillation columns.

### Column 2 Bottom Flow
- Ethylene glycol recovery increased almost linearly with bottom flow rate.
- Approximately **0.09 kg/s** achieved nearly complete solvent recovery.
- Lower bottom flow rates resulted in significant solvent loss into product loops and lower process performance.

### Column 2 Reflux Ratio
- Increasing reflux ratio produced negligible improvements in separation quality.
- Utility consumption increased substantially as the reflux ratio scaled up.
- The highest overall Process Performance Index (PPI) was obtained at the lowest stable reflux ratio investigated.

### Feed Temperature
- Between **180–240°C**, ethanol purity remained relatively stable.
- Ethanol recovery increased steadily with increasing temperature.
- At approximately **250°C**, ethanol purity collapsed abruptly while recovery remained high. This marks a clear practical thermal boundary for stable extractive distillation operation.

### Variable Interactions
- **Feed temperature** has the strongest influence on ethanol recovery.
- **Bottom flow rate** strongly governs solvent (EG) recovery loop closing.
- **Boilup ratio** influences both separation quality and component recovery simultaneously.
- **Reflux ratio** primarily affects specific energy consumption profiles rather than overhead composition lines.

---

## Engineering Significance

The engineering analysis demonstrates that no single operating variable independently determines process performance. Instead, efficient operation is achieved through a multi-objective balance of product purity, ethanol recovery, solvent recovery, and energy consumption. 

These precise relationships justify the use of a multi-objective **Process Performance Index (PPI)** as the single composite optimization metric during the machine learning phase.

---

## Repository Contents06_Engineering_Analysis
│
├── Engineering_Findings.pdf
│
├── Performance_Index
│    ├── PPI_Correlation.png
│    ├── PPI_Distribution.png
│    ├── PPI_vs_AverageRecovery.png
│    ├── PPI_vs_Energy.png
│    ├── PPI_vs_Purity.png
│    └── Top10_PPI.png
│
└── Sensitivity_Plots
├── 01_Boilup_vs_Purity.png
├── 02_Boilup_vs_Recovery.png
├── 03_Boilup_vs_TotalEnergy.png
├── 04_BottomFlow_vs_EGRecovery.png
├── 05_BottomFlow_vs_PPI.png
├── 06_RR_vs_TotalEnergy.png
├── 07_RR_vs_PPI.png
├── 08_Temperature_vs_Purity.png
├── 09_Temperature_vs_Recovery.png
├── 11_Scatter_Matrix.png
└── Correlation_Heatmap.png---

## Conclusion

The engineering analysis establishes the practical operating window of the extractive distillation process and maps out the major trade-offs. The generated operating boundaries form the firm physical foundation for the surrogate machine learning modeling and optimization stages that follow.
