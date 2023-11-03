from bstree import *
    
"""
	Let us create following BST
		50
	   /  \
	 30	   70
	 / \   / \
	20 40 60 80

"""

tree = BSTree()

tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print()
print('Pre-Order Traverse: ', end="")
tree.preVisit()
print('In-Order Traverse: ', end="")
tree.inVisit()
print('Post-Order Traverse: ', end="")
tree.postVisit()
print('Breadth-First Traverse: ', end="")
tree.breadth_first(); print()
print()

do = input('   - Delete: ').split() 
tree.delete(int(do[0]))

print()
print('Pre-Order Traverse: ', end="")
tree.preVisit()
print('In-Order Traverse: ', end="")
tree.inVisit()
print('Post-Order Traverse: ', end="")
tree.postVisit()
print('Breadth-First Traverse: ', end="")
tree.breadth_first()
print()