dir=/home/uni/molmod/mm-project/vivek/xtb-goat
cd $dir
method=MP2-opt
cd $method

for j in a c d e f g h i k l; do
	for n in 0 1 2 3 4 5; do
		upper_j=${j^^}
		fileB97=$dir/B97-D-opt/$j/$n/$n.xyz
		fileMP2=$dir/$method/$j/$n/$n.xyz
		chmod +x $fileB97
		chmod +x $fileMP2
		nlines=$( echo "$(wc -l < $fileB97) - 2" | bc)
		sum=0
		for ((line=3; line<=nlines; line++)); do
			#extract the second, third and forth terms, from each file, 
			dev_x=$(echo "scale=14;  $(awk -v line="$line" 'NR==line {print $2}' $fileB97) - $(awk -v line="$line" 'NR==line {print $2}' $fileMP2) " | bc -l)
			dev_y=$(echo "scale=14;  $(awk -v line="$line" 'NR==line {print $3}' $fileB97) - $(awk -v line="$line" 'NR==line {print $3}' $fileMP2) " | bc -l)
			dev_z=$(echo "scale=14;  $(awk -v line="$line" 'NR==line {print $4}' $fileB97) - $(awk -v line="$line" 'NR==line {print $4}' $fileMP2) " | bc -l)
			local_sum=$(echo "scale=14; ($dev_x * $dev_x) + ($dev_y * $dev_y) + ($dev_z * $dev_z)" | bc)
			sum=$(echo "scale=14; $sum + $local_sum" | bc)
		done
		mean=$(echo "scale=14; $sum / $nlines" | bc -l)
		root=$(echo "scale=14; sqrt($mean)" | bc -l)
		echo "$root" > $dir/$method/$j/$n/$n.rmsdWithB97-D-opt
	done
done
