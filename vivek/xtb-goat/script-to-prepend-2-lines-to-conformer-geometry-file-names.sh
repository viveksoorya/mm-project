for j in  l; do
	cd ${j}/${j^^}_CONF
	for file in 0 1 2 3 4 5 ; do
		lines=$(cat ${file}.xyz | wc -l)
		sed -i '1i'"$lines\n$j"', conformer '"$file" ${file}.xyz
	done
	cd ../../
done
