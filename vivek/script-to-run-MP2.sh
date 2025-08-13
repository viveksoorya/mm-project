for j in d g k ; do
	for dir in xtb-goat/${j}/${j^^}_CONF; do
		mkdir MP2/${j}/
		for conformer in 0 1 2 3 4 5; do
			mkdir MP2/${j}/${conformer}
			echo -e "! MP2 6-31G** \n\n* xyzfile 0 1 /home/vivek/mm-project/vivek/${dir}/${conformer}.xyz" > /home/vivek/mm-project/vivek/MP2/${j}/${conformer}/${conformer}.inp
			cd /home/vivek/mm-project/vivek/MP2/${j}/${conformer}/
			orca ${conformer}.inp > ${conformer}.out
			cd /home/vivek/mm-project/vivek/ 
		done
	done
done
# Creates a directory for each conformer for each amino acid
# creates inpute file for MP2 for each confomer for each amino acid
# goes into the conformer folder runs the orca program and comes back out 
