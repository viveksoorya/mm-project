for j in g h i k l; do
	cd ${j}/${j^^}_CONF
	for file in *; do
		mv ${file} ${file}.xyz
	done
	cd ../..
done
