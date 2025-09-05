for j in a c d e f g h i k l; do
	touch "${j}/absolute-Relative-ENERGIES-kcal-per-mol"
	awk '{print ($1 < 0) ? -$1 : $1}' "${j}/Relative-ENERGIES-kcal-per-mol" > "${j}/absolute-Relative-ENERGIES-kcal-per-mol"
done
