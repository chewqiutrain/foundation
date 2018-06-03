# TODO: Add type check? 

class SLLNode(object):
	'''
	Represents a node in a Singly Linked List
	'''
	def __init__(self, val = None):
		# :param val: value stored in this node
		# :param next: pointer to the next node
		self.val = val
		self.next = None

	def isEnd(self):
		return self.next == None

	def printself(self):
		if self.val == None:
			return
		else:
			print(self.val)

class SinglyLinkedList(object):
	'''
	Chain of SLLNodes
	'''
	def __init__(self):
		# :param headval: pointer to the first node in the list 
		self.headval = None

	def printsl(self):
		currNode = self.headval
		while currNode != None:
			currNode.printself()
			currNode = currNode.next

	def length(self):
		count = 0
		currNode = self.headval
		while currNode != None:
			count += 1
			currNode = currNode.next
		return count

	def insertAtTail(self, new_val):
		# :param new_val: value to insert
		currNode = self.headval

		if currNode == None:
			self.insertAtHead(new_val)
			return 

		while not currNode.isEnd():
			currNode = currNode.next 
		currNode.next = SLLNode(new_val)
		return 

	def insertAtHead(self, new_val):
		# :param new_val: value to insert
		newNode = SLLNode(new_val)
		newNode.next = self.headval
		self.headval = newNode
		return

	def insertAtIndex(self, index, new_val):
		# :param index: index to insert to
		# :param new_val: value to insert
		# index out of bounds, just return
		if (index >= self.length()) or (index < 0): 
			return
		elif index == 0: 
			self.insertAtHead(new_val)
		elif index == (self.length() - 1): 
			self.insertAtTail(new_val)
		else:
			# traverse list
			currNode = self.headval
			count = 0 
			while count < (index - 1):
				currNode = currNode.next 
				count += 1

			tailNodes = currNode.next
			newNode = SLLNode(new_val)
			newNode.next = tailNodes
			currNode.next = newNode

	def removeTail(self):
		currNode = self.headval
		if currNode == None:
			return 

		while not currNode.isEnd():
			prevNode = currNode
			currNode = currNode.next 

		prevNode.next = None 

	def removeHead(self):
		if self.headval == None:
			return 
		tailNodes = self.headval.next 
		self.headval = tailNodes

	def removeAtIndex(self, index):
		# :param index: index to insert to
		# index out of bounds, just return
		if (index >= self.length()) or (index < 0): 
			return
		elif index == 0: 
			self.removeHead()
		elif index == (self.length() - 1): 
			self.removeTail()
		else:
			prevNode = self.headval
			currNode = self.headval
			count = 0 
			while count < (index - 1):
				prevNode = currNode
				currNode = currNode.next 
				count += 1 

			prev.next = curr.next

	def fromPythonList(self, input_list):
		# :param input_list: list of elements of the same type
		# :returns: SingleLinkedList Object built from input_list elements
		if input_list == None:
			return None 

		for inputI in input_list:
			self.insertAtTail(inputI)
		return 
