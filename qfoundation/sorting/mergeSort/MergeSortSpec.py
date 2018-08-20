from MergeSort import mergeSortWrapper

def mergeSortSpec1():
	print('Empty list')
	A0 = list()
	A0_result = mergeSortWrapper(A0)
	assert(not bool(A0_result)), "Empty list should return empty list"

	print('\n')
	print('A1 = [5,2,4,6,1,3]')
	A1 = [5,2,4,6,1,3]
	A1_result = mergeSortWrapper(A1)
	A1_expected = [1,2,3,4,5,6]
	assert(A1_result == A1_expected), "A1"

	print('\n')
	print('A2 = [2,1]')
	A2 = [2,1]
	A2_result = mergeSortWrapper(A2)
	A2_expected = [1,2]
	assert(A2_result == A2_expected), "A2"	

	print('\n')
	print('A3 = [0,1,2,3,4,5,6,7]')
	A3 = [0,1,2,3,4,5,6,7]
	A3_result = mergeSortWrapper(A3)
	A3_expected = [0,1,2,3,4,5,6,7]
	assert(A3_result == A3_expected), "A3"	

	print('\n')
	print('A4 = [2]')
	A4 = [2]
	A4_result = mergeSortWrapper(A4)
	A4_expected = [2]
	assert(A4_result == A4_expected), "A3"		

mergeSortSpec1()