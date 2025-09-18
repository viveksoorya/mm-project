#To plot correlations I need two axes of data where each axis has relative energies of all 60 conformers

#MP2 wrt B97-D 

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

amino_acids =  ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l']

relative_energies_B97D = []
relative_energies_MP2 = []

for xaa in amino_acids:
    with open("B97-D/" + xaa + "/absolute-Relative-ENERGIES-kcal-per-mol", 'r') as file:
        vals = [float(line.strip()) for line in file if line.strip()]
        relative_energies_B97D.extend(vals)

for xaa in amino_acids:
    with open("MP2/" + xaa + "/absolute-Relative-ENERGIES-kcal-per-mol", 'r') as file:
        vals = [float(line.strip()) for line in file if line.strip()]
        relative_energies_MP2.extend(vals)


x = relative_energies_B97D
y = relative_energies_MP2
#print(x)
#print(len(x))
#print(y)
#print(len(y))

r, p = pearsonr(x, y)
plt.scatter(x, y, label='data')
plt.xlim(0, 15)
plt.ylim(0, 5)
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
plt.plot(np.unique(x), poly(np.unique(x)), color='red', label = f"Fit: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}")

plt.text(0.05, 0.95, f'Pearson r = {r:.3f}\np-value={p:.3g}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
plt.title('Correlation')
plt.xlabel('B97-D Relative energy in kcal per mol')
plt.ylabel('MP2 Relative energy in kcal per mol')
plt.legend()
plt.savefig('MP2_vs_B97-D.png', dpi=600)
plt.show()
