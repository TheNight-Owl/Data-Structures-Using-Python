from NodeStructureDoublyLinkedList import Node
class InsertAtEnd:
    def __init__(self):
        self.head = None
        self.temp = None

    def insert_at_specific_position(self):
        position = int(input("Enter the position at which you want to insert an element:\n"))
        s = 0
        t = self.head
        while t != None:
            s += 1
            t = t.next
        if position < 1 or position > s + 1:
            print("Invalid Position")
        else:
            value = int(input("Enter the value\n"))
            if position == 1:
                loc = Node(value)
                loc.next = self.head
                if self.head == None:
                    self.temp = loc
                else:
                    self.head.prev = loc
                self.head = loc
            else:
                t = self.head
                i = 1
                while i < position - 1:
                    i += 1
                    t = t.next

                loc = Node(value)
                loc.next = t.next
                loc.prev = t
                if t.next == None:
                    self.temp = loc
                else:
                    t.next.prev = loc
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
    choice = int(input("\n1.TO INSERT AT SPECIFIC POSITION\n2.TO DISPLAY LEFT TO RIGHT\n3.TO DISPLAY RIGHT TO LEFT\n4.TO EXIT...\n"))
    if choice == 1:
        obj.insert_at_specific_position()
    elif choice == 2:
        obj.display_left_to_right()
    elif choice == 3:
        obj.display_right_to_left()
    elif choice == 4:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
