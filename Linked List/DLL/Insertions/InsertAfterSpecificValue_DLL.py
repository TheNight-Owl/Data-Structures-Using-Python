from NodeStructureDoublyLinkedList import Node
class InsertAtEnd:
    def __init__(self):
        self.head = None
        self.temp = None

    def insert_at_end(self, value):
        if self.head == None:
            self.head = Node(value)
            self.temp = self.head
        else:
            loc = self.temp
            self.temp.next = Node(value)
            self.temp = self.temp.next
            self.temp.prev = loc

    def insert_after_specific_value(self, element, value):
        k = 0
        if self.head == None:
            k = 0
        else:
            t = self.head
            while t != None:
                if t.data == element:
                    k = 1
                    break
                t = t.next
        if k == 0:
            print("Sorry the given value not found. Element cannot be inserted")
        else:
            loc = Node(value)
            loc.next = t.next
            loc.prev = t
            if t.next != None:          #If the value is being inserted at end the following step at line 35 should be avoided
                loc.next.prev = loc
            else:
                self.temp = loc
            t.next = loc
            print("Element inserted successfully")

    def display_left_to_right(self):
        st = ""
        if self.head == None:
            print("The Doubly Linked List is empty")
        else:
            t = self.head
            while t != None:
                st += str(t.data) + " "
                t = t.next
            print(f"The Doubly Linked List from left to right is:\n{st}")

    def display_right_to_left(self):
        st = ""
        if self.head == None:
            print("The Doubly Linked List is empty")
        else:
            t = self.temp
            while t != None:
                st += str(t.data) + " "
                t = t.prev
            print(f"The Doubly Linked List from right to left is:\n{st}")


obj = InsertAtEnd()
while True:
    choice = int(input("\n1.TO INSERT AT END\n2.TO INSERT AFTER SPECIFIC VALUE\n3.TO DISPLAY LEFT TO RIGHT\n4.TO DISPLAY RIGHT TO LEFT\n5.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        el = int(input("Enter the element after which you want to insert\n"))
        val = int(input("Enter the value to be inserted\n"))
        obj.insert_after_specific_value(el, val)
    elif choice == 3:
        obj.display_left_to_right()
    elif choice == 4:
        obj.display_right_to_left()
    elif choice == 5:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
