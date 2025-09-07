dir=/home/vivek/mm-project/vivek/xtb-goat
cd $dir
method=MP2-opt
cd $method
file=$dir/$method/rmsd-MP2opt-with-xtbgoat
cat $file

AA=(A C D E F G H I K L)
awk -v prefix="$j" 'BEGIN{aa="a c d e f g h i k l"; split(aa, arr, " "); idx=1}; NR%7==0{if(n){printf "%s:\t%.14f\n", arr[idx], sum/n; sum=0; n=0; idx++}} NR%7!=0 {sum+=$3; n++} END{if(n) printf "%s:\t%.14f\n", arr[idx], sum/n}' "$file" >> $dir/$method/amino-acid-wise---rsmd-MP2opt-with-xtb-goat

