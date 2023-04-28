from NodeStructureDoublyLinkedList import Node
class InsertAtEnd:
    def __init__(self):
        self.head = None
        self.temp = None

    def insert_at_beginning(self, value):
        if self.head == None:
            self.head = Node(value)
            self.temp = self.head
        else:
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev

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
    choice = int(input("\n1.TO INSERT AT BEGINNING\n2.TO DISPLAY LEFT TO RIGHT\n3.TO DISPLAY RIGHT TO LEFT\n4.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_beginning(val)
    elif choice == 2:
        obj.display_left_to_right()
    elif choice == 3:
        obj.display_right_to_left()
    elif choice == 4:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
