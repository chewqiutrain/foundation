def powerSetAlgo1(A):
	'''A is a set
	let n be the number of elements in A. i.e. len(A) == n
	1. we know number of powersets = 2 ** n
	2. for i in range(0, 2**n), convert each i to bits, then 
		use the individual bits as indicator functions corresponding to
		each element in A.
		If bit == 1, then take element from A and append to powerset.
	3. return all powersets
	'''
	def int2Bits(intI, maxBits):
		# O(1)?
		bitStr = bin(intI)[2:]
		fillLeft = maxBits - len(bitStr)
		bitStr = ('0' * fillLeft) + bitStr
		return bitStr

	def subsetFromBits(AList, bits):
		# O(n)
		subset = list()
		for idx, bi in enumerate(bits):
			if bi == '1':
				subset.append(AList[idx])
		return set(subset)

	def getPowerSets(A):
		AList = list(A)
		numMaxSets = 2 ** len(A)
		numMaxBits = len(bin(numMaxSets)[2:]) - 1
		powersets = list()

		# total run time = O(n 2^n)?!?!
		for i in range(0, numMaxSets, 1): # outer loop = O(2^n) ?
			bitsI = int2Bits(i, numMaxBits)
			powersets.append(subsetFromBits(AList, bitsI)) 
		return powersets

	return getPowerSets(A)

def powerSetAlgo2(A):
	# O(n!) ?
	powerset = set()
	if len(A) == 1:
		powerset.add(frozenset(A))
		return powerset

	for i in A:
		yi = A - set([i])
		powerset.add(frozenset(powerSetAlgo2(yi)))

	powerset.add(frozenset(A))
	return powerset 

def powerSetAlgo3(A):
	# O(n * 2^n)
	acc = [set()]
	AList = list(A)
	for i in AList:
		accCopy = [j.copy() for j in acc]
		for subsetJ in acc:
			subsetJ.add(i)

		acc = acc + accCopy

	return acc 



def test(powerSetOf):
	A0 = set([])
	A1 = set([0,1])
	A2 = set([0,1,2])
	A3 = set([0,1,2,3])

	R0 = powerSetOf(A0)
	R1 = powerSetOf(A1)
	R2 = powerSetOf(A2)
	R3 = powerSetOf(A3)
	print(R0)
	print('\n')
	print(R1)
	print('\n')
	print(R2)
	print('\n')
	print(R3)


test(powerSetAlgo3)
