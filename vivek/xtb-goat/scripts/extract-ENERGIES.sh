for j in l; do
	for file in 0 1 2 3 4 5; do
		awk 'NR==2 {print $1}' $j/${j^^}"_CONF"/$file.xyz >> $j/ENERGIES
	done
done
