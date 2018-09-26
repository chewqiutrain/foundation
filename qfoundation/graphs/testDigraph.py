from Graphs import Digraph

def digraph1():
	V = 13 
	E = 21 
	edges = [(0,5), (0,1), (2,0), (2,3), (3,2), (3,5), (4,2), (4,3),\
		(5,4), (6,0), (6,4), (6,8), (6,9), (7,6), (7,9), (8,6), (9,10), \
		(9,11), (10,12), (11,12), (12,9)]

	dGraph1 = Digraph(V)
	dGraph1.buildGraphFromEdgeList(edges)
	assert(dGraph1.E == E)
	assert(dGraph1.V == V)
	return dGraph1

def DAG1():
	V = 7
	E = 10
	edges = [(0,1), (0,2), (1,2), (1,3), (1,5), (2,3), (3,4), (4,5), \
		(4,6), (5,6)]

	dag1 = Digraph(V)
	dag1.buildGraphFromEdgeList(edges)
	assert(dag1.E == E)
	assert(dag1.V == V)
	return dag1

def test():
	dGraph1 = digraph1()
	print(dGraph1)

	print('\n')
	dag1 = DAG1()
	print(dag1)

# test()

def ctci4_1():
	def search(s, t):
		if s.visited:
			return False 

		if s is None:
			return False 

		if s == t:
			return True 

		result = False 
		for neighbour in G.adj(s):
			result = result or search(neighbour, t)

	G = digraph1()
	assert(search(0,2)), "Error: path from 0 to 2 does not exist"
	assert(not search(0, 7)), "Error: Path from 0 to 7 should NOT exist"


ctci4_1()


