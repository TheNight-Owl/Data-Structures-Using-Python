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

    def delete_from_specific_position(self):
        if self.head == None:
            print("The Doubly Linked List is empty")
        else:
            position = int(input("Enter the position from which you want to delete\n"))
            s = 0
            t = self.head
            while t != None:
                s += 1
                t = t.next
            if position < 1 or position > s:
                print("Invalid Position")
            else:
                if position == 1:
                    print(f"Element {self.head.data} deleted")
                    loc = self.head.next
                    del self.head
                    if loc == None:
                        self.head = None
                        self.temp = None
                    else:
                        self.head = loc
                        self.head.prev = None
                else:
                    t = self.head
                    i = 1
                    while i < position - 1:
                        i += 1
                        t = t.next
                    print(f"Element deleted: {t.next.data}")
                    loc = t.next.next
                    if loc == None:
                        del t.next
                        t.next = None
                        del self.temp
                        self.temp = t
                    else:
                        loc.prev = t
                        del t.next
                        t.next = loc

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
    choice = int(input("\n1.TO INSERT AT END\n2.TO DELETE FROM SPECIFIC POSITION\n3.TO DISPLAY LEFT TO RIGHT\n4.TO DISPLAY RIGHT TO LEFT\n5.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        obj.delete_from_specific_position()
    elif choice == 3:
        obj.display_left_to_right()
    elif choice == 4:
        obj.display_right_to_left()
    elif choice == 5:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
