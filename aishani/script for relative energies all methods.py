import matplotlib.pyplot as plt
import numpy as np

categories = ['m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']
methods = {
    "Relative-ENERGIES": "XTB",
    "Relative_B97D": "B97D",
    "Relative_MP2": "MP2"
}
colors = {"XTB": "tab:blue", "B97D": "tab:orange", "MP2": "tab:green"}

fig, ax = plt.subplots(figsize=(12, 6))

for method_file, method_name in methods.items():
    all_aas = []
    all_energies = []

    for xaa in categories:
        filepath = f"{xaa}/{xaa.upper()}.{method_file}"
        with open(filepath, 'r') as file:
            energies = [float(line.strip()) for line in file if line.strip()]
            all_aas.extend([xaa.upper()] * len(energies))
            all_energies.extend(energies)

    ax.scatter(all_aas, all_energies, marker='_', s=100,
               color=colors[method_name], label=method_name)

ax.set_xlabel('Amino Acid')
ax.set_ylabel('kcal per mol')
ax.legend(title="Method")
plt.grid(True, axis='y')
plt.savefig("kcal-mol-dashes.png")
plt.close(fig)
