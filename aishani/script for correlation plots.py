import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.stats import pearsonr

categories = ['m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']
methods = {
    "Relative-ENERGIES": "XTB",
    "Relative_B97D": "B97D",
    "Relative_MP2": "MP2"
}

# Collect aligned conformers across amino acids
data = {m: [] for m in methods.values()}

for xaa in categories:
    # Load per-amino-acid data
    aa_data = {}
    for method_file, method_name in methods.items():
        filepath = f"{xaa}/{xaa.upper()}.{method_file}"
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                vals = [float(line.strip()) for line in file if line.strip()]
            aa_data[method_name] = vals
        else:
            aa_data[method_name] = []

    # Align conformers within this amino acid
    min_len = min(len(aa_data["XTB"]), len(aa_data["B97D"]), len(aa_data["MP2"]))
    if min_len > 0:
        for method in methods.values():
            data[method].extend(aa_data[method][:min_len])

# Now do pairwise correlations on pooled aligned data
pairs = [("XTB", "B97D"), ("B97D", "MP2"), ("XTB", "MP2")]

for m1, m2 in pairs:
    x = np.array(data[m1])
    y = np.array(data[m2])

    if len(x) < 2:
        print(f"⚠️ Skipping {m1} vs {m2}: not enough data")
        continue

    # Pearson correlation
    r, pval = pearsonr(x, y)

    # Linear regression
    slope, intercept = np.polyfit(x, y, 1)
    fit_line = slope * x + intercept

    # Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, alpha=0.7, label="Data")
    plt.plot(x, fit_line, color="red", lw=2,
             label=f"Fit: y={slope:.2f}x+{intercept:.2f}")
    plt.xlabel(f"{m1} Relative Energies (kcal/mol)")
    plt.ylabel(f"{m2} Relative Energies (kcal/mol)")
    plt.title(f"{m1} vs {m2}\nPearson r = {r:.3f}, p = {pval:.2e}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"Correlation_{m1}_vs_{m2}.png", dpi=300)
    plt.close()

    print(f"{m1} vs {m2}: r={r:.3f}, slope={slope:.3f}, intercept={intercept:.3f}, n={len(x)}")
