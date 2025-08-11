for j in a c d e f g h i k l; do
	awk 'NR==1 {tmp=$1} {print $1 - tmp}' ${j}/${j^^}.ENERGIES > ${j}/${j^^}.Relative-ENERGIES 
done
