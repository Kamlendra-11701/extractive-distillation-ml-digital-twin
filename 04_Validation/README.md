# 04 – Validation of Extractive Distillation Simulation

## Overview

This section validates the developed extractive distillation model against published literature data before performing sensitivity analysis and optimization. Validation ensures that the simulation accurately represents the separation behaviour of the ethanol–water–ethylene glycol system and provides confidence in all subsequent engineering analyses.

---

## Objective

The objective of this validation study is to compare the simulation results with literature-reported values for:

- Ethanol product purity
- Ethylene glycol recovery
- Product flow rates
- Column temperature profiles
- Condenser and reboiler duties

Successful validation confirms that the developed digital process model can reliably predict the behaviour of the extractive distillation system.

---

## Validation Case

The simulation was performed using the following operating conditions:

| Parameter | Value |
|:---|---:|
| **Feed Flow Rate** | 5173 kg/h |
| **Solvent Flow Rate** | 20000 kg/h |
| **Column 1 Pressure** | 3.5 bar |
| **Column 1 Boilup Ratio** | 0.47 |
| **Column 1 Reflux Ratio** | 2.825 |
| **Column 2 Pressure** | 1.0 bar |
| **Column 2 Bottom Flow** | 0.09 kmol/s |
| **Column 2 Reflux Ratio** | 3.0 |
| **Solvent Temperature** | 256 °C |

This operating point was selected because it closely matches the reference operating conditions reported in the literature and provides stable convergence for both distillation columns.

---

## Validation Procedure

The validation was carried out using the following workflow:

1. Configure both ChemSep distillation columns using the selected operating conditions.
2. Run the simulation until both columns converge.
3. Record all major operating variables.
4. Compare the simulated results with literature values.
5. Calculate percentage deviations for key performance indicators.
6. Evaluate whether the deviations are within acceptable engineering limits.

---

## Validation Results

The simulation successfully converged for both distillation columns. Key performance indicators obtained from the simulation include:

### Column 1
- **Ethanol purity:** 96.15 wt%
- **Bottom EG purity:** 92.87 wt%
- **Top temperature:** 113.97 °C
- **Bottom temperature:** 208.90 °C

### Column 2
- **Bottom EG purity:** 99.51 wt%
- **Top temperature:** 96.64 °C
- **Bottom temperature:** 245.42 °C

These results closely match the trends reported in the reference study.

---

## Validation Figures

The following figures were generated during validation and are hosted inside the assets directory:

| Figure | Description |
|:---|:---|
| **01_Process_Summary.png** | Process flow diagram summary and stream metrics |
| **02_Column1_Validation.png** | Column 1 separation performance comparison curves |
| **03_Column2_Validation.png** | Column 2 separation performance comparison curves |
| **04_Column1_Composition.png** | Liquid phase composition profile across Column 1 stages |
| **05_Column2_Composition.png** | Liquid phase composition profile across Column 2 stages |
| **06_Energy_Distribution.png** | Utility duties comparison (reboilers vs condensers) |
| **07_Temperature_Profile.png** | Stage-by-stage thermal profiles for both columns |

---

## Files Included04_Validation
│
├── Validation_Cases.xlsx
├── Validation_Report.md
├── Validated_Base_Case.md
├── Reference_vs_Simulation.md
│
└── Validation_Figures
├── 01_Process_Summary.png
├── 02_Column1_Validation.png
├── 03_Column2_Validation.png
├── 04_Column1_Composition.png
├── 05_Column2_Composition.png
├── 06_Energy_Distribution.png
└── 07_Temperature_Profile.png


---

## Engineering Significance

Validation demonstrates that the developed process model accurately reproduces the behaviour of the ethanol–water extractive distillation process using ethylene glycol as the solvent.

A validated model provides confidence that subsequent sensitivity analysis, optimization studies, and machine learning predictions are based on a physically reliable process representation rather than numerical assumptions.

---

## Conclusion

The developed simulation successfully converged under the selected validation operating conditions and produced product compositions, temperature profiles, and energy requirements that agree well with published literature.

The validated model was therefore adopted as the baseline configuration for all subsequent sensitivity analysis and optimization studies included in this project.
