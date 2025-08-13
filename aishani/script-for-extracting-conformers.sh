# extract the number from the first line in the finalensemble
# go to line 3
# cat the next n lines to a file k in 0 1 2 3 4 5
# after each cat skip 2 lines

for xaa in m n p q r s t v w y; do
	file=${xaa}/${xaa}.finalensemble.xyz
	n=$(head -n 1 "$file" | awk '{print $1}')
	
	startline=3
	for conformer in 0 1 2 3 4 5; do
		endline=$((startline + n - 1))
		sed -n "${startline},${endline}p" "$file" > "$xaa/$conformer"
		startline=$((endline+3))
	done
done
