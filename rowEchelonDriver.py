from rowEchelon import rowEchelon

A = [[1,0,-3,0],
	[1,0,0,-2],
	[4,10,-4,-7],
	[0,4,-1,0]]

print "--Before Row Echelon--"
rowEchelon.showMatrix(A)
rowEchelon.solveRowEchelon(A)
print "--After Row Echelon--"
rowEchelon.showMatrix(A)