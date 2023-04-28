from NodeStructure import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def insert_at_end(self, value):
        if self.head == None:
            self.head = Node(value)
            self.temp = self.head
        else:
            self.temp.link = Node(value)
            self.temp = self.temp.link

    def delete_from_specific_position(self):
        if self.head == None:
            print("The linked list is empty")
        else:
            position = int(input("Enter the position from which you want to delete\n"))
            s = 0
            t = self.head
            while t != None:
                s += 1
                t = t.link
            if position < 1 or position > s:
                print("Invalid Position")
            else:
                if position == 1:
                    loc = self.head.link
                    print(f"Element {self.head.data} deleted")
                    del self.head
                    self.head = loc
                else:
                    t = self.head
                    i = 1
                    while i < position - 1:
                        i += 1
                        t = t.link
                    print(f"Element deleted: {t.link.data}")
                    loc = t.link.link
                    del t.link
                    t.link = loc

    def display(self):
        st = ""
        if self.head == None:
            print("The Linked List is empty")
        else:
            t = self.head
            while t != None:
                st += str(t.data) + " "
                t = t.link
            print(f"The Linked List is:\n{st}")


obj = LinkedList()
while True:
    choice = int(input("\n1.TO INSERT AT END\n2.TO DELETE FROM SPECIFIC POSITION\n3.TO DISPLAY THE LINKED LIST\n4.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        obj.delete_from_specific_position()
    elif choice == 3:
        obj.display()
    elif choice == 4:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
