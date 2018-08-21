def checkPowerSetResult(actual, expected):
	pass

def powerSetSpec(f):
	# Need to include null set?
	A0 = [1]
	E0 = [[1]]
	R0 = f(A0)
	checkPowerSetResult(R0, E0)

	A1 = [1,2]
	E1 = [[1], [2], [1,2]]
	R1 = f(A1)
	checkPowerSetResult(R1, E1)

	A2 = [1,2,3]
	E2 = [[1], [2], [3], [1,2], [2,3], [1,2,3]]
	R2 = f(A2)
	checkPowerSetResult(R2, E2)