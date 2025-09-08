import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# amino acid folders
categories = ['m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']

# file patterns + regex to extract RMSD values
files = {
    "B97D_vs_xTB": ("RMSD_per_conf_B97D", r"conf\d+:\s*RMSD\s*=\s*([0-9.]+)"),
    "MP2_vs_xTB": ("RMSD_per_conf_MP2", r"conf\d+:\s*RMSD\s*=\s*([0-9.]+)"),
    "MP2_vs_B97D": ("MP2 vs B97D RMSD", r"conf\d+:\s*MP2 vs B97D RMSD\s*=\s*([0-9.]+)")
}

# containers for pooled data (for correlation plots)
all_data = {k: [] for k in files}

# summary rows for per-AA statistics
summary_rows = []

# loop over amino acids
for xaa in categories:
    aa_stats = {"amino_acid": xaa}
    print(f"\n📂 Processing {xaa}...")

    for label, (filename, pattern) in files.items():
        filepath = os.path.join(xaa, filename)
        values = []

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                text = f.read()

            values = [float(m.group(1)) for m in re.finditer(pattern, text)]
            all_data[label].extend(values)

            # stats per amino acid
            aa_stats[f"{label}_mean"] = np.mean(values)
            aa_stats[f"{label}_std"] = np.std(values)
        else:
            print(f"⚠️ Missing {filepath}")
            aa_stats[f"{label}_mean"] = np.nan
            aa_stats[f"{label}_std"] = np.nan

    summary_rows.append(aa_stats)

# make summary dataframe
summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv("summary_RMSD.csv", index=False)
print("\n✅ Saved summary_RMSD.csv")

# ---- Global Correlation Plots ---- #
pairs = [("B97D_vs_xTB", "MP2_vs_xTB"),
         ("B97D_vs_xTB", "MP2_vs_B97D"),
         ("MP2_vs_xTB", "MP2_vs_B97D")]

for m1, m2 in pairs:
    x = np.array(all_data[m1])
    y = np.array(all_data[m2])

    if len(x) < 2 or len(y) < 2:
        print(f"⚠️ Skipping {m1} vs {m2}: not enough data")
        continue

    r, pval = pearsonr(x, y)
    slope, intercept = np.polyfit(x, y, 1)
    fit_line = slope * x + intercept

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, alpha=0.7, label="Data")
    plt.plot(x, fit_line, color="red", lw=2,
             label=f"Fit: y={slope:.2f}x+{intercept:.2f}")
    plt.xlabel(m1)
    plt.ylabel(m2)
    plt.title(f"{m1} vs {m2}\nPearson r = {r:.3f}, p = {pval:.2e}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"Correlation_{m1}_vs_{m2}.png", dpi=300)
    plt.close()

    print(f"{m1} vs {m2}: r={r:.3f}, slope={slope:.3f}, intercept={intercept:.3f}, n={len(x)}")
