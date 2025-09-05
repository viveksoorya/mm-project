import matplotlib.pyplot as plt
import numpy as np

categories = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l']

# Initialize containers for the three datasets
all_aas_1, all_energies_1 = [], []
all_aas_2, all_energies_2 = [], []
all_aas_3, all_energies_3 = [], []

# Dataset 1 (from first case)
for xaa in categories:
        with open("xtb-goat/" + xaa + "/Relative-ENERGIES-kcal-per-mol", 'r') as file:
                    energies = [float(line.strip()) for line in file if line.strip()]
                    all_aas_1.extend([xaa.upper()] * len(energies))
                    all_energies_1.extend(energies)

                    # Dataset 2 (second case)
                    for xaa in categories:
                            with open("MP2/" + xaa + "/Relative-ENERGIES-kcal-per-mol", 'r') as file:
                                        energies = [float(line.strip()) for line in file if line.strip()]
                                        all_aas_2.extend([xaa.upper()] * len(energies))
                                        all_energies_2.extend(energies)

                                                        # Dataset 3 (third case)
                                        for xaa in categories:
                                                with open("B97-D/" + xaa + "/Relative-ENERGIES-kcal-per-mol", 'r') as file:
                                                            energies = [float(line.strip()) for line in file if line.strip()]
                                                            all_aas_3.extend([xaa.upper()] * len(energies))
                                                            all_energies_3.extend(energies)

                                                            fig, ax = plt.subplots(figsize=(12, 6))

                                                            # Plot dataset 1
                                                            ax.scatter(all_aas_1, all_energies_1, marker='_', s=100, color='blue', label='xtb-goat')

                                                            # Plot dataset 2
                                                            ax.scatter(all_aas_2, all_energies_2, marker='_', s=100, color='red', label='MP2')

                                                            # Plot dataset 3
                                                            ax.scatter(all_aas_3, all_energies_3, marker='_', s=100, color='green', label='B97-D')

                                                            ax.set_xlabel('Amino Acid')
                                                            ax.set_ylabel('kcal per mol')
                                                            plt.grid(True, axis='y')
                                                            plt.legend()
                                                            plt.savefig("Relative-Energies-three-Methods.png")
                                                            plt.close(fig)



