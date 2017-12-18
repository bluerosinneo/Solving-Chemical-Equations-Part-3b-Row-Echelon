# This code follows the following post.
# http://cramerexplainsmath.com/2017/12/18/solving-chemical-equations-part-3b-row-echelon/
# @desc A basic driver that of rowEchelon.  A detailed description of each
# method can be found in the post
# @author Cramer Grimes cramergrimes@gmail.com

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