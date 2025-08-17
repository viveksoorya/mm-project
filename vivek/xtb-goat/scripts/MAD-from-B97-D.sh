# I want to add all the values in a DEVIATIONS file
dir=/home/uni/mm-project/vivek/xtb-goat/B97-D
exec > $dir/MAD
sumAllconfs=0
for j in a c d e f g h i k l; do
	sum6confs=$(awk 'NR>=1 && NR<=6 {local_sum += $1} END {print local_sum}' "$dir/$j/DEVIATIONS-OF-XTB-GOAT")
	echo -e $j "\t" $sum6confs
	sumAllconfs=$(echo "$sum6confs + $sumAllconfs" | bc)
done
mad=$(echo "$sumAllconfs / 60" | bc)
echo -e "grand sum: \t" $sumAllconfs
echo -e "Mean Absolute Deviation: \t" $mad

