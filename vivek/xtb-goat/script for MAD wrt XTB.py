import os
import numpy as np

# Define paths
base_dir = "xtb-goat"   # starting point
methods = ["B97-D", "MP2"]   # compare XTB against these
amino_acids = ['a','c','d','e','f','g','h','i','k','l']  # expand if needed

mad_results = []

for method in methods:
    for aa in amino_acids:
        deviation_file = os.path.join(base_dir, method, aa, "DEVIATIONS-OF-XTB-GOAT")
        
        if os.path.exists(deviation_file):
            with open(deviation_file, 'r') as f:
                values = [float(line.strip()) for line in f if line.strip()]
            
            mad = np.mean(np.abs(values))
            mad_results.append({
                "Amino Acid": aa.upper(),
                "Comparison": f"XTB vs {method}",
                "MAD": mad
            })
        else:
            mad_results.append({
                "Amino Acid": aa.upper(),
                "Comparison": f"XTB vs {method}",
                "MAD": None
            })

# Print results
print("=== MAD values ===")
for res in mad_results:
    print(res)

# Optional: save as CSV
import pandas as pd
df = pd.DataFrame(mad_results)
df.to_csv("MAD_XTB_vs_methods.csv", index=False)
