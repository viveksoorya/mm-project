for j in a c d e f g h i k l; do
	awk '{print $1 * 627.509}' "${j}/${j^^}.Relative-ENERGIES" > "${j}/${j^^}.Relative-ENERGIES-kcal-per-mol"
done
