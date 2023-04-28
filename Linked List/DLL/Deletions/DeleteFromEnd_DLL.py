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

    def delete_from_end(self):
        if self.head == None:
            print("The Doubly Linked List is empty")
        else:
            if self.head == self.temp:
                print(f"Element deleted: {self.temp.data}")
                del self.head
                self.head = None
                self.temp = None
            else:
                print(f"Element deleted: {self.temp.data}")
                loc = self.temp.prev
                loc.next = None
                del self.temp
                self.temp = loc

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
    choice = int(input("\n1.TO INSERT AT END\n2.TO DELETE FROM END\n3.TO DISPLAY LEFT TO RIGHT\n4.TO DISPLAY RIGHT TO LEFT\n5.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        obj.delete_from_end()
    elif choice == 3:
        obj.display_left_to_right()
    elif choice == 4:
        obj.display_right_to_left()
    elif choice == 5:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
