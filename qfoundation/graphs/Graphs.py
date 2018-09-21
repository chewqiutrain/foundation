class BaseGraph(object):
	def __init__(self, V):
		self.nodes = [None] * V 
		self.V = V 
		self.E = 0

	def __repr__(self):
		template = "No. vertices, V = {V}; No. edges, E = {E} ".format(V = self.V,\
			E = self.E)
		nodeTemplate = "Node: {nodeI}, Adjacents: {adjacentsI}"
		for nodeI, adjI in enumerate(self.nodes):
			strI = nodeTemplate.format(nodeI = nodeI, adjacentsI = str(adjI))
			template = template + '\n' + strI
		return template

	# get all nodes adjacent to v
	# 0 < v < len(self.nodes)
	def adj(self, v): 
		assert(0 <= v), "v not within bounds, can't be negative"
		assert(v < len(self.nodes)), "v not within bounds, can't be greater than len(self.nodes)"
		return self.nodes[v]

	def addEdge(self, v, w, weight):
		pass 

	def buildGraphFromEdgeList(self, edges):
		pass


# undirected graph without weights
class Graph(BaseGraph):
	# add edge v-w to graph
	# assume we only use this once, at initialization of graph
	# 	i.e. don't allow graph to be changed dynamically
	def addEdge(self, v, w): 
		if (v < 0) or (w < 0): 
			raise Exception('v, w must be >= 0')

		vExists = self.nodes[v] is not None 
		wExists = self.nodes[w] is not None 

		if vExists:
			vNode = self.nodes[v]
			vNode.append(w)
		else:
			self.nodes[v] = [w]

		if wExists:
			wNode = self.nodes[w]
			wNode.append(v)
		else:
			self.nodes[w] = [v]

		self.E += 1 
		return 

	def buildGraphFromEdgeList(self, edges):
		for edgeI in edges:
				self.addEdge(edgeI[0], edgeI[1])
	

#Directed graph without weights
class Digraph(BaseGraph):
	# add edge v->w to graph
	# assume we only use this once, at initialization of graph
	# 	i.e. don't allow graph to be changed dynamically
	def addEdge(self, v, w): 
		if (v < 0) or (w < 0): 
			raise Exception('v, w must be >= 0')

		vExists = self.nodes[v] is not None 

		if vExists:
			vNode = self.nodes[v]
			vNode.append(w)
		else:
			self.nodes[v] = [w]

		self.E += 1 
		return 

	def buildGraphFromEdgeList(self, edges):
		for edgeI in edges:
				self.addEdge(edgeI[0], edgeI[1])
	

def main():
	edges1 = [(0, 6), (0, 5), (0, 1), (0, 2), (3, 5), (3, 4), (4, 5), (4, 6)]
	V1 = 7
	E1 = 8
	g1 = Graph(V1)
	
	for edgeI in edges1:
		g1.addEdge(edgeI[0], edgeI[1])


	print(g1.E)
	print(g1)
	x = g1.adj(0)
	print(x)

	# TODO: add supp for node without edges
# main()

