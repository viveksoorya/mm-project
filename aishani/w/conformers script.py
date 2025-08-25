import re
import os

# Input ORCA output file
input_file = "w.out"

# Read file
with open(input_file, "r") as f:
    content = f.read()

# Regex to capture "CARTESIAN COORDINATES (ANGSTROEM)" blocks
pattern = re.compile(r"CARTESIAN COORDINATES \(ANGSTROEM\)(.*?)\n\s*\n", re.DOTALL)
matches = pattern.findall(content)

# Take first 6 geometries
geometries = matches[:6]

# Output folder
output_dir = "orca_inputs"
os.makedirs(output_dir, exist_ok=True)

# ORCA input templates
template_b97d = """! B97-D3 def2-SVP TightSCF SP

* xyz 0 1
{coords}
*
"""

template_mp2 = """! MP2 def2-SVP TightSCF SP

* xyz 0 1
{coords}
*
"""

# Function to extract geometry
def extract_coords(geom_block):
    lines = [line.strip() for line in geom_block.strip().split("\n")]
    atoms = []
    for line in lines[1:]:  # skip the header line
        parts = line.split()
        if len(parts) >= 4:
            atom, x, y, z = parts[0], parts[1], parts[2], parts[3]
            atoms.append(f"{atom} {x} {y} {z}")
    return "\n".join(atoms)

# Generate input files
for i, geom in enumerate(geometries, start=1):
    coords = extract_coords(geom)
    
    # Write B97-D input
    with open(os.path.join(output_dir, f"conf{i}_B97D.inp"), "w") as f:
        f.write(template_b97d.format(coords=coords))
    
    # Write MP2 input
    with open(os.path.join(output_dir, f"conf{i}_MP2.inp"), "w") as f:
        f.write(template_mp2.format(coords=coords))

print(f"Generated input files in folder: {output_dir}")
