class TreeNode:
   def __init__(self, value):
      self.val = value
      self.left = None
      self.right = None
   def number_of_nodes(self, root):
      if root is None:
         return 0
      else:
         return (1 + self.number_of_nodes(root.left) + self.number_of_nodes(root.right))
   def has_heap_property(self, root):
      if (root.left is None and root.right is None):
         return True
      if root.right is None:
         return root.val >= root.left.val
      else:
         if (root.val >= root.left.val and
            root.val >= root.right.val):
            return (self.has_heap_property(root.left) and self.has_heap_property(root.right))
         else:
            return False
   def is_complete_tree(self, root,index, node_count):
      if root is None:
         return True
      if index >= node_count:
         return False
      return (self.is_complete_tree(root.left, 2 * index + 1, node_count) and self.is_complete_tree(root.right, 2 * index + 2, node_count))
   def is_heap(self):
      node_count = self.number_of_nodes(self)
      if (self.is_complete_tree(self, 0, node_count) and self.has_heap_property(self)):
         return True
      else:
         return False
root = TreeNode(99)
root.left = TreeNode(46)
root.right = TreeNode(39)
root.left.left = TreeNode(14)
root.left.right = TreeNode(5)
root.right.left = TreeNode(9)
root.right.right = TreeNode(33)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(12)
print(root.is_heap())