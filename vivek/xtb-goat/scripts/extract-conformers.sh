for j in l; do
	cd $j
	nlines=$(awk 'NR==1 {print $1}' $j-input-coordinates.xyz)
	split -l $(($nlines+2)) -d -a 1 --additional-suffix=.xyz "$j.finalensemble.xyz" ''
	rm {6,7,8,9}.xyz
	cd ..
done
