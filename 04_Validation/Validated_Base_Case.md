# Validated Base Case

## Purpose

Following the sensitivity analysis of both distillation columns, multiple operating conditions were evaluated to identify a simulation that could reliably reproduce the separation behaviour reported in the reference literature.

The selected validation case represents the operating condition that produced stable convergence in both columns while providing the closest agreement with the published process performance.

---

## Selected Operating Conditions

### Feed Stream

| Parameter | Value |
|------------|------:|
| Feed Flowrate | 5173 kg/h |
| Feed Composition | 73 wt% Ethanol / 27 wt% Water |
| Feed Temperature | 111.2 °C |
| Feed Pressure | 3.5 bar |

---

### Solvent Stream

| Parameter | Value |
|------------|------:|
| Solvent | Ethylene Glycol |
| Flowrate | 20000 kg/h |
| Temperature | 256 °C |

---

### Column 1

| Parameter | Value |
|------------|------:|
| Number of Stages | 15 |
| Feed Stage | 8 |
| Solvent Stage | 8 |
| Operating Pressure | 3.5 bar |
| Reflux Ratio | 2.825 |
| Boilup Ratio | 0.47 |

---

### Column 2

| Parameter | Value |
|------------|------:|
| Number of Stages | 10 |
| Feed Stage | 5 |
| Operating Pressure | 1.0 bar |
| Bottom Product Flow | 0.09 kmol/s |
| Reflux Ratio | 3.0 |

---

## Validation Results

### Column 1

| Output | Value |
|---------|------:|
| Top Temperature | 113.97 °C |
| Bottom Temperature | 208.90 °C |
| Ethanol Purity | 96.15 wt% |
| Water Purity | 3.27 wt% |
| EG Purity | 0.58 wt% |
| Top Flow | 3876.05 kg/h |
| Bottom Flow | 21296.90 kg/h |
| Condenser Duty | 3617 kW |
| Reboiler Duty | 2858 kW |
| Converged | Yes |

---

### Column 2

| Output | Value |
|---------|------:|
| Top Temperature | 96.64 °C |
| Bottom Temperature | 245.42 °C |
| Ethanol Top | 96.64 wt% |
| Water Top | 3.46 wt% |
| EG Top | 0.01 wt% |
| Ethanol Bottom | 0.01 wt% |
| Water Bottom | 0.48 wt% |
| EG Bottom | 99.51 wt% |
| Top Flow | 1422.56 kg/h |
| Bottom Flow | 19874.00 kg/h |
| Condenser Duty | 3502 kW |
| Reboiler Duty | 2137 kW |
| Converged | Yes |

---

## Selection Rationale

This operating condition was selected as the validation case because it satisfied all engineering validation requirements.

- Successful convergence of both distillation columns.
- Ethanol product purity closely matched the published literature.
- Ethylene glycol recovery column produced greater than 99 wt% EG purity.
- Temperature profiles were physically realistic.
- Stable condenser and reboiler duties were obtained.
- No abnormal phase behaviour or convergence instability was observed.

Among all investigated validation runs, this operating condition demonstrated the best overall agreement with the reference study while maintaining physically meaningful operating conditions.

---

## Role in This Project

The selected validation case served as the baseline operating condition for all subsequent work in this project.

It was used for:

- Dataset generation.
- Machine learning model development.
- AI-based operating condition optimization.
- Final performance comparison.
