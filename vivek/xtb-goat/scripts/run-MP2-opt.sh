dir=/home/vivek/mm-project/vivek/xtb-goat/MP2-opt
cd $dir
for j in k; do
	cd $j
	for num in 0 1; do
		cd $num
		/home/test/orca/orca_6_1_0_linux_x86-64_shared_openmpi418/orca $num.inp > $num.out
		cd ..
	done
	cd ..
done
for j in h; do
	cd $j
	for num in 1 5; do
		cd $num
		/home/test/orca/orca_6_1_0_linux_x86-64_shared_openmpi418/orca $num.inp > $num.out
		cd ..
	done
	cd ..
done
