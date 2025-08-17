dir=/home/uni/mm-project/vivek/xtb-goat/
cd $dir
for j in a c d e f g h i k l; do
	for conformer in 0 1 2 3 4 5; do
		diff=$(echo "$(awk -v line=$((conformer+1)) 'NR==line {print $1}' "$dir/xtb-goat/$j/ENERGIES") - $(awk -v line=$((conformer+1)) 'NR==line {print $1}' "$dir/MP2/$j/ENERGIES")" | bc)
		abs_diff=$(echo "$diff" | awk '{if($1<0) print -$1; else print $1}')
		echo $abs_diff >> "MP2/$j/DEVIATIONS-OF-XTB-GOAT"
	done
done
