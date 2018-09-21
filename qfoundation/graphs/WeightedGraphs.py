from Graphs import BaseGraph

class WeightedEdge(object):
	def __init__(self, v, w, weight):
		assert(v >= 0), "v must be non-negative integer"
		assert(w >= 0), "w must be non-negative integer"
		assert(weight is not None), "weight cannot be None"
		self.v = v 
		self.w = w 
		self.weight = weight

	def __repr__(self):
		template = "WeightedEdge({v}-{w}; weight = {weight})"
		return template.format(v = self.v, w = self.w, weight = self.weight)

	# tail vertex of the directed edge
	def _from(self): 
		return self.v

	# head vertex of the directed edge
	def _to(self):
		return self.w


def DirectedWeightedEdge(object):
	def __init__(self, v, w, weight):
		assert(v >= 0), "v must be non-negative integer"
		assert(w >= 0), "w must be non-negative integer"
		assert(weight is not None), "weight cannot be None"
		self.v = v 
		self.w = w 
		self.weight = weight

	def __repr__(self):
		template = "DirectedWeightedEdge({v}->{w}; weight = {weight})"
		return template.format(v = self.v, w = self.w, weight = self.weight)

	# tail vertex of the directed edge
	def _from(self): 
		return self.v

	# head vertex of the directed edge
	def _to(self):
		return self.w


class EdgeWeightedDigraph(BaseGraph):
	# add edge v->w to graph
	# assume we only use this once, at initialization of graph
	# 	i.e. don't allow graph to be changed dynamically
	def addEdge(self, v, w, weight): 
		vExists = self.nodes[v] is not None 

		newDirectedEdge = DirectedWeightedEdge(v, w, weight)
		if vExists:
			vNode = self.nodes[v]
			vNode.append(newDirectedEdge)
		else:
			self.nodes[v] = [newDirectedEdge]

		self.E += 1 
		return 

	def buildGraphFromEdgeList(self, edges):
		for edgeI in edges:
				self.addEdge(edgeI[0], edgeI[1], edgeI[2])


class EdgeWeightedGraph(BaseGraph):
	# add edge v-w to graph,
	# assume we only use this once, at initialization of graph
	# 	i.e. don't allow graph to be changed dynamically
	def addEdge(self, v, w, weight): 
		vExists = self.nodes[v] is not None 
		wExists = self.nodes[w] is not None 

		newDirectedEdgeForward = WeightedEdge(v, w, weight)
		newDirectedEdgeBackward = WeightedEdge(w, v, weight)

		if vExists:
			vNode = self.nodes[v]
			vNode.append(newDirectedEdgeForward)
		else:
			self.nodes[v] = [newDirectedEdgeForward]

		if wExists:
			wNode = self.nodes[w]
			wNode.append(newDirectedEdgeBackward)
		else:
			self.nodes[w] = [newDirectedEdgeBackward]

		self.E += 1 
		return 

	def buildGraphFromEdgeList(self, edges):
		for edgeI in edges:
				self.addEdge(edgeI[0], edgeI[1], edgeI[2])


