def merge(A, left_start, left_end, right_start, right_end):
	# assumes left and right arrays are sorted 
	sizeLeft = (left_end - left_start) + 1 
	sizeRight = (right_end - right_start) + 1 

	# temporary lists initialized explicitly
	tempLeft = [None] * sizeLeft
	tempRight = [None] * sizeRight

	# copy values from A to tempLists 
	for i in range(0, sizeLeft, 1):
		tempLeft[i] = A[left_start + i]

	for j in range(0, sizeRight, 1):
		tempRight[j] = A[right_start + j]

	# maintain current pointers
	currentA = left_start
	currentLeft = 0 
	currentRight = 0

	# Compare temporary lists and copy the minimum values to A 
	while ((currentLeft < sizeLeft) and (currentRight < sizeRight)):
		leftVal = tempLeft[currentLeft]
		rightVal = tempRight[currentRight]

		if leftVal < rightVal:
			A[currentA] = leftVal
			currentLeft += 1 
		else:
			A[currentA] = rightVal
			currentRight += 1 
		currentA += 1 

	# copy remaining values in temp lists to A 
	#  can do this because we assumed left and right lists are sorted 
	# 	only 1 of these next 2 loops should trigger
	while (currentLeft < sizeLeft):
		A[currentA] = tempLeft[currentLeft]
		currentLeft += 1 
		currentA += 1

	while (currentRight < sizeRight):
		A[currentA] = tempRight[currentRight]
		currentRight += 1
		currentA += 1 

	return 

def mergeSort(A, start, end):
	if (start < end):
		middle = (start + end) // 2
		leftStart = start
		leftEnd = middle 
		rightStart = middle + 1 
		rightEnd = end 
		mergeSort(A, leftStart, leftEnd)
		mergeSort(A, rightStart, rightEnd)
		merge(A, leftStart, leftEnd, rightStart, rightEnd)
	return 

def mergeSortWrapper(A):
	mergeSort(A, 0, len(A) - 1)
	return A 
