import math

def getPermutations(setA):
	if len(setA) <= 1:
		return [[list(setA)[0]]]
	else:
		result = list()
		for elem in setA:
			x = [elem]
			difference = setA - set(elem)
			allPerms = getPermutations(difference)
			for permI in allPerms:
				result.append(x + permI)
			
		return result 


def testTemplate(testList):
	A0 = set(testList)
	R0 = getPermutations(A0)
	print(R0)
	setLength = len(A0)
	expectedPermsLength = math.factorial(len(A0))
	actualPermsLength = len(R0)
	assert(actualPermsLength == expectedPermsLength),\
		"length should be {expected}; actual = {actual}".format(\
			expected = expectedPermsLength, actual = actualPermsLength)


def test0():
	testTemplate(['A', 'B'])

def test1():
	testTemplate(['A', 'B', 'C'])

def test2():
	testTemplate(['A', 'B', 'C', 'D'])


def test():
	test0()
	print('\n')
	test1()
	print('\n')
	test2()

test()

