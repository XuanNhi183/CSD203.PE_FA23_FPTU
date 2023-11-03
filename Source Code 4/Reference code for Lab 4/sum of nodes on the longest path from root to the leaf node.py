# Python3 implementation to find the 
# Sum of nodes on the longest path
# from root to leaf nodes
 
# function to get a new node
class getNode:
    def __init__(self, data):
 
        # put in the data
        self.data = data
        self.left = self.right = None
 
# function to find the Sum of nodes on the
# longest path from root to leaf node
def SumOfLongRootToLeafPath(root, Sum, Len,
                            maxLen, maxSum):
                                 
    # if true, then we have traversed a
    # root to leaf path
    if (not root):
         
        # update maximum Length and maximum Sum
        # according to the given conditions
        if (maxLen[0] < Len):
            maxLen[0] = Len
            maxSum[0] = Sum
        elif (maxLen[0]== Len and
              maxSum[0] < Sum):
            maxSum[0] = Sum
        return
 
    # recur for left subtree
    SumOfLongRootToLeafPath(root.left, Sum + root.data,
                            Len + 1, maxLen, maxSum)
 
    # recur for right subtree
    SumOfLongRootToLeafPath(root.right, Sum + root.data,
                            Len + 1, maxLen, maxSum)
 
# utility function to find the Sum of nodes on
# the longest path from root to leaf node
def SumOfLongRootToLeafPathUtil(root):
     
    # if tree is NULL, then Sum is 0
    if (not root):
        return 0
 
    maxSum = [-999999999999]
    maxLen = [0]
 
    # finding the maximum Sum 'maxSum' for
    # the maximum Length root to leaf path
    SumOfLongRootToLeafPath(root, 0, 0,
                            maxLen, maxSum)
 
    # required maximum Sum
    return maxSum[0]
 
# Driver Code
if __name__ == '__main__':
     
    # binary tree formation
    root = getNode(4)         #     4    
    root.left = getNode(2)         #     / \    
    root.right = getNode(5)     #     2 5    
    root.left.left = getNode(7) #     / \ / \    
    root.left.right = getNode(1) # 7 1 2 3
    root.right.left = getNode(2) #     /        
    root.right.right = getNode(3) #     6        
    root.left.right.left = getNode(6)
 
    print("Sum = ", SumOfLongRootToLeafPathUtil(root))