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

    def delete_specific_value(self):
        if self.head == None:
            print("The Doubly Linked List is empty")
        else:
            value = int(input("Enter the value you want to delete\n"))
            if self.head.data == value:
                loc = self.head.next
                print(f"Element {self.head.data} deleted")
                del self.head
                if loc == None:
                    self.head = None
                    self.temp = None
                else:
                    self.head = loc
                    self.head.prev = None
            else:
                t = self.head
                p = None
                while t != None and t.data != value:
                    p = t
                    t = t.next
                if p.next == None:
                    print("Value not found in the given doubly linked list")
                else:
                    print(f"Element {t.data} deleted")
                    p.next = t.next
                    if t.next != None:
                        t.next.prev = p
                    else:
                        self.temp = p
                    del t

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
    choice = int(input("\n1.TO INSERT AT END\n2.TO DELETE SPECIFIC VALUE\n3.TO DISPLAY LEFT TO RIGHT\n4.TO DISPLAY RIGHT TO LEFT\n5.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        obj.delete_specific_value()
    elif choice == 3:
        obj.display_left_to_right()
    elif choice == 4:
        obj.display_right_to_left()
    elif choice == 5:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
