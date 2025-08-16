import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l']
x_pos = np.arange(len(categories))


for xaa in categories:

    fig, ax = plt.subplots(figsize=(12, 6))
    with open(xaa + "/" + xaa.upper() + ".ENERGIES", 'r') as file:
        energies = [float(line.strip()) for line in file if line.strip()]
    category_stack = np.full(6, xaa)
    ax.scatter(category_stack, energies, marker='x', s=100)
    ax.set_xlabel('Amino Acid ')
    ax.set_ylabel('Energy (Hartrees)')
    ax.set_title('Scatter Plot for amino acid ' + xaa.upper())
    plt.grid(True, axis='y')
    plt.savefig(xaa + "/" + xaa.upper()+ ".png")
    plt.close(fig)
