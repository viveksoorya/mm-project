for j in a; do
	for dir in xtb-goat/${j}/${j^^}_CONF; do
		for conformer in 0; do
			echo -e "! 6-31G** 387-D\n\n* xyzfile 0 1 ${dir}/${conformer}.xyz" > 387-D/${j}/${j}.inp
		done
	done
done
