#!/usr/bin/env python3
"""
MAD Calculator for Relative Energies
------------------------------------

This script calculates the Mean Absolute Deviation (MAD) between
XTB, B97D, and MP2 relative energy files across multiple amino acids.

Expected file structure:
  m/M.Relative-ENERGIES
  m/M.Relative-B97D
  m/M.Relative-MP2
  n/N.Relative-ENERGIES
  ...

Usage:
  python mad_calculator.py
"""

import os
import numpy as np

# List of amino acids (folder names, lowercase)
CATEGORIES = ['m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']

# Mapping of filenames to method labels
METHODS = {
    "Relative-ENERGIES": "XTB",
    "Relative_B97D": "B97D",
    "Relative_MP2": "MP2"
}

OUTPUT_FILE = "MAD_results.txt"

def load_values(filepath):
    """Load energy values from a file into a list of floats."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return [float(line.strip()) for line in f if line.strip()]
    return []

def main():
    # Store MAD results
    mad_results = {("XTB","B97D"): {}, ("B97D","MP2"): {}, ("XTB","MP2"): {}}
    overall_data = {("XTB","B97D"): [], ("B97D","MP2"): [], ("XTB","MP2"): []}

    for xaa in CATEGORIES:
        # Load per-amino-acid data
        aa_data = {}
        for method_file, method_name in METHODS.items():
            filepath = f"{xaa}/{xaa.upper()}.{method_file}"
            aa_data[method_name] = load_values(filepath)

        # Align conformers (truncate to smallest length)
        min_len = min(len(aa_data["XTB"]), len(aa_data["B97D"]), len(aa_data["MP2"]))
        if min_len == 0:
            continue  # skip if missing data

        for m1, m2 in mad_results.keys():
            x = np.array(aa_data[m1][:min_len])
            y = np.array(aa_data[m2][:min_len])
            mad = np.mean(np.abs(x - y))  # mean absolute deviation
            mad_results[(m1, m2)][xaa.upper()] = mad

            # Store for overall MAD
            overall_data[(m1, m2)].extend(np.abs(x - y))

    # Write results to file
    with open(OUTPUT_FILE, "w") as f:
        f.write("=== Mean Absolute Deviations per amino acid ===\n")
        for pair, results in mad_results.items():
            f.write(f"\n{pair[0]} vs {pair[1]}:\n")
            for aa, mad in results.items():
                f.write(f"  {aa}: {mad:.3f} kcal/mol\n")

        f.write("\n=== Total Mean Absolute Deviations (across all amino acids) ===\n")
        for pair, diffs in overall_data.items():
            if len(diffs) > 0:
                total_mad = np.mean(diffs)
                f.write(f"{pair[0]} vs {pair[1]}: {total_mad:.3f} kcal/mol\n")

    print(f"✅ Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
