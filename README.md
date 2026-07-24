# 📘 Low-Code/No-Code (LC/NC) Adoption Analysis — UTAUT2-Based Study

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![semopy 2.3.11](https://img.shields.io/badge/semopy-2.3.11-green.svg)](https://semopy.com/)
[![License: Academic](https://img.shields.io/badge/license-Academic-orange.svg)](#license)

---

## 📌 Project Overview

Data-analysis pipeline and research materials for:

> **"From Behavioral Intention to Adoption Readiness: A UTAUT2-Based Analysis of Low-Code/No-Code Platforms with Privacy/Trust as a Mediating Mechanism"**

**Journal:** *Humanities and Social Sciences Communications* (Springer Nature) — under Round 1 revision (resubmitted 2026-07-24)

The study investigates individual-level determinants of LC/NC platform adoption readiness using an **extended UTAUT2** framework with three context-sensitive additions:

| Original UTAUT2 | Extensions |
|---|---|
| Performance Expectancy (PE) | Privacy/Trust (PT) — *mediator* |
| Effort Expectancy (EE) | Price Consciousness (PC) |
| Social Influence (SI) | Techno-Anxiety (TA) |
| Facilitating Conditions (FC) | |
| Hedonic Motivation (HM) | |
| Habit (HB) | |

**Terminal DV:** Behavioral Intention (BI) — as proxy for **adoption readiness** in the early diffusion stage. Actual usage behavior is identified as future longitudinal work.

**Sample:** N = 411 Thai professional and academic users (purposive sampling, 2024–2025)

---

## 📂 Repository Structure

```
├── lcnc_sem_analysis.py       # 🆕 CFA + Full latent SEM (semopy 2.3.11)
├── lcnc_preview_tables.py     # 🆕 Tables 10/11/12 Markdown preview
├── lcnc_sem_diagram.py        # 🆕 Figure 5 path diagram (matplotlib)
├── lcnc_analysis.ipynb        # Original MLR pipeline (Jupyter notebook)
├── LowCode_NoCode.sav         # Full dataset (SPSS format)
├── GoogleForm.pdf             # Survey instrument
├── IRB_HE683119.pdf           # KKUEC Exemption Determination
└── README.md                  # This file
```

---

## ⚙️ Analytical Approach — Hybrid MLR + SEM

This study uses a **hybrid analytical strategy**, motivated by two-reviewer feedback during Round 1 revision:

### Primary: Multiple Linear Regression (MLR)
- CFA-then-MLR on composite scores (following Anderson & Gerbing, 1988)
- Bootstrapped 95% CIs (n = 5,000 iterations)
- Rationale: single-DV model with confirmed latent-variable validity

### Supplementary: Full Latent-Variable SEM (semopy 2.3.11)
- All 10 constructs modeled with three indicator items each
- Structural equations: `BI ~ 9 predictors` and `PT ~ FC + PE + HM + SI`
- Maximum likelihood estimation
- Purpose: cross-validate mediation claims within a coherent structural framework

**Both frameworks converge on the substantively strongest paths** (HM, HB, PT, FC).

---

## 🎯 Key Results

### CFA Measurement Model
- All standardized loadings ≥ 0.65
- AVE ≥ 0.73 for all 10 constructs
- HTMT < 0.77 (discriminant validity confirmed)

### MLR (Primary Analysis)
- **R² = 0.621** (Adjusted R² = 0.612)
- F(9, 401) = 72.84, p < .001
- Bootstrap CIs (n = 5,000) confirm all significant effects

### Supplementary SEM Model Fit
| Fit Index | Value | Threshold |
|---|---:|---:|
| χ²(364) | 841.12 | — |
| χ²/df | 2.31 | < 3.0 ✅ |
| CFI | 0.941 | ≥ 0.90 ✅ |
| TLI | 0.929 | ≥ 0.90 ✅ |
| GFI | 0.901 | ≥ 0.90 ✅ |
| AGFI | 0.881 | ≥ 0.85 ✅ |
| RMSEA | 0.058 | ≤ 0.08 ✅ |

### MLR vs SEM Convergence (7/9 predictors)

| Predictor → BI | MLR β | SEM β | Convergence |
|---|---:|---:|:---:|
| Performance Expectancy (PE) | +0.109* | +0.064 ns | ⚠️ MLR sig, SEM ns |
| Effort Expectancy (EE) | −0.034 ns | −0.024 ns | ✅ |
| Social Influence (SI) | **+0.145\*\*** | **+0.151\*** | ✅ |
| Hedonic Motivation (HM) | **+0.302\*\*\*** | **+0.338\*\*\*** | ✅ |
| Habit (HB) | **+0.232\*\*\*** | **+0.308\*\*\*** | ✅ |
| Facilitating Conditions (FC) | **−0.113\*** | **−0.276\*\*** | ✅ (negative) |
| Privacy/Trust (PT) | **+0.249\*\*\*** | **+0.291\*\*\*** | ✅ |
| Price Consciousness (PC) | +0.116* | +0.161 ns | ⚠️ |
| Techno-Anxiety (TA) | −0.013 ns | +0.002 ns | ✅ |

### Mediation via Privacy/Trust (SEM)

| Path | a | b | Indirect (a×b) | Direct | Total | Type |
|---|---:|---:|---:|---:|---:|:---:|
| FC → PT → BI | +0.468*** | +0.291*** | +0.136 | −0.276** | −0.140 | **Partial** |
| HM → PT → BI | +0.261** | +0.291*** | +0.076 | +0.338*** | +0.414 | **Partial** |

**Key finding:** Privacy/Trust is a significant explanatory mediator of Facilitating Conditions → Behavioral Intention, with a negative net total effect explained by suppression + inconsistent mediation.

---

## 💻 Requirements

### Python Environment

- Python **3.11+** (tested on `/opt/homebrew/bin/python3.11`)
- macOS / Linux (tested on macOS 26.5 arm64)

### Install Dependencies

```bash
pip install semopy factor_analyzer pandas numpy scipy statsmodels pingouin \
             matplotlib seaborn openpyxl python-docx
```

Or minimally for the three SEM scripts:

```bash
pip install semopy pandas numpy statsmodels matplotlib openpyxl
```

---

## ▶️ How to Reproduce

### Prerequisites

Place the raw data file (`Total_31052025.xlsx` sheet `Full_Code`, N = 411 × 35 cols) at the path referenced inside `lcnc_sem_analysis.py`, or edit the `DATA` constant near the top of the script.

Column schema:
- Demographics: `Gender`, `Age`, `Experience`, `Affiliation`
- Constructs (3 items each): `PE1-3`, `EE1-3`, `SI1-3`, `HM1-3`, `HB1-3`, `FC1-3`, `PT1-3`, `PC1-3`, `TA1-3`, `BI1-3`

### Execution Order

```bash
# 1. Main analysis — CFA + SEM + MLR comparison
python3.11 lcnc_sem_analysis.py
# ↳ Outputs: SEM_Supplementary/*.csv and .json (fit indices, estimates, mediation)

# 2. Generate preview tables (Table 10/11/12)
python3.11 lcnc_preview_tables.py
# ↳ Outputs: SEM_Supplementary/PREVIEW_Section_4.10_Tables.md

# 3. Draw SEM path diagram (Figure 5 draft)
python3.11 lcnc_sem_diagram.py
# ↳ Outputs: SEM_Supplementary/Figure5_SEM_Path_Diagram.png (400 dpi)
```

### Runtime

- `lcnc_sem_analysis.py`: ~30–60 s
- `lcnc_preview_tables.py`: < 5 s
- `lcnc_sem_diagram.py`: ~5 s

---

## 📊 Outputs

### CSV Tables (from `lcnc_sem_analysis.py`)

| File | Description |
|---|---|
| `cfa_fit_stats.csv` | Measurement model fit indices |
| `cfa_estimates.csv` | Standardized loadings + p-values |
| `sem_fit_stats.csv` | Structural model fit indices |
| `sem_estimates.csv` | All SEM path estimates (unstandardized + standardized) |
| `sem_indirect_effects.csv` | Mediation decomposition via PT |
| `mlr_standardized.csv` | MLR standardized coefficients |
| `mlr_vs_sem_comparison.csv` | Side-by-side path comparison |
| `sem_supplementary_summary.json` | Full analytical summary (all above combined) |

### Markdown Preview (from `lcnc_preview_tables.py`)

- `PREVIEW_Section_4.10_Tables.md` — Tables 10 (fit indices), 11 (MLR vs SEM comparison), 12 (mediation effects)

### Figure (from `lcnc_sem_diagram.py`)

- `Figure5_SEM_Path_Diagram.png` — Path diagram with standardized β + significance markers (400 dpi)

---

## 🔬 Reproducibility Notes

- **Random seed:** semopy is deterministic under ML estimation; no explicit seed needed.
- **Missing data:** After listwise deletion on the indicator items, N = 411 (no missing values).
- **Composite scores:** Mean of three items per construct (used only in MLR reference; SEM uses raw items).
- **Standardization for MLR β:** `β_std = β_raw × SD_x / SD_y` (matches CFA-then-regression convention).
- **Bootstrap:** MLR uses `statsmodels` with 5,000 non-parametric bootstrap samples for CIs.

---

## 📚 Theoretical Framework

- **UTAUT2** (Venkatesh et al., 2012) — core 7 constructs
- **Trust in technology** (Gefen et al., 2003; McKnight et al., 2002) — Privacy/Trust operationalization
- **Protection Motivation Theory** (Rogers, 1975) — Techno-Anxiety
- **Two-step approach** (Anderson & Gerbing, 1988) — CFA-then-structural analysis
- **Preacher-Hayes bootstrapping** (Preacher & Hayes, 2008) — mediation testing

---

## 🚀 Contributions

- **Empirical:** First large-sample (N = 411) UTAUT2 study of LC/NC platform adoption readiness in a Southeast Asian emerging-economy context.
- **Methodological:** Hybrid MLR + SEM design that satisfies both parsimony/interpretability and structural rigor.
- **Substantive:** Identifies **Hedonic Motivation, Habit, and Privacy/Trust** as leading positive antecedents; **Facilitating Conditions negative direct effect** reframed as suppression + inconsistent mediation via PT.
- **Practical:** Design and policy implications for LC/NC vendors, organizations, and Thai digital-transformation initiatives.

---

## ⚠️ Limitations

- **Cross-sectional design** — no causal inference
- **Purposive (non-probability) sampling** — generalizability caveats
- **Behavioral Intention as terminal DV** — actual adoption behavior not measured
- **Privacy/Trust as combined construct** — separate measurement (privacy concern, institutional assurance, vendor trust) is future work
- **Common method bias** — mitigated but not eliminated; Harman's test + procedural controls

---

## 🔮 Future Work

- Longitudinal panel study with **platform login frequency** and **completed project counts** as external UB indicators (3–6 month follow-up)
- **Second-order factor** measurement of Privacy/Trust (privacy concerns + trust feelings as sub-constructs)
- **Stratified probability sampling** by industry, organization size, and region
- **Cross-country comparison** across ASEAN economies
- **AI-embedded LC/NC platforms** — extended Techno-Anxiety with situational stimuli

---

## 📖 Citation

If you use this repository, please cite:

```bibtex
@article{Chansanam2026LCNC,
  author  = {Chansanam, Wirapong},
  title   = {From Behavioral Intention to Adoption Readiness: A UTAUT2-Based Analysis of
             Low-Code/No-Code Platforms with Privacy/Trust as a Mediating Mechanism},
  journal = {Humanities and Social Sciences Communications},
  year    = {2026},
  note    = {Under revision}
}
```

---

## 👤 Author

**Assoc. Prof. Dr. Wirapong Chansanam**
Khon Kaen University, Thailand
Email: [wirapongc@kku.ac.th](mailto:wirapongc@kku.ac.th)
ORCID: [0000-0001-5546-8485](https://orcid.org/0000-0001-5546-8485)

---

## 📌 License

This project is provided for **academic and research purposes**.
Please contact the author for reuse or redistribution.

---

## 📝 Changelog

- **2026-07-24** — Added SEM analysis pipeline (`lcnc_sem_analysis.py`, `lcnc_preview_tables.py`, `lcnc_sem_diagram.py`) following Round 1 revision. Title updated to reflect Behavioral Intention framing. README expanded with hybrid MLR+SEM methodology and full results.
- **Earlier** — Original MLR-only notebook (`lcnc_analysis.ipynb`), dataset, IRB, and survey instruments.
