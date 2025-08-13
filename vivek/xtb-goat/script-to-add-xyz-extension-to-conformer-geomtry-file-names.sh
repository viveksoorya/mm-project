for j in a; do
	cd ${j}/${j^^}_CONF
	for file in *; do
		echo ${file}
		mv ${file} ${file}.xyz
	done
	cd ..
done
