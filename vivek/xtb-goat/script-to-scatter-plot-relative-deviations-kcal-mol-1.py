import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l']
# categories = ['a']
# x_pos = np.arange(len(categories))

all_aas = []
all_energies = []
 
for xaa in categories:
   with open(xaa + "/" + xaa.upper() + ".Relative-ENERGIES-kcal-per-mol", 'r') as file:
        energies = [float(line.strip()) for line in file if line.strip()]
        all_aas.extend([xaa.upper()] * len(energies))
        all_energies.extend(energies)

fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(all_aas, all_energies, marker='_', s=100)
ax.set_xlabel('Amino Acid ')
ax.set_ylabel('kcal per mol')
plt.grid(True, axis='y')
plt.savefig("kcal-mol-1-dashes.png")
plt.close(fig)
