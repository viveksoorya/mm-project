for j in d g k; do
	awk '{print $1 * 627.509}' "${j}/${j^^}.Relative-ENERGIES" > "${j}/${j^^}.Relative-ENERGIES-kcal-per-mol"
done
