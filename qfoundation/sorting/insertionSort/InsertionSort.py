def insertionSort(A):
	for i in range(0, len(A), 1):
		for j in range(i-1, -1, -1):
			currVal = A[j + 1]
			prevVal = A[j]
			if prevVal > currVal:
				A[j] = currVal
				A[j + 1] = prevVal

	return A


