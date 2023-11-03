from node import *
from myqueue import *

class BSTree:	
	def __init__(self):
		self.root = None
   
	def clear(self):
		self.root = None
        
	def isEmpty(self):
		return self.root == None

	def insert(self, key):
		self.root = BSTree.insertNode(self.root, key)
	
	def insertNode(node, key):
        # if the tree is empty, return a new node
		if node is None:
			return Node(key)
        # otherwise, recur down the tree
		if key < node.key:
			node.left = BSTree.insertNode(node.left, key)
		elif key > node.key:
			node.right = BSTree.insertNode(node.right, key)
		# return the node pointer
		return node

	# function that returns the node with minimum key value 
	# found in that tree
	def minValueNode(node):
		current = node
		# Loop down to find the leftmost leaf
		while current and current.left is not None:
			current = current.left
		return current
	
	def delete(self, key):
		self.root = BSTree.deleteNode(self.root, key)
	
	def deleteNode(root, key):
		# base Case
		if root is None:
			return root
		# if the key to be deleted is smaller than the root's key, 
		# then it lies in left subtree
		if key < root.key:
			root.left = BSTree.deleteNode(root.left, key)
		# if the key to be deleted is greater than the root's key, 
		# then it lies in right subtree
		elif key > root.key:
			root.right = BSTree.deleteNode(root.right, key)
		# if key is same as root's key, then this is the node to be deleted
		else:
		# node with only one child or no child
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp
			# node with two children: get the inorder successor (smallest
			# in the right subtree)
			temp = BSTree.minValueNode(root.right)
			# copy the inorder successor's content to this node
			root.key = temp.key
			# delete the inorder successor
			root.right = BSTree.deleteNode(root.right, temp.key)
		return root
	
	def visit(self, p):
		if p==None:
			return
		print(f"{p.key}",end =" ")
	
	def preOrder(self, p):
		if p==None:
			return
		self.visit(p)
		self.preOrder(p.left)
		self.preOrder(p.right)
	
	def preVisit(self):
		self.preOrder(self.root)
		print()
	
	def inOrder(self, p):
		if p==None:
			return
		self.inOrder(p.left)
		self.visit(p)
		self.inOrder(p.right)
	
	def inVisit(self):
		self.inOrder(self.root)
		print()      

	def postOrder(self,p):
		if p==None:
			return
		self.postOrder(p.left)
		self.postOrder(p.right)
		self.visit(p)
	
	def postVisit(self):
		self.postOrder(self.root)
		print()
	
	def breadth_first(self):
		if self.isEmpty():
			return
		mq = MyQueue()
		mq.enQueue(self.root)
		while not mq.isEmpty():
			p = mq.deQueue()
			self.visit(p)
			if p.left!=None:
				mq.enQueue(p.left)
			if p.right!=None:
				mq.enQueue(p.right)