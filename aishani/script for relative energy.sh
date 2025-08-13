for j in m n p q r s t v w y; do
	awk 'NR==1 {tmp=$1} {print $1 - tmp}' ${j}/${j^^}.ENERGIES > ${j}/${j^^}.Relative-ENERGIES 
done
