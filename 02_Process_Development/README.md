# 02 - Process Development

<img src="../.assets/process_flowsheet.png" alt="Process Flowsheet" width="100%%" />

Figure 1. Process flowsheet of the ethanol extractive distillation system developed in ChemSep. The validated process model consists of an extractive distillation column followed by a solvent recovery column with ethylene glycol recycle.

---

## Overview

This section documents the complete development of the extractive distillation process model implemented in ChemSep.

The objective of this stage was to reproduce the ethanol purification process presented in the reference literature and develop a reliable simulation model that could later be used for sensitivity analysis, dataset generation, machine learning, and AI-assisted process optimization.

During reproduction of the published work, several important operating conditions required to fully define the process were not reported. Therefore, the process model was systematically reconstructed using engineering assumptions, literature information, convergence studies, and process engineering judgement.

The final process model developed in this stage serves as the validated engineering foundation for the remainder of this project.

---

## Objectives

- Develop a complete ChemSep model for ethanol extractive distillation.
- Reconstruct the published process using available literature data.
- Identify missing operating parameters.
- Establish engineering assumptions for unavailable process information.
- Select appropriate thermodynamic models.
- Develop a stable base case capable of converging both distillation columns.
- Generate a validated process model suitable for further optimization studies.

---

## Development Workflow

Literature Review

[]

Identification of Missing Process Parameters

[]

Engineering Assumptions

[]

Thermodynamic Model Selection

[]

ChemSep Process Development

[]

Base Case Construction

[]

Stable Convergence of Both Columns

[]

Validated Process Model

[]

Sensitivity Analysis

---

## Process Description

The developed process consists of two coupled distillation columns.

### Column 1 - Extractive Distillation

The first column performs separation of ethanol and water using ethylene glycol as an entrainer.

Ethylene glycol selectively interacts with water, reducing its volatility and allowing high-purity ethanol to leave through the distillate stream.

### Column 2 - Solvent Recovery

The bottoms stream from Column 1 enters the solvent recovery column.

This column separates ethylene glycol from water so that the solvent can be recycled back to the extractive distillation column while water is removed from the process.

---

## Challenges Encountered

While reproducing the published research, several important simulation parameters were unavailable, including:

- Complete operating specifications
- Certain column operating conditions
- Missing convergence specifications
- Several process operating variables
- Exact simulation setup used by the authors

These missing details prevented direct reproduction of the published simulation.

Instead of making arbitrary assumptions, missing parameters were determined through systematic engineering studies and convergence analysis.

---

## Engineering Approach

1. Reproduce the published process flowsheet.
2. Identify missing simulation parameters.
3. Develop physically realistic engineering assumptions.
4. Construct a stable ChemSep model.
5. Perform convergence studies.
6. Select a stable operating point.
7. Use the validated base case for all subsequent analyses.

---

## Thermodynamic Model

The following thermodynamic models were selected based on the highly non-ideal ethanol-water system and recommendations available in literature.

| Property | Model |
|----------|-------|
| Property Method | Gamma-Phi |
| Activity Coefficient Model | NRTL |
| Equation of State | Peng-Robinson |
| Vapour Pressure Model | Extended Antoine |

---

## Base Case

A complete base case was developed after convergence studies.

The base case represents a physically realistic operating condition where both distillation columns converge successfully while maintaining stable temperatures and satisfactory product separation.

This operating condition served as the reference case for:

- Sensitivity analysis
- Dataset generation
- Machine learning model development
- AI optimization

The detailed operating parameters are available in:

**Base_Case_Parameters.xlsx**

---

## Files Included

| File | Description |
|------|-------------|
| Assumptions.pdf | Authoritative engineering assumptions used during model development |
| Thermodynamic_Model.md | Selection and justification of thermodynamic models |
| Base_Case_Parameters.xlsx | Complete operating specifications of the validated base case |
| Process_Flowsheet.md | Markdown viewer showing Figure 2 Process Flowsheet |
| ChemSep_Configuration.md | Complete ChemSep configuration files including Figure 3, Column layouts, and Stream inputs |

---

## Output of This Stage

The major outcome of this stage is a fully functional and validated ChemSep process model that serves as the engineering foundation for the remainder of the project.

This validated model is subsequently used for:

- Process sensitivity analysis
- Generation of engineering datasets
- Machine learning model development
- AI-assisted operating condition optimization

---

## Next Stage

The validated base case developed in this section is used in **03 - Sensitivity Analysis**, where key operating variables are systematically varied to determine their influence on process performance and identify feasible operating ranges for optimization.
