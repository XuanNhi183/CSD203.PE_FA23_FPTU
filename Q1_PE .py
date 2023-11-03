class Std:
    def __init__(self, name, ID, GPA):
        self.name = name
        self.ID = ID
        self.GPA = GPA

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.size = 0

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def addLast(self, name, ID, GPA):
        n = Std(name, ID, GPA)
        new_node = Node(n)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addToHead(self,name, ID, GPA):
        n = Std(name, ID, GPA)
        new_Value = Node(n)
        if self.head is None:
            self.head = new_Value
            self.size += 1
        else:
            new_Value.next = self.head
            self.head = new_Value
            self.size += 1



    def count(self):
        return self.size
    def loadData(self):
        self.addLast("A", "1701", 8)
        self.addLast("B", "1702", 7)
        self.addLast("C", "1706", 9)
        self.addLast("D", "1801", 10)
        self.addLast("E", "1803", 8)

    def avg(self):
        sum =0
        count = 0
        p = self.head
        if p is None:
            return None
        else:
            while p:
                count = count + 1
                sum = sum + p.data.GPA
                avg = sum / count
                p = p.next
        return avg

    def f1(self):
    # === BEGIN YOUR CODE HERE
        gpa_student = self.avg()
        return gpa_student
    #=== END YOUR CODE

    def f2(self,name, ID, GPA):
        # =========================================
        # === BEGIN YOUR CODE HERE
        self.addToHead(name,ID,GPA)
        gpa_students = self.avg()
        return gpa_students
        # === END YOUR CODE
    def delete_3First(self):
        n = 0
        while n <=  3:
            if self.head is None:
                return None
            else:
                current = self.head
                self.head = current.next
                current = None
                n = n+1
    def f3(self):
        # =========================================
        # === BEGIN YOUR CODE HERE
        self.delete_3First()
        gpa_students = self.avg()
        return gpa_students
        # === END YOUR CODE

    def f4(self):
        current = self.head
        count = 0
        while current:
            if current.data.GPA >= 9:
                count = count + 1
            current = current.next
        return count
        # === BEGIN YOUR CODE HERE
        # === END YOUR CODE
#nếu tra thấy id 1702 -> điểm GPA đc cộng thêm 0.5

    def f5(self):
        #=== BEGIN YOUR CODE HERE
        current = self.head
        while current:
            if current.data.ID == "1702":
                current.data.GPA += 0.5
                return current.data.GPA
            current = current.next


        # === END YOUR CODE


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
        result = lst.f1()
        print("OUTPUT:")
        print(result)

    if n == 2:
        lst.f2("F", "1807", 7)
        lst.f2("G", "1808", 9)
        result = lst.f2("H", "1809", 6)
        print("OUTPUT:")
        print(result)

    if n == 3:
        result = lst.f3()
        print("OUTPUT:")
        print(result)

    if n == 4:
        result = lst.f4()
        print("OUTPUT:")
        print(result)

    if n == 5:
        result = lst.f5()
        print("OUTPUT:")
        print(result)

# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================
