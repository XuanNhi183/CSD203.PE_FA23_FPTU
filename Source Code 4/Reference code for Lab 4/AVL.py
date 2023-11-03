# A class to store a binary tree node
class Node:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right


# Recursive function to check if a given binary tree is height-balanced or not
def isHeightBalanced(root, isBalanced=True):

	# base case: tree is empty or not balanced
	if root is None or not isBalanced:
		return 0, isBalanced

	# get the height of the left subtree
	left_height, isBalanced = isHeightBalanced(root.left, isBalanced)

	# get the height of the right subtree
	right_height, isBalanced = isHeightBalanced(root.right, isBalanced)

	# tree is unbalanced if the absolute difference between the height of
	# its left and right subtree is more than 1
	if abs(left_height - right_height) > 1:
		isBalanced = False

	# return height of subtree rooted at the current node
	return max(left_height, right_height) + 1, isBalanced


if __name__ == '__main__':

	''' Construct the following tree
			  1
			/   \
		   /     \
		  2       3
		 / \     /
		4   5   6
	'''

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)

	if isHeightBalanced(root)[1]:
		print('Binary tree is balanced')
	else:
		print('Binary tree is not balanced')
