import queue

class BSTNode(object):
	def __init__(self, key):
		self.key = key 
		self.left = None
		self.right = None

	def __repr__(self):
		return 'BSTNode({key})'.format(key = self.key)

class BST(object):
	def __init__(self):
		self.root = None 

	def insertHelper(self, parent, key):
		if parent == None:
			return BSTNode(key)

		elif key < parent.key:
			parent.left = self.insertHelper(parent.left, key)
			return parent
		
		elif parent.key < key:
			parent.right = self.insertHelper(parent.right, key)
			return parent

		else:
			raise Exception("we assumed unique keys")

	def insert(self, key):
		self.root = self.insertHelper(self.root, key)

	def traversePreOrderHelper(self, node):
		if node is not None:
			print(node.key)
			self.traversePreOrderHelper(node.left)
			self.traversePreOrderHelper(node.right)

	def traversePreOrder(self):
		self.traversePreOrderHelper(self.root)

	def traverseInOrderHelper(self, node):
		if node is not None:
			self.traverseInOrderHelper(node.left)
			print(node.key)
			self.traverseInOrderHelper(node.right)

	def traverseInOrder(self):
		self.traverseInOrderHelper(self.root)

	def traversePostOrderHelper(self, node):
		if node is not None:
			self.traversePostOrderHelper(node.left)
			self.traversePostOrderHelper(node.right)
			print(node.key)

	def traversePostOrder(self):
		self.traversePostOrderHelper(self.root)
		
	def traverseLevelOrder(self):
		storageQueue = queue.Queue()
		storageQueue.put(self.root)
		while not storageQueue.empty():
			nextNode = storageQueue.get()
			print(nextNode.key)
			if nextNode.left is not None:
				storageQueue.put(nextNode.left)

			if nextNode.right is not None:
				storageQueue.put(nextNode.right)
	
		




def spec():
	testVal1 = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
	BST1 = BST()
	for keyI in testVal1:
		BST1.insert(keyI)
	
	print('traverse pre-order')
	BST1.traversePreOrder()
	
	print('\ntraverse in-order')
	BST1.traverseInOrder()

	print('\ntraverse post-order')
	BST1.traversePostOrder()

	print('\ntraverse level-order')
	BST1.traverseLevelOrder()

def test():
	spec()
		

test()