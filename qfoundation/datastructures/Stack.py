class Node(object):
	def __init__(self, data):
		self.data = data
		self.prev = None 

class Stack(object):
	def __init__(self, head):
		self.head = head  # head is a node

	def isEmpty(self):
		return self.head == None 

	def pop(self):
		if not self.isEmpty():
			self.head = self.head.prev

	def push(self, newNode):
		if self.isEmpty():
			self.head = newNode
		else:
			newNode.prev = self.head
			self.head = newNode

	def peek(self):
		return self.head.data 