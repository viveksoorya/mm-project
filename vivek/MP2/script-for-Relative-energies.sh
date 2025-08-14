for j in a; do
	awk 'NR==1 {tmp=$1} {print $1 - tmp}' ${j}/ENERGIES > ${j}/Relative-ENERGIES 
done
