# need this class to have .visited attribute; used in cycle detection
class GraphNode(object):
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.adjacents = list()

	def __repr__(self):
		template = "GraphNode({key}, {visited})"
		return template.format(key = self.key, visited = self.visited)


class BaseGraphArb(object):
	def __init__(self, V):
		self.nodes = [GraphNode(i) for i in range(0, V)]
		self.V = V 
		self.E = 0

	def __repr__(self):
		template = "No. vertices, V = {V}; No. edges, E = {E} ".format(V = self.V,\
			E = self.E)
		nodeTemplate = "Node: {nodeI}, Adjacents: {adjacentsI}"
		for nodeI, adjI in enumerate(self.nodes):
			strI = nodeTemplate.format(nodeI = nodeI, adjacentsI = str(adjI.adjacents))
			template = template + '\n' + strI
		return template

	# get all nodes adjacent to v
	# 0 < v < len(self.nodes)
	def adj(self, v): 
		assert(0 <= v), "v not within bounds, can't be negative"
		assert(v < len(self.nodes)), "v not within bounds, can't be greater than len(self.nodes)"
		return self.nodes[v].adjacents

	def addEdge(self, v, w, weight):
		pass 

	def buildGraphFromEdgeList(self, edges):
		pass


class DigraphArb(BaseGraphArb):
	def addEdge(self, v, w):
		if (v < 0) or (w < 0): 
			raise Exception('v, w must be >= 0')

		if (v > self.V) or (w > self.V):
			raise Exception('v, w must be < len(V)')

		vNode = self.nodes[v]
		# vNode.adjacents.append(w) #record w as an outgoing edge from v
		self.nodes[v].adjacents.append(w)
		self.E += 1 
		return 

	def buildGraphFromEdgeList(self, edges):
		for edgeI in edges:
				self.addEdge(edgeI[0], edgeI[1])


def digraph1():
	V = 13 
	E = 21 
	edges = [(0,5), (0,1), (2,0), (2,3), (3,2), (3,5), (4,2), (4,3),\
		(5,4), (6,0), (6,4), (6,8), (6,9), (7,6), (7,9), (8,6), (9,10), \
		(9,11), (10,12), (11,12), (12,9)]

	dGraph1 = DigraphArb(V)
	dGraph1.buildGraphFromEdgeList(edges)
	assert(dGraph1.E == E)
	assert(dGraph1.V == V)
	return dGraph1

def test():
	d = digraph1()
	print(d)

test()