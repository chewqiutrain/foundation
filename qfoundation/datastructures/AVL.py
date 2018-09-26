class AVLNode(object):
	def __init__(self, key):
		self.key = key
		self.height = 1
		self.left = None
		self.right = None 

	def __repr__(self):
		return 'AVLNode(key = {key}, height = {height})'.format(\
			key = self.key,\
			height = self.height)

class AVLTree(object):
	def __init__(self):
		self.root = None 


	def fixHeight(self, x):
		if x is None:
			return None 
		x.height = max(self.height(x.left), self.height(x.right)) + 1 

	def height(self, x):
		# reached a leaf
		if x is None:
			return 0
		return x.height

	def isBalanced(self, node):
		if node is None:
			return True 

		heightLeft = self.height(node.left)
		heightRight = self.height(node.right)
		return (abs(heightLeft - heightRight) <= 1) and self.isBalanced(node.left) and self.isBalanced(node.right)


	def rotateLeft(self, x):
		y = x.right
		if y is not None:
			x.right = y.left 
			y.left = x 
			return y 
		else:
			return x

	def rotateRight(self, x):
		y = x.left 
		if y is not None:
			x.left = y.right 
			y.right = x 
			return y 
		else:
			return x

	def insertHelper(self, parent, key):
		if parent == None:
			return AVLNode(key)

		elif key < parent.key:
			parent.left = self.insertHelper(parent.left, key)
			self.fixHeight(parent)
			return parent
		
		elif parent.key < key:
			parent.right = self.insertHelper(parent.right, key)
			self.fixHeight(parent)
			return parent

		else:
			raise Exception("we assumed unique keys")

	def insert(self, key):
		self.root = self.insertHelper(self.root, key)


def test():
	testVal1 = [25, 15, 40, 8, 20, 30, 45]
	AVL1 = AVLTree()
	AVL1.insert(25)
	print(AVL1.root)

	print('\n')
	AVL1.insert(15)
	# AVL1.fixHeight(AVL1.root)
	print(AVL1.root)

	print('\n')
	AVL1.insert(40)
	# AVL1.fixHeight(AVL1.root)
	print(AVL1.root)

	print('\n')
	AVL1.insert(8)
	# AVL1.fixHeight(AVL1.root.left)
	# AVL1.fixHeight(AVL1.root)
	print(AVL1.root)
# 	print(AVL1.root.left)
# 	print(AVL1.root.left.left)
# test()

def test2():
	x = AVLTree()
	x.insert(25)

	print(id(x))
	print(id(x.root))
	print(id(x.root.key))

	y = AVLTree()
	y.insert(25)
	print('\n')
	print(id(y))
	print(id(y.root))
	print(id(y.root.key))


	z = y 
	print(id(z))
	y.insert(5)
	print(y.root.left)
	print(id(y.root.left))

	print(z.root.left)
	print(id(z.root.left))
test2()