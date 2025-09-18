import pandas as pd
import matplotlib.pyplot as plt

# Combined MAD data
data = {
    "Amino Acid": ["A","C","D","E","F","G","H","I","K","L",
                   "M","N","P","Q","R","S","T","V","W","Y"],
    "XTB vs B97-D": [0.847,0.864,0.485,1.785,0.600,0.751,5.018,0.436,0.529,0.589,
                     0.137,0.375,0.561,0.224,0.904,0.537,0.096,0.150,2.073,0.220],
    "XTB vs MP2": [0.620,0.888,1.329,2.140,0.642,0.325,7.869,0.896,0.780,1.043,
                   0.049,0.709,0.543,0.189,0.696,0.790,0.340,0.370,2.111,0.265]
}
df = pd.DataFrame(data)

# Summary statistics
min_val = df[["XTB vs B97-D","XTB vs MP2"]].min().min()
max_val = df[["XTB vs B97-D","XTB vs MP2"]].max().max()
avg_val = df[["XTB vs B97-D","XTB vs MP2"]].stack().mean()

# Create figure
fig, ax = plt.subplots(figsize=(10,6))
ax.axis('off')

# Table data
table_data = df.round(3).values.tolist()
columns = df.columns.tolist()

# Add a row for average
table_data.append(["—","—", round(avg_val,3)])
columns_out = columns

# Create table
table = ax.table(cellText=table_data, colLabels=columns_out, cellLoc='center',
                 loc='center')

# Highlight cells
for (i,j), cell in table.get_celld().items():
    if i == 0:  # header row
        cell.set_facecolor("#cccccc")
        cell.set_text_props(weight="bold")
    elif j > 0 and i > 0:
        val = table_data[i-1][j]
        if isinstance(val, (float,int)):
            if abs(val - min_val) < 1e-6:
                cell.set_facecolor("lightgreen")  # minimum
            elif abs(val - max_val) < 1e-6:
                cell.set_facecolor("lightcoral")  # maximum
            elif abs(val - round(avg_val,3)) < 1e-6:
                cell.set_facecolor("lightblue")   # average

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2,1.2)

plt.savefig("MAD_summary_table.png", dpi=300, bbox_inches="tight")
plt.show()
