class Car:
    def __init__(self, code, make, owner, price, color):
        self.code = code
        self.make = make
        self.owner = owner
        self.price = price
        self.color = color
    
    def __repr__(self):
        return f"{self.code}, {self.make}, {self.owner}, {self.price}, {self.color}"

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
    
    def addFirst(self, code, make, owner, price, color):
        new_node = Node(Car(code, make, owner, price, color))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    # def addLast(self, code, make, owner, price, color):
		# ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
    def addLast(self, code, make, owner, price, color):
        new_value = Node(Car(code, make, owner, price, color))
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_value

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # def addAfter(self, ref_node, new_node):
		# ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
    def addAfter(self, ref_node, new_node):
        if ref_node is None:
            return
        new_node.next = ref_node.next
        ref_node.next = new_node



        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # def sortByPrice(self):
		# ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
            print()

    def loadData(self):
        self.addFirst('CR005', 'BMW', 'AN DONG', 63.25, 'BLACK')
        self.addFirst('CR004', 'MERCEDES', 'AN HOA', 112.56, 'RED')
        self.addFirst('CR003', 'HONDA CIVIC', 'AN KHANH', 36.99, 'GRAY')
        self.addFirst('CR002', 'BMW', 'AN LAC', 57.09, 'WHITE')
        self.addFirst('CR001', 'HONDA CIVIC', 'AN BINH', 39.69, 'SILVER')

    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Insert after the current list a new Car which code = 'CR006', 
            make = 'MERCEDES', owner = 'AN YEN', price = 115.74, color = 'BRONZE'.
            Hint: 
                (1) Implement an 'addLast' function that inserts a new car into the 
                    current list's tail.
                (2) Call the 'addLast' function in the f1() to perform it and display 
                    the list of all cars as required.
            With the data provided, the output after running this function will be:
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER 
                CR002, BMW, AN LAC, 57.09, WHITE 
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY 
                CR004, MERCEDES, AN HOA, 112.56, RED 
                CR005, BMW, AN DONG, 63.25, BLACK 
                CR006, MERCEDES, AN YEN, 115.74, BRONZE 
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        self.addLast('CR006','MERCEDES','AN YEN','115.74','BRONZE ')
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(Car('CR007', 'BMW', 'AN LANH', 59.35, 'LIQUID BLUE'))
        """
            Question 2: Using the new_node initialized above, write your code to insert 
            the new_node after the third node (which index is 2) of the current list.
            Hint: 
                (1) Use the 'get_node' function given in this file to find the 
                    ref_node (which index is 2).
                (2) Implement an 'addAfter' function with 2 parameters ref_node, 
                    new_node above to insert the new_node after the ref_node.
            With the data provided, the output after running this function will be:
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER
                CR002, BMW, AN LAC, 57.09, WHITE
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY
                CR007, BMW, AN LANH, 59.35, LIQUID BLUE
                CR004, MERCEDES, AN HOA, 112.56, RED
                CR005, BMW, AN DONG, 63.25, BLACK
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        ref_node = self.get_node(2)
        self.addAfter(ref_node,new_node)


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Find the first node in the linked list that has Car's make 
            start with 'B', if such a node is found, then set the color of Car in 
            this node to 'ALPINE WHITE'. 
            Hint: Use str.startswith(start) to find the first node in a linked list 
            whose Car's make begins with 'B'.
            Example: if the linked list before change is  
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER 
                CR002, BMW, AN LAC, 57.09, WHITE 
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY 
                CR004, MERCEDES, AN HOA, 112.56, RED 
                CR005, BMW, AN DONG, 63.25, BLACK 
            then the the linked list after change is:  
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER 
                CR002, BMW, AN LAC, 57.09, ALPINE WHITE 
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY 
                CR004, MERCEDES, AN HOA, 112.56, RED 
                CR005, BMW, AN DONG, 63.25, BLACK 
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------ 
        current = self.head
        while current:      #trong khi cái current chạy
            if current.next.data.make.startswith('B'):   #nếu như chạy tới cái node chứa data bắt đầu là B đầu tiên
                current.next.data.color = 'ALPINE WHITE'    #thì cập nhật data color lại thành ALPINE WHITE
                break    #xong thì dừng lại
            current = current.next   #nếu như không phải thì tiếp tục chuyển đến node tiếp theo
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Sort the linked list in an descending order according to Car's 
            price. 
            Hint: Create a new function 'sortByPrice' to sort the linked list, then call 
            the created function in the f4() to perform it.
            Example: if the linked list before change is  
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER 
                CR002, BMW, AN LAC, 57.09, WHITE 
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY 
                CR004, MERCEDES, AN HOA, 112.56, RED 
                CR005, BMW, AN DONG, 63.25, BLACK 
            then the the linked list after change is:  
                OUTPUT:
                CR004, MERCEDES, AN HOA, 112.56, RED 
                CR005, BMW, AN DONG, 63.25, BLACK 
                CR002, BMW, AN LAC, 57.09, WHITE 
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER 
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY                             
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        current = self.head
        while current:
            if current.data.price > current.next.data.price:
                current = current.next
                break
            current = current.next
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5


    def f5(self):
        """
            Question 5: Delete the first node in the linked list with Car's make = 'BMW'.
            Example: if the linked list before change is
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER 
                CR002, BMW, AN LAC, 57.09, WHITE 
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY 
                CR004, MERCEDES, AN HOA, 112.56, RED 
                CR005, BMW, AN DONG, 63.25, BLACK 
            then the the linked list after change is:  
                OUTPUT:
                CR001, HONDA CIVIC, AN BINH, 39.69, SILVER
                CR003, HONDA CIVIC, AN KHANH, 36.99, GRAY
                CR004, MERCEDES, AN HOA, 112.56, RED
                CR005, BMW, AN DONG, 63.25, BLACK                         
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        current = self.head
        while current:
            if current.next.data.make.startswith('B'):
                current.next = current.next.next
                break
            current = current.next

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===

def main():
    lst = LinkedList()
    lst.loadData()
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        lst.f1()

    if n ==2:
        print("OUTPUT:")
        lst.f2()

    if n == 3:
        print("OUTPUT:")
        lst.f3()

    if n == 4:
        print("OUTPUT:")
        lst.f4()

    if n == 5:
        print("OUTPUT:")
        lst.f5()

# End main

# --------------------------------

if __name__ == "__main__":
    main()
    
# ============================================================