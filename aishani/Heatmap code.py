import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load summary file
df = pd.read_csv("summary_RMSD.csv")

# Select only mean columns (ignore std)
mean_cols = [c for c in df.columns if "mean" in c]
df_means = df.set_index("amino_acid")[mean_cols]

# Sort amino acids only by MP2 vs B97D mean RMSD
df_sorted = df_means.sort_values("MP2_vs_B97D_mean")

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df_sorted, annot=True, cmap="viridis", cbar_kws={'label': 'RMSD (Å)'})
plt.title("Amino Acid RMSD Heatmap (sorted by MP2 vs B97D mean)")
plt.xlabel("Comparison")
plt.ylabel("Amino Acid (sorted by MP2 vs B97D)")
plt.tight_layout()
plt.savefig("RMSD_heatmap_sorted_MP2vsB97D.png", dpi=300)
plt.show()
