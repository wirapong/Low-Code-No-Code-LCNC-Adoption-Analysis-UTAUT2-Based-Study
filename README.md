# 📘 README.txt

## Low-Code/No-Code (LCNC) Adoption Analysis – UTAUT2-Based Study

---

## 📌 Project Overview

This repository contains the **data analysis pipeline and research manuscript** for the study:

> **“Factors Affecting Behavioral Intention to Use Low-Code/No-Code Platforms: An Empirical Investigation Based on the UTAUT2 Framework”** 

The project investigates **individual-level determinants of LCNC platform adoption** using an extended **UTAUT2 model**, incorporating:

* Hedonic Motivation
* Habit
* Social Influence
* Performance Expectancy
* Facilitating Conditions
* Price Consciousness
* Privacy/Trust
* Techno-Anxiety

The study uses **quantitative survey data (N = 411)** and applies **multiple linear regression analysis** to explain behavioral intention.

---

## 📂 Repository Structure

```
├── lcnc_analysis.ipynb        # Main Python analysis pipeline (Colab-ready)
├── research_article.md        # Full research manuscript (journal-ready)
├── README.txt                 # Project documentation (this file)
```

---

## ⚙️ Methodology Summary

### Research Design

* Quantitative, cross-sectional survey
* 5-point Likert scale instrument
* 9 independent variables → Behavioral Intention (DV)

### Analytical Workflow

1. Data preprocessing
2. Descriptive statistics
3. Reliability analysis (Cronbach’s alpha)
4. Correlation analysis (Pearson)
5. Multiple linear regression
6. Multicollinearity diagnostics (VIF)
7. Regression diagnostics

---

## 🧪 Key Results

* Model explanatory power:
  **R² = 0.621 (62.1% variance explained)**

* Significant predictors:

  * Hedonic Motivation (strongest)
  * Privacy/Trust
  * Habit
  * Social Influence
  * Performance Expectancy
  * Price Consciousness
  * Facilitating Conditions (negative effect)

* Non-significant:

  * Effort Expectancy
  * Techno-Anxiety

---

## 💻 Requirements

### Python Environment

* Python 3.10+
* Recommended: Google Colab / Jupyter Notebook

### Required Libraries

```bash
pandas
numpy
scipy
statsmodels
pingouin
matplotlib
seaborn
```

Install via:

```bash
pip install pandas numpy scipy statsmodels pingouin matplotlib seaborn
```

---

## ▶️ How to Run

1. Open the notebook:

   ```
   lcnc_analysis.ipynb
   ```

2. Run all cells sequentially:

   * Data loading
   * Statistical analysis
   * Model estimation
   * Visualization

3. Outputs include:

   * Tables (Descriptive, Reliability, Regression)
   * Correlation matrix
   * Diagnostic plots

---

## 📊 Outputs

The notebook generates:

* Descriptive statistics tables
* Cronbach’s alpha reliability results
* Pearson correlation matrix
* Regression coefficients (β, p-values, VIF)
* Diagnostic plots:

  * Residual plots
  * Q-Q plots
  * Homoscedasticity checks

---

## 🔍 Reproducibility Notes

* Dataset is assumed to be **survey-based (N = 411)**
* No missing data (complete-case analysis)
* All variables are **composite means of 3-item constructs**
* VIF < 3 confirms no multicollinearity issues

---

## 📚 Theoretical Framework

This study is grounded in:

* **Unified Theory of Acceptance and Use of Technology**
* **UTAUT2**

Extended with:

* Price Consciousness
* Techno-Anxiety
* Privacy/Trust

---

## 🚀 Contributions

* Extends UTAUT2 to **LCNC platforms (citizen development context)**
* Identifies **hedonic and trust factors as dominant drivers**
* Reveals **unexpected negative effect of facilitating conditions**
* Provides **practical insights for digital transformation strategies**

---

## ⚠️ Limitations

* Cross-sectional design (no causal inference)
* Self-reported data
* Sample may not fully represent all industries
* No longitudinal behavioral validation

---

## 🔮 Future Work

* Structural Equation Modeling (SEM)
* Longitudinal adoption studies
* Cross-country comparison
* Actual usage behavior analysis

---

## 📖 Citation

If you use this repository, please cite:

```
Chansanam, W. (2026).
Factors Affecting Behavioral Intention to Use Low-Code/No-Code Platforms:
An Empirical Investigation Based on the UTAUT2 Framework.
```

---

## 👤 Author

**Assoc. Prof. Dr. Wirapong Chansanam**
Khon Kaen University, Thailand
Email: [wirapongc@kku.ac.th](mailto:wirapongc@kku.ac.th)

---

## 📌 License

This project is for **academic and research purposes**.
Please contact the author for reuse or redistribution permissions.

---

If you want, I can also:

* Convert this into a **GitHub Markdown README.md (with badges & visuals)**
* Add **workflow diagrams (publication-ready)**
* Or align it with **Elsevier / Springer reproducibility standards**
