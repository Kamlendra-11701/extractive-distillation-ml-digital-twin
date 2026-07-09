# Reference vs Simulation Comparison

## Objective

The objective of this comparison is to evaluate how closely the developed ChemSep simulation reproduces the process behaviour reported in the reference literature.

The published paper primarily reports separation performance and sensitivity trends rather than complete simulation specifications. Consequently, only the variables explicitly available in the literature are compared directly. Parameters not reported by the authors are indicated as **NR (Not Reported)**.

---

## Process Comparison

| Parameter | Literature | Present Work | Agreement |
|------------|-----------:|-------------:|-----------|
| **Feed Flowrate** | 5173 kg/h | 5173 kg/h | ✓ Exact |
| **Feed Composition** | 73 wt% EtOH / 27 wt% Water | 73 wt% EtOH / 27 wt% Water | ✓ Exact |
| **Solvent** | Ethylene Glycol | Ethylene Glycol | ✓ Exact |
| **Solvent Flowrate** | 20000 kg/h | 20000 kg/h | ✓ Exact |
| **Column 1 Pressure** | 3.5 bar | 3.5 bar | ✓ Exact |
| **Column 2 Pressure** | 1 bar | 1 bar | ✓ Exact |
| **Number of Stages (C1)** | 15 | 15 | ✓ Exact |
| **Number of Stages (C2)** | 10 | 10 | ✓ Exact |

---

## Separation Performance

| Variable | Literature | Present Work | Difference |
|-----------|-----------:|-------------:|-----------:|
| **Ethanol Purity** *(Column 1 Top)* | ~96 wt% | 96.15 wt% | +0.15 wt% |
| **EG Purity** *(Column 2 Bottom)* | ~99 wt% | 99.51 wt% | +0.51 wt% |
| **Stable Convergence** | Reported | Achieved | ✓ |

---

## Temperature Comparison

| Variable | Literature | Present Work |
|-----------|-----------:|-------------:|
| **Column 1 Top Temperature** | NR | 113.97 °C |
| **Column 1 Bottom Temperature** | NR | 208.90 °C |
| **Column 2 Top Temperature** | NR | 96.64 °C |
| **Column 2 Bottom Temperature** | NR | 245.42 °C |

---

## Energy Comparison

| Variable | Literature | Present Work |
|-----------|-----------:|-------------:|
| **Column 1 Condenser Duty** | NR | 3617 kW |
| **Column 1 Reboiler Duty** | NR | 2858 kW |
| **Column 2 Condenser Duty** | NR | 3502 kW |
| **Column 2 Reboiler Duty** | NR | 2137 kW |

---

## Discussion

The published research paper provides the overall process configuration and reports the expected separation behaviour but does not disclose every operating parameter or energy requirement necessary for exact numerical reproduction.

To address these missing specifications, engineering assumptions were developed and validated through systematic sensitivity analysis.

The resulting ChemSep model successfully reproduces the key separation characteristics reported in the literature:

- Ethanol purity at the top of the extractive distillation column is approximately **96 wt%**, consistent with the published work.
- Ethylene glycol purity at the bottom of the solvent recovery column exceeds **99 wt%**, demonstrating efficient solvent recovery.
- Both columns converge successfully under realistic operating conditions.
- Temperature profiles remain physically reasonable throughout the process.

Although some numerical variables cannot be compared directly because they are not reported in the paper, the developed simulation reproduces the intended process behaviour and therefore serves as a validated baseline for subsequent optimization and machine learning.

---

## Reference

> Malucelli, B. M., Bach, L. H., Mafra, A. C. O., & Silva, W. C. (2024). *Study of the Hydrous Ethanol Purification Stage: Simulation and Sensitivity Analysis of Extractive Distillation Using the DWSIM Simulator*. Journal of Engineering Research. https://doi.org/10.22533/at.ed.3174232418095
