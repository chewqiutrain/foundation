from WeightedGraphs import EdgeWeightedGraph 

def singleNode():
	V = 1 
	E = 0
	edges = []
	g = EdgeWeightedGraph(V)
	g.buildGraphFromEdgeList(edges)
	assert(g.E == E)
	assert(g.V == V)
	return g


def sampleEdgeWeighted1():
	'''https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/'''
	V = 9
	E = 14 
	edges = [(0,1,4), (0,7,8), (1,7,11), (1,2,8), (2,8,2), (2,3,7), \
		(2,5,4), (3,5,4), (3,4,9), (4,5,10), (5,6,2), (6,8,6), (6,7,1),\
		(7,8,7)]

	g = EdgeWeightedGraph(V)
	g.buildGraphFromEdgeList(edges)
	assert(g.E == E)
	assert(g.V == V)
	return g


def test():
	g0 = singleNode()
	print(g0)

	print('\n')
	g1 = sampleEdgeWeighted1()
	print(g1)

test()