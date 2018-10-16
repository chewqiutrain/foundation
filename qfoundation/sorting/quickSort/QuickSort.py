def swap(arr, i, j):
	'''
	swap arr[i] with arr[j]
	'''
	holdI = arr[i]
	holdJ = arr[j]
	arr[i] = holdJ
	arr[j] = holdI

def partition(arr, low, high):
	pivotVal = arr[high]
	i = low 
	j = low 
	while (j <= (high - 1)):
		if arr[j] < pivotVal:
			swap(arr, i, j)
			i += 1 
		j += 1

	swap(arr, i, j)
	return i 

def quickSort(arr, low, high, index):
	if low < 0: return
	if high > len(arr): return
	# print("quickSort.low = " + str(low))
	# print("quickSort.high = " + str(high))

	# print("index = " + str(index))

	if low < high:
		pivottedIndex = partition(arr, low, high)
		# print("pivottedIndex = " + str(pivottedIndex) + '\n')

		quickSort(arr, low, pivottedIndex - 1, index + 1)
		quickSort(arr, pivottedIndex + 1, high, index + 1)

def quickSortWrapper(A):
	quickSort(A, 0, len(A) - 1, 0)
	return A 


# def test():
# 	print('\n')
# 	print('A1 = [5,2,4,6,1,3]')
# 	A1 = [5,2,4,6,1,3]
# 	p1 = partition(A1, 0, 5)
# 	print(A1)
# 	print("pivottedIndex 1 =" + str(p1))
# 	print('\np2')

# 	p2 = partition(A1,0, 2)
# 	print(A1)
# 	print("pivottedIndex 2 =" + str(p2))

# 	p2a = partition(A1,0, 2)
# 	print(A1)
# 	print("pivottedIndex 2a =" + str(p2a))

# 	print('\np3')
# 	p3 = partition(A1,3, 5)
# 	print(A1)
# 	print("pivottedIndex 3 =" + str(p3))

# 	print('\n\n')
# 	A10 = [5,2,4,6,1,3]
# 	A1_result = quickSortWrapper(A10)
# 	A1_expected = [1,2,3,4,5,6]
# 	print(A1_result)
# 	assert(A1_result == A1_expected), "A1"

# # test()