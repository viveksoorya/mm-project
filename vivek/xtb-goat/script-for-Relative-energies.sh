for j in d g k; do
	awk 'NR==1 {tmp=$1} {print $1 - tmp}' ${j}/${j^^}.ENERGIES > ${j}/${j^^}.Relative-ENERGIES 
done
