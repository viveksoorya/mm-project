for j in a; do
	awk '{print $1 * 627.509}' "${j}/Relative-ENERGIES" > "${j}/Relative-ENERGIES-kcal-per-mol"
done
