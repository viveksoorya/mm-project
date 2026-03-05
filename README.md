# MM Project

Computational chemistry project comparing XTB (extended tight binding) method performance against higher-level quantum chemistry methods (MP2 and B97-D) for amino acid conformational analysis. Done under the supervision of Dr. Brijesh Mishra (Krea University), in collaboration with Ms. Aishani Tewari (a fellow undergraduate student of Krea University)

## Project Structure

```
.
├── README.md                      # This file
├── README_xyz_format.md           # Original XYZ coordinate format documentation
├── table.py                       # Script to generate MAD summary table
├── MAD_summary_table.png          # Mean Absolute Deviation (MAD) comparison table
├── MAD_XTB_vs_methods.csv         # Raw MAD data
├── schmitz2020.pdf                # Reference paper
├── vivek/                         # Vivek's calculations
│   ├── xtb-goat/                  # XTB method results
│   ├── MP2-goat/                  # MP2 method results
│   ├── B97-D-goat/                # B97-D method results
│   └── hpc-goat-MP2-B97-D/        # HPC cluster results
└── aishani/                       # Aishani's work
    └── p/                         # Proline conformer analysis
        ├── orca_inputs/           # ORCA quantum chemistry input files
        ├── p.*                     # XTB calculation outputs
        └── conformers script.py   # Conformer generation script
```

## Methods Compared

- **XTB**: Extended Tight Binding - semi-empirical quantum chemistry method
- **B97-D**: DFT method with dispersion correction
- **MP2**: Second-order Møller-Plesset perturbation theory

## Data

The `MAD_XTB_vs_methods.csv` file contains Mean Absolute Deviation (MAD) values comparing XTB against B97-D and MP2 for all 20 standard amino acids.

## Usage

Generate the MAD summary table:
```bash
python table.py
```

This will produce `MAD_summary_table.png` with color-coded comparison values.
