"""
LC/NC Manuscript Round 1 — Supplementary SEM Validation
Journal: Humanities and Social Sciences Communications (Springer Nature)

Strategy per อาจารย์ (2026-07-24 10:50):
  - Keep MLR as primary analysis (as in Section 3.1 Para 45)
  - Add Section 4.10 "Supplementary SEM Validation" to satisfy reviewers
  - Show convergence between MLR (composite scores) and full latent SEM

This script:
  1. Loads Total_31052025.xlsx (Sheet: Full_Code) — N=411
  2. Fits full latent-variable SEM with semopy:
     - 9 predictors → BI (single-level structural model)
     - Mediation paths: FC → PT → BI, and PT mediating PE/HM/SI → BI
  3. Reports model fit + standardized paths + indirect effects
  4. Exports results as CSV + Markdown + PNG figure
"""
import os, json, sys
import numpy as np
import pandas as pd
from semopy import Model, calc_stats
from semopy.inspector import inspect

DATA = "/Volumes/Backup-1/Google Drive/iSchool2024/ประเมินภาระงาน-2567/NO-Code-Low-Code/Dataset/Total_31052025.xlsx"
OUT_DIR = "/Volumes/Backup-1/Google Drive/iSchool2024/ประเมินภาระงาน-2567/NO-Code-Low-Code/2026/Analysis_Output/Analysis_Output_update/Humanities and Social Sciences Communications/Revision/Round1/SEM_Supplementary"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------- Load data ----------
df = pd.read_excel(DATA, sheet_name="Full_Code")
print(f"Loaded: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Identify indicator items
indicator_prefixes = ["PE", "EE", "SI", "HM", "HB", "FC", "PT", "PC", "TA", "BI"]
items = {}
for prefix in indicator_prefixes:
    cols = [c for c in df.columns if c.startswith(prefix) and c[len(prefix):].isdigit()]
    items[prefix] = sorted(cols)
    print(f"  {prefix}: {cols}")

# Convert to numeric — coerce any strings
for prefix, cols in items.items():
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

# Drop any rows with NA on the indicator items
all_item_cols = [c for cols in items.values() for c in cols]
n_before = len(df)
df = df.dropna(subset=all_item_cols).reset_index(drop=True)
print(f"\nN after listwise: {len(df)} (was {n_before})")

# Verify all cols numeric
for c in all_item_cols:
    assert pd.api.types.is_numeric_dtype(df[c]), f"{c} is not numeric"

# ============================================================
# Model 1: MEASUREMENT MODEL (CFA) — 10 constructs
# ============================================================
cfa_desc = """
# Measurement model (CFA): 10 latent constructs, 3 items each
PE =~ PE1 + PE2 + PE3
EE =~ EE1 + EE2 + EE3
SI =~ SI1 + SI2 + SI3
HM =~ HM1 + HM2 + HM3
HB =~ HB1 + HB2 + HB3
FC =~ FC1 + FC2 + FC3
PT =~ PT1 + PT2 + PT3
PC =~ PC1 + PC2 + PC3
TA =~ TA1 + TA2 + TA3
BI =~ BI1 + BI2 + BI3
"""

cfa_model = Model(cfa_desc)
cfa_model.fit(df[all_item_cols])
cfa_stats = calc_stats(cfa_model)
print("\n=== CFA MODEL FIT ===")
print(cfa_stats.T)

cfa_stats.to_csv(os.path.join(OUT_DIR, "cfa_fit_stats.csv"))
cfa_est = cfa_model.inspect()
cfa_est.to_csv(os.path.join(OUT_DIR, "cfa_estimates.csv"), index=False)
print("\n=== CFA LOADINGS (measurement model) ===")
print(cfa_est[cfa_est['op'] == '~'][['lval','op','rval','Estimate','Std. Err','p-value']].head(30))

# ============================================================
# Model 2: FULL LATENT-VARIABLE STRUCTURAL MODEL
# ============================================================
# Structural specification:
#  - 9 exogenous UTAUT2 predictors (PE, EE, SI, HM, HB, FC, PC, TA) + PT (mediator) → BI
#  - Mediation: FC → PT, PE → PT, HM → PT, SI → PT (upstream drivers of trust)
# ============================================================
sem_desc = """
# Measurement (10 latent constructs)
PE =~ PE1 + PE2 + PE3
EE =~ EE1 + EE2 + EE3
SI =~ SI1 + SI2 + SI3
HM =~ HM1 + HM2 + HM3
HB =~ HB1 + HB2 + HB3
FC =~ FC1 + FC2 + FC3
PT =~ PT1 + PT2 + PT3
PC =~ PC1 + PC2 + PC3
TA =~ TA1 + TA2 + TA3
BI =~ BI1 + BI2 + BI3

# Structural: BI regressed on 9 predictors (matches manuscript MLR)
BI ~ PE + EE + SI + HM + HB + FC + PT + PC + TA

# Mediation: PT regressed on upstream drivers
PT ~ FC + PE + HM + SI
"""

sem_model = Model(sem_desc)
sem_model.fit(df[all_item_cols])
sem_stats = calc_stats(sem_model)
print("\n=== FULL SEM MODEL FIT ===")
print(sem_stats.T)

sem_stats.to_csv(os.path.join(OUT_DIR, "sem_fit_stats.csv"))
sem_est = sem_model.inspect(std_est=True)
sem_est.to_csv(os.path.join(OUT_DIR, "sem_estimates.csv"), index=False)

# Print structural paths only
print("\n=== SEM STRUCTURAL PATHS (BI ~ predictors) ===")
struct = sem_est[(sem_est['op'] == '~')].copy()
print(struct[['lval','op','rval','Estimate','Std. Err','p-value','Est. Std']].to_string())

# Save nicely formatted summary
struct_bi = struct[struct['lval'] == 'BI'].copy()
struct_pt = struct[struct['lval'] == 'PT'].copy()

# Compute indirect effects: e.g., FC → PT → BI
print("\n=== INDIRECT EFFECTS (via PT) ===")
# Get standardized coefficients
def get_est(df_, lval, rval):
    row = df_[(df_['lval'] == lval) & (df_['rval'] == rval) & (df_['op'] == '~')]
    if len(row) == 0: return None, None
    return float(row['Est. Std'].iloc[0]), float(row['p-value'].iloc[0])

# Path b: PT → BI
b, bp = get_est(struct, 'BI', 'PT')
print(f"PT → BI: β={b:.3f}, p={bp:.4f}")

# Path a: X → PT for each X
indirect_rows = []
for X in ['FC', 'PE', 'HM', 'SI']:
    a, ap = get_est(struct, 'PT', X)
    if a is None: continue
    ab = a * b
    # Direct effect of X on BI
    c_dir, c_dir_p = get_est(struct, 'BI', X)
    total = ab + c_dir if c_dir is not None else ab
    print(f"  {X} → PT: β={a:.3f}, p={ap:.4f}  |  Indirect (a×b) = {ab:.3f}  |  Direct = {c_dir:.3f} (p={c_dir_p:.4f})  |  Total = {total:.3f}")
    indirect_rows.append({
        'predictor': X, 'a_std': a, 'a_p': ap, 'b_std': b, 'b_p': bp,
        'indirect_ab': ab, 'direct_c': c_dir, 'direct_p': c_dir_p, 'total': total
    })

pd.DataFrame(indirect_rows).to_csv(os.path.join(OUT_DIR, "sem_indirect_effects.csv"), index=False)

# ============================================================
# Comparison: MLR (composite scores) vs SEM (latent)
# ============================================================
# Compute composite scores
comp_df = pd.DataFrame({p: df[items[p]].mean(axis=1) for p in indicator_prefixes})

# MLR: BI ~ 9 predictors
from statsmodels.api import OLS, add_constant
Xcols = [p for p in indicator_prefixes if p != 'BI']
X = add_constant(comp_df[Xcols])
y = comp_df['BI']
mlr = OLS(y, X).fit()
print("\n=== MLR (composite scores, reference) ===")
print(mlr.summary().tables[1])

# Standardize MLR coefficients: β_std = β_raw * (SD_x / SD_y)
mlr_std = {}
sd_y = y.std()
for c in Xcols:
    b_raw = mlr.params[c]
    p_val = mlr.pvalues[c]
    sd_x = comp_df[c].std()
    b_std = b_raw * sd_x / sd_y
    mlr_std[c] = {'b_std': b_std, 'p': p_val}
mlr_std_df = pd.DataFrame(mlr_std).T
mlr_std_df.to_csv(os.path.join(OUT_DIR, "mlr_standardized.csv"))
print("\nMLR standardized coefficients:")
print(mlr_std_df)

# Merge with SEM structural paths for comparison
compare = []
for pred in Xcols:
    sem_b, sem_p = get_est(struct, 'BI', pred)
    mlr_b = mlr_std[pred]['b_std']
    mlr_p = mlr_std[pred]['p']
    compare.append({
        'Predictor': pred,
        'MLR β (std)': round(mlr_b, 3),
        'MLR p': round(mlr_p, 4),
        'SEM β (std)': round(sem_b, 3) if sem_b is not None else None,
        'SEM p': round(sem_p, 4) if sem_p is not None else None,
        'Δβ': round(abs(mlr_b - sem_b), 3) if sem_b is not None else None,
    })
compare_df = pd.DataFrame(compare)
compare_df.to_csv(os.path.join(OUT_DIR, "mlr_vs_sem_comparison.csv"), index=False)
print("\n=== MLR vs SEM COMPARISON TABLE ===")
print(compare_df.to_string(index=False))

# Save a full JSON summary
summary = {
    'N': len(df),
    'cfa_fit': cfa_stats.to_dict(),
    'sem_fit': sem_stats.to_dict(),
    'mlr_r2': mlr.rsquared,
    'mlr_r2_adj': mlr.rsquared_adj,
    'mlr_f': mlr.fvalue,
    'mlr_f_pvalue': mlr.f_pvalue,
    'indirect_effects': indirect_rows,
    'mlr_vs_sem': compare,
    'notes': 'SEM = full latent-variable model with semopy 2.3.11; MLR reference matches manuscript §4.6.'
}
with open(os.path.join(OUT_DIR, "sem_supplementary_summary.json"), "w") as f:
    json.dump(summary, f, indent=2, default=str)

print(f"\n✅ All artifacts saved to: {OUT_DIR}")
print(f"   Files: {os.listdir(OUT_DIR)}")
