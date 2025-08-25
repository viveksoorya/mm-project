for j in a l; do
	awk '{print $1 * 627.509}' "${j}/Relative-ENERGIES" > "${j}/Relative-ENERGIES-kcal-per-mol"
done
