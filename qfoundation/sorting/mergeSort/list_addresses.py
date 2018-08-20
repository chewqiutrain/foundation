arrA = [1,2,3]

def foo(A):
	A[0] = 3
	return A

print(arrA)
B = foo(arrA)
print(arrA)
print(B)
print(id(B))
print(id(arrA))
# id(B) = id(arrA)