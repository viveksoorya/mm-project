set -e

for j in e f g h i k l; do 
	mkdir ${j}
	git mv ${j}.inp ${j}-input-coordinates.xyz -t ${j}
	cd ${j}
	/home/uni/orca_6_1_0/orca ${j}.inp > ${j}.out
	wait
	cd ..
done
