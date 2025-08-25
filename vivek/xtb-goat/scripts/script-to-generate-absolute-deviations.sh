# aim: to get absolute deviations for all conformers of all amino acids 
# outer loop amino acids; inner loop through lines of amino acid energy file
# run this file from the parent folder
# conformer energy deviation = xtb-goat/$j/${j^^}.ENERGIES.line - B97-D/$j/ENERGIES.line
# conformer energy deviation = xtb-goat/$j/${j^^}.ENERGIES.line - MP2/$j/ENERGIES.line
# wrap this in an absolute value function to get absolute deviation
# scale this up through loops and also in the end generate one mean absolute deviation value for all 60 conformers together.
