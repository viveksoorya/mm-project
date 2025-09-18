import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

root = "/home/uni/molmod/mm-project/vivek/xtb-goat"
amino_acids = [aa for aa in (chr(i) for i in range(ord('A'), ord('L') + 1)) if aa not in ('B', 'J')]
conformers = range(6)
aa_codes = [aa.lower() for aa in amino_acids] 

# Define RMSD sets config:
rmsd_sets = {
            "B97-D-opt_vs_xtbgoat": {
                        "folder": "B97-D-opt",
                                "filename_pattern": "{}.rmsd"
                                    },
                "MP2-opt_vs_xtbgoat": {
                            "folder": "MP2-opt",
                                    "filename_pattern": "{}.rmsd"
                                        },
                    "MP2-opt_vs_B97-D-opt": {
                                "folder": "MP2-opt",
                                        "filename_pattern": "{}.rmsdWithB97-D-opt"
                                            }
                    }

def read_rmsd_value(filepath):
        try:
                    with open(filepath, 'r') as f:
                            val_str = f.read().strip()
                            return float(val_str)
        except Exception as e:
                            print(f"Warning: Could not read {filepath}: {e}")
                            return np.nan

data = {pair_name: [] for pair_name in rmsd_sets.keys()}

for aa, aa_code in zip(amino_acids, aa_codes):
    for pair_name, conf in rmsd_sets.items():
         folder = conf["folder"]
         filename_pattern = conf["filename_pattern"]
         rmsds_for_conformers = []
         for conf_idx in conformers:
                                                                                                                            filepath = os.path.join(root, folder, aa_code, str(conf_idx), filename_pattern.format(conf_idx))
                                                                                                                            rmsd_val = read_rmsd_value(filepath)
                                                                                                                            rmsds_for_conformers.append(rmsd_val)
         mean_rmsd = np.nanmean(rmsds_for_conformers)  # mean over conformers for this amino acid and RMSD pair
         data[pair_name].append(mean_rmsd)
df = pd.DataFrame(data, index=amino_acids)

plt.figure(figsize=(10, 8))
sns.heatmap(df, cmap='viridis', annot=True, fmt=".3f", cbar_kws={'label': 'Mean RMSD'})
plt.xlabel("RMSD Pair")
plt.ylabel("Amino Acid")
plt.title("Mean RMSD per Amino Acid across RMSD Pairs")
plt.tight_layout()
plt.savefig("heatmap.png", dpi=300, bbox_inches='tight')
plt.show()

