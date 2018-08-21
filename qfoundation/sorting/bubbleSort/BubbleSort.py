def bubbleSort(A):
	maxIndex = len(A)
	isSorted = False 
	totalSwaps = 0

	while (not isSorted):
		numSwapsI = 0
		for i in range(0, maxIndex - 1, 1):
			currVal = A[i]
			nextVal = A[i+1]
			if currVal > nextVal:
				A[i+1] = currVal
				A[i] = nextVal
				numSwapsI += 1 
		
		totalSwaps += numSwapsI
		if numSwapsI == 0:
			isSorted = True 

	return A