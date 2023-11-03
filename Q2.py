class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.height = 0




class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, new_number):
        if not self.root:
            self.root = Node(new_number)
        else:
            self._insert_recursively(self.root, new_number)

    def _insert_recursively(self, current_node, new_number):
        if new_number == current_node.key:
            return
        if new_number < current_node.key:
            if current_node.left is None:
                current_node.left = Node(new_number)
            else:
                self._insert_recursively(current_node.left, new_number)
        else:
            if current_node.right is None:
                current_node.right = Node(new_number)
            else:
                self._insert_recursively(current_node.right, new_number)



    def search(self,p, key):
        if key < p.element:
            if p.left:
                return self.search(p.left, key)
            else:
                return False
        elif key > p.element:
            if p.right:
                return self.search(p.right, key)
            else:
                return False

        elif key == p.element:
            return True
        else:
            return False


    def f1(self):
    # =========================================
        # === BEGIN YOUR CODE HERE


        # === END YOUR CODE

    def f2(self):
    # =========================================
        # === BEGIN YOUR CODE HERE


        # === END YOUR CODE

    #def f3(self):
    # =========================================
        # === BEGIN YOUR CODE HERE


        # === END YOUR CODE

    #def f4(self):
    # =========================================
        # === BEGIN YOUR CODE HERE


        # === END YOUR CODE

    #def f5(self, k):
    # =========================================
        # === BEGIN YOUR CODE HERE


        # === END YOUR CODE

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    t = BSTree()
    t.insert(5)
    t.insert(3)
    t.insert(10)
    t.insert(20)
    t.insert(14)
    t.insert(7)
    t.insert(2)
    t.insert(40)
    t.insert(6)
    t.insert(8)
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        result = t.f1(10)
        print("OUTPUT:")
        print(str(result))

    if n == 2:
        result = t.f2()
        print("OUTPUT:")
        print(result)

    if n == 3:
        result = t.f3()
        print("OUTPUT:")
        print(result)

    if n == 4:
        result = t.f4()
        print("OUTPUT:")
        print(result)

    if n == 5:
        result = t.f5(100)
        print("OUTPUT:")
        print(result)


# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================
