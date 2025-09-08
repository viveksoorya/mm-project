import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Load summary
summary_df = pd.read_csv("summary_RMSD.csv")

# ---------------- Bar Plot (mean RMSD per amino acid) ---------------- #
plt.figure(figsize=(10,6))
bar_df = summary_df.melt(id_vars="amino_acid",
                         value_vars=[c for c in summary_df.columns if "_mean" in c],
                         var_name="Comparison", value_name="Mean RMSD")

sns.barplot(data=bar_df, x="amino_acid", y="Mean RMSD", hue="Comparison", errorbar=None)
plt.title("Mean RMSD per Amino Acid")
plt.ylabel("RMSD (Å)")
plt.xlabel("Amino Acid")
plt.legend(title="Comparison", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("BarPlot_Mean_RMSD.png", dpi=300)
plt.close()

# ---------------- Heatmap (mean RMSD per amino acid & comparison) ---------------- #
heatmap_df = summary_df.set_index("amino_acid")[
    [c for c in summary_df.columns if "_mean" in c]
]

plt.figure(figsize=(10,6))
sns.heatmap(heatmap_df, annot=True, cmap="viridis", cbar_kws={'label': 'Mean RMSD (Å)'})
plt.title("Heatmap of Mean RMSDs")
plt.ylabel("Amino Acid")
plt.xlabel("Comparison")
plt.tight_layout()
plt.savefig("Heatmap_Mean_RMSD.png", dpi=300)
plt.close()
