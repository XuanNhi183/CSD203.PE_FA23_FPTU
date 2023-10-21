class TShirt:
    def __init__(self, sku, style, size, color, price):
        self.sku = sku
        self.style = style
        self.size = size
        self.color = color
        self.price = price

    def __repr__(self):
        return f"{self.sku}, {self.style}, {self.size}, {self.color}, {self.price}"
    
    def set_size(self, x): 
        self.size = x 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class qNode:    
    def __init__(self,data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def enQueue(self, data):
        node = qNode(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def deQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

class BSTree:	
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self, data):
        self.root = BSTree.insertNode(self.root, data)  
    
    def insertNode(node, data):
        if node is None:
            return Node(data)
        if data.sku < node.data.sku:
            node.left = BSTree.insertNode(node.left, data)
        elif data.sku > node.data.sku:
            node.right = BSTree.insertNode(node.right, data)
        return node
    
    def visit(self, p):
        if p==None:
            return
        print(f"{p.data}")
    
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

    # find the maximum depth or height of a tree
    # def maxDepth(self,node):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------   
    
    # perform the Post-Order traverse on the BST, but ONLY 
    # visit nodes that has TShirt's price lager than 3.
    # def postOrder2(self,p):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # def postVisit2(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # compute number of nodes in tree
    # def size(self,node):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        
    # decrease the TShirt's price of all Nodes that have 
    # style = 'LINE' by 1       
    # def updateTShist(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # remove all nodes that are leaves of given BST
    # def deleteLeaf(self,node):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Find the Maximum Depth or Height of given Binary Search Tree (BST). 
            Hint: 
                (1) Implement a 'maxDepth' function to calculate the height of the tree. 
                    Note: The height of an empty tree is 0 and the height of a tree with 
                    single node is 1.
                (2) Recursively calculate the height of the left and the right subtrees 
                    of a node and assign height to the node as max of the heights of two 
                    children plus 1.
            With the data provided, the output after running this function will be:
                OUTPUT:
                3
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # This function is used for Question 2
    def f2(self):
        """
            Question 2: Perform the Post-Order traverse on the BST, but ONLY visit nodes 
            that has TShirt's price lager than 3.
            Hint: 
                (1) You should create 2 new functions 'postVisit2' and 'postOrder2' 
                    with similar content to the two functions "postVisit" and "postOrder" 
                    (available in this file) to perform the Post-Order traverse but only 
                    consider the price greater than 3.
                (2) Call the 'postVisit2' function in the f2() to perform them.
            With the data provided, the output after running these two functions will 
            be:
                OUTPUT:
                0131-1, LINE, M-L-XL, GRAY-BLACK, 5.2
                T03-1, SIMPLE, M-L-XL, NAVY, 3.75
                0192-1, LINE, M-L-XL, WHITE-BLACK, 5.2
        """  
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Insert into the current tree a new TShirt which sku = '0111-1', 
            style = 'BLOKECORE', size = 'M-L-XL', color = 'GRAY-BLACK', price = k, where 
            k is size of the current tree before insertion. 
            Hint:  
                (1) Implement a 'size' function to calculate the size or number of nodes 
                    in tree.
                (2) Insert the new TShirt('0111-1', 'BLOKECORE', 'M-L-XL', 'GRAY-BLACK', 
                    float(Tree_Size)) into the current tree.
            With the data provided, the output after running this function will be:
                OUTPUT:
                0192-1, LINE, M-L-XL, WHITE-BLACK, 5.2
                0131-1, LINE, M-L-XL, GRAY-BLACK, 5.2
                0111-1, BLOKECORE, M-L-XL, GRAY-BLACK, 5.0
                FIR-16-2, FIRE, L, RED, 2.5
                FIR-10-1, FIRE, M-L, DARK-BROW, 2.5
                T03-1, SIMPLE, M-L-XL, NAVY, 3.75             
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.preVisit()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Decrease the TShirt's price of all Nodes that have style = 'LINE' 
            by 1. 
            Hint: 
            This function is similar to the function 'breadth_first' . 
                (1) You should create a new function 'updateTShist' which body is similar 
                    to the function 'breadth_first' (provided in this file already) for 
                    doing BFS but considering only style = 'LINE'.
                (2) Call the 'updateTShist' function in the f4() to perform it (decrease 
                    the TShirt's price of all Nodes that have style = 'LINE' by 1).
            With the data provided, the output after running this function will be:
                OUTPUT:
                0192-1, LINE, M-L-XL, WHITE-BLACK, 4.2
                0131-1, LINE, M-L-XL, GRAY-BLACK, 4.2
                FIR-16-2, FIRE, L, RED, 2.5
                FIR-10-1, FIRE, M-L, DARK-BROW, 2.5
                T03-1, SIMPLE, M-L-XL, NAVY, 3.75
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    # this function is used for Question 5
    def f5(self):
        """
            Question 5: Remove all leaf nodes from the given Binary Search Tree (BST). 
            Hint: 
                (1) Leaf nodes have neither left child nor right child.
                (2) Implement a 'deleteLeaf' function to remove all leaf nodes 
                    from the given BST.
                (3) Call the 'deleteLeaf' function in the f5() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                0192-1, LINE, M-L-XL, WHITE-BLACK, 5.2
                FIR-16-2, FIRE, L, RED, 2.5
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()
        
# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===

def main():
    tree = BSTree()
    tree.insert(TShirt('0192-1', 'LINE', 'M-L-XL', 'WHITE-BLACK', 5.20))
    tree.insert(TShirt('0131-1', 'LINE', 'M-L-XL', 'GRAY-BLACK', 5.20))
    tree.insert(TShirt('FIR-16-2', 'FIRE', 'L', 'RED', 2.50))
    tree.insert(TShirt('FIR-10-1', 'FIRE', 'M-L', 'DARK-BROW', 2.50))
    tree.insert(TShirt('T03-1', 'SIMPLE', 'M-L-XL', 'NAVY', 3.75))
    
    print("Do you want to run Q2?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1: 
        print("OUTPUT:")      
        tree.f1()

    if n ==2:
        print("OUTPUT:")
        tree.f2()

    if n == 3:
        print("OUTPUT:")
        tree.f3()

    if n == 4:
        print("OUTPUT:")
        tree.f4()

    if n == 5:
        print("OUTPUT:")
        tree.f5()       
# end main

# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================