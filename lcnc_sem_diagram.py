"""
Draw SEM path diagram for Section 4.10 (Figure 5).
- Only structural paths (latent-level), suppress measurement (indicator) side.
- Standardized coefficients + significance markers.
- Solid = significant, dashed = ns; green = positive, red = negative.
- FC → PT → BI mediation highlighted.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

OUT_DIR = "/Volumes/Backup-1/Google Drive/iSchool2024/ประเมินภาระงาน-2567/NO-Code-Low-Code/2026/Analysis_Output/Analysis_Output_update/Humanities and Social Sciences Communications/Revision/Round1/SEM_Supplementary"

# Structural paths from SEM results
# Format: (source, target, beta, p_value)
paths_to_BI = [
    ("PE", "BI", 0.064, 0.279),
    ("EE", "BI", -0.024, 0.641),
    ("SI", "BI", 0.151, 0.021),
    ("HM", "BI", 0.338, 0.000),
    ("HB", "BI", 0.308, 0.000),
    ("FC", "BI", -0.276, 0.001),
    ("PC", "BI", 0.161, 0.063),
    ("TA", "BI", 0.002, 0.953),
    ("PT", "BI", 0.291, 0.000),
]

paths_to_PT = [
    ("FC", "PT", 0.468, 0.000),
    ("PE", "PT", 0.061, 0.403),
    ("HM", "PT", 0.261, 0.001),
    ("SI", "PT", -0.055, 0.455),
]

# Node positions (x, y)
positions = {
    # Left column: exogenous predictors
    "PE": (0.10, 0.90),
    "EE": (0.10, 0.78),
    "SI": (0.10, 0.66),
    "HM": (0.10, 0.54),
    "HB": (0.10, 0.42),
    "FC": (0.10, 0.30),
    "PC": (0.10, 0.18),
    "TA": (0.10, 0.06),
    # Center: mediator
    "PT": (0.50, 0.50),
    # Right: outcome
    "BI": (0.90, 0.50),
}

# Full names
labels = {
    "PE": "PE\n(Perf.\nExpect.)",
    "EE": "EE\n(Effort\nExpect.)",
    "SI": "SI\n(Social\nInfluence)",
    "HM": "HM\n(Hedonic\nMotiv.)",
    "HB": "HB\n(Habit)",
    "FC": "FC\n(Facilit.\nCond.)",
    "PC": "PC\n(Price\nConsc.)",
    "TA": "TA\n(Techno-\nAnxiety)",
    "PT": "PT\n(Privacy /\nTrust)",
    "BI": "BI\n(Behavioral\nIntention)",
}

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Draw arrows first (paths)
def draw_path(source, target, beta, p, offset=0.0, curved=False):
    x1, y1 = positions[source]
    x2, y2 = positions[target]
    # Node radius offset (approx)
    dx = x2 - x1
    dy = y2 - y1
    dist = np.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    # shrink
    r_src, r_tgt = 0.055, 0.055
    x1p, y1p = x1 + ux * r_src, y1 + uy * r_src
    x2p, y2p = x2 - ux * r_tgt, y2 - uy * r_tgt

    sig = p < 0.05
    color = "#2ca02c" if beta > 0 else "#d62728"  # green + red
    ls = "-" if sig else "--"
    alpha = 1.0 if sig else 0.4
    lw = 2.4 if abs(beta) >= 0.25 else 1.8 if abs(beta) >= 0.15 else 1.2

    arrow_style = "->,head_length=8,head_width=5"
    connectionstyle = f"arc3,rad={0.18 if curved else 0}"

    arrow = FancyArrowPatch(
        (x1p, y1p), (x2p, y2p),
        arrowstyle=arrow_style,
        connectionstyle=connectionstyle,
        color=color, linestyle=ls, linewidth=lw, alpha=alpha,
        mutation_scale=15,
    )
    ax.add_patch(arrow)

    # Label position (midpoint + perpendicular offset)
    mx, my = (x1p + x2p) / 2, (y1p + y2p) / 2
    px, py = -uy, ux
    if curved:
        mx += px * 0.05
        my += py * 0.05
    mx += px * offset
    my += py * offset

    sig_marker = ""
    if p < 0.001:
        sig_marker = "***"
    elif p < 0.01:
        sig_marker = "**"
    elif p < 0.05:
        sig_marker = "*"
    lbl = f"{beta:+.2f}{sig_marker}"
    ax.text(mx, my, lbl, fontsize=8.5,
            fontweight="bold" if sig else "normal",
            color=color if sig else "#888",
            ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))

# Draw paths X → BI (direct)
for src, tgt, beta, p in paths_to_BI:
    if src == "PT":  # will draw separately with emphasis
        continue
    draw_path(src, tgt, beta, p, offset=0.005, curved=True)

# Draw paths X → PT (mediation a-paths)
for src, tgt, beta, p in paths_to_PT:
    draw_path(src, tgt, beta, p, offset=0.02, curved=False)

# Draw PT → BI (path b) with extra emphasis
for src, tgt, beta, p in paths_to_BI:
    if src == "PT":
        x1, y1 = positions[src]
        x2, y2 = positions[tgt]
        color = "#1f77b4"  # blue for mediator path
        arrow = FancyArrowPatch(
            (x1 + 0.055, y1), (x2 - 0.055, y2),
            arrowstyle="->,head_length=10,head_width=6",
            color=color, linewidth=3.0,
            mutation_scale=18,
        )
        ax.add_patch(arrow)
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2 + 0.015
        ax.text(mx, my, f"{beta:+.3f}***", fontsize=11, fontweight="bold",
                color=color, ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color, lw=1.2))

# Draw nodes on top
def draw_node(name, pos, style="predictor"):
    x, y = pos
    if style == "outcome":
        fc = "#fff4d6"; ec = "#e69138"
    elif style == "mediator":
        fc = "#d9e6f7"; ec = "#3d85c6"
    else:
        fc = "#f2f2f2"; ec = "#666"
    box = FancyBboxPatch(
        (x - 0.055, y - 0.045), 0.11, 0.09,
        boxstyle="round,pad=0.005",
        fc=fc, ec=ec, lw=1.8
    )
    ax.add_patch(box)
    ax.text(x, y, labels[name], fontsize=9, ha="center", va="center",
            fontweight="bold")

for name in ["PE","EE","SI","HM","HB","FC","PC","TA"]:
    draw_node(name, positions[name], style="predictor")
draw_node("PT", positions["PT"], style="mediator")
draw_node("BI", positions["BI"], style="outcome")

# Title
ax.text(0.5, 0.985, "Figure 5. Supplementary Latent-Variable SEM — Standardized Path Coefficients (N = 411)",
        fontsize=13, fontweight="bold", ha="center")
ax.text(0.5, 0.955,
        "Model fit: χ²(364) = 841.12, χ²/df = 2.31 · CFI = 0.941 · TLI = 0.929 · RMSEA = 0.058 · GFI = 0.901",
        fontsize=10, ha="center", color="#333")

# Legend
green_solid = plt.Line2D([0],[0], color="#2ca02c", lw=2, label="Positive, p < .05")
red_solid = plt.Line2D([0],[0], color="#d62728", lw=2, label="Negative, p < .05")
gray_dashed = plt.Line2D([0],[0], color="#888", lw=1.2, linestyle="--", label="Non-significant")
blue_thick = plt.Line2D([0],[0], color="#1f77b4", lw=3, label="Mediator path (PT → BI)")
ax.legend(handles=[green_solid, red_solid, gray_dashed, blue_thick],
          loc="lower right", fontsize=8, frameon=True, ncol=1)

# Footnote
ax.text(0.5, 0.005,
        "Standardized β · Significance: *p<.05, **p<.01, ***p<.001 · Values on curved arrows = X → BI direct; on straight arrows = X → PT (path a); on center arrow = PT → BI (path b).",
        fontsize=7.5, ha="center", style="italic", color="#444")

out_path = f"{OUT_DIR}/Figure5_SEM_Path_Diagram.png"
plt.savefig(out_path, dpi=400, bbox_inches="tight", facecolor="white")
print(f"✅ Saved: {out_path}")
plt.close()
