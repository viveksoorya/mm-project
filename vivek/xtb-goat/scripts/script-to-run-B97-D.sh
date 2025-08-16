for j in l; do
	for dir in xtb-goat/${j}/${j^^}_CONF; do
		mkdir B97\-D/${j}/
		for conformer in 0 1 2 3 4 5; do
			mkdir B97\-D/${j}/${conformer}
			echo -e "! B97-D 6-31G** \n\n* xyzfile 0 1 /home/vivek/mm-project/vivek/xtb-goat/${dir}/${conformer}.xyz" > /home/vivek/mm-project/vivek/xtb-goat/B97\-D/${j}/${conformer}/${conformer}.inp
			cd /home/vivek/mm-project/vivek/xtb-goat/B97\-D/${j}/${conformer}/
			orca ${conformer}.inp > ${conformer}.out
			cd /home/vivek/mm-project/vivek/xtb-goat/ 
		done
	done
done
# Creates a directory for each conformer for each amino acid
# creates inpute file for B97-D for each confomer for each amino acid
# goes into the conformer folder runs the orca program and comes back out 
