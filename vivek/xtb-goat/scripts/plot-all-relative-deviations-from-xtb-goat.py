import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l']

# Initialize containers for the three datasets
all_aas_1, all_energies_1 = [], []
all_aas_2, all_energies_2 = [], []

# Dataset 1 (from first case)
for xaa in categories:
        with open("B97-D/" + xaa + "/DEVIATIONS-OF-XTB-GOAT", 'r') as file:
                    energies = [float(line.strip()) for line in file if line.strip()]
                    all_aas_1.extend([xaa.upper()] * len(energies))
                    all_energies_1.extend(energies)

                    # Dataset 2 (second case)
                    for xaa in categories:
                            with open("MP2/" + xaa + "/DEVIATIONS-OF-XTB-GOAT", 'r') as file:
                                        energies = [float(line.strip()) for line in file if line.strip()]
                                        all_aas_2.extend([xaa.upper()] * len(energies))
                                        all_energies_2.extend(energies)

                                        fig, ax = plt.subplots(figsize=(12, 6))

                                        # Plot dataset 1
                                        ax.scatter(all_aas_1, all_energies_1, marker='_', s=100, color='blue', label='B97-D')

                                        # Plot dataset 2
                                        ax.scatter(all_aas_2, all_energies_2, marker='_', s=100, color='red', label='MP2')
                                        ax.set_ylabel('kcal per mol')
                                        plt.grid(True, axis='y')
                                        plt.legend()
                                        plt.savefig("DEVIATIONS-OF-XTB-GOAT")
                                        plt.close(fig)
                                        plt.title("Deviations of xTB-GOAT from B97-D and MP2")



