# I want to add all the values in a DEVIATIONS file
dir=/home/uni/molmod/mm-project/vivek/xtb-goat/MP2
exec > $dir/MAD
sumAllconfs=0
for j in a c d e f g h i k l; do
	avg6confs=$(awk 'NR>=1 && NR<=6 {local_sum += $1} END {print local_sum/6}' "$dir/$j/DEVIATIONS-OF-XTB-GOAT")
	echo -e "MAD value of " $j ":\t" $avg6confs
	sumAllconfs=$(echo "$avg6confs + $sumAllconfs" | bc)
done
mad=$(echo "scale=2; $sumAllconfs / 10" | bc)
echo -e "Mean Absolute Deviation: \t" $mad

