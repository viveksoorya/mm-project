dir=/home/vivek/mm-project/vivek/xtb-goat/B97-D-opt
cd $dir
for j in d e f g h i k l; do
	cd $j
	for num in 0 1 2 3 4 5; do
		cd $num
		rm $num.out
		sudo /home/test/orca/orca_6_1_0_linux_x86-64_shared_openmpi418/orca $num.inp > $num.out
		cd ..
	done
	cd ..
done
