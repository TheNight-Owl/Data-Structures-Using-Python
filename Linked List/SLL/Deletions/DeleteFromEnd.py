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

    def delete_from_end(self):
        if self.head == None:
            print("The Linked List doesn't exist...")
        else:
            t = self.head
            p = None
            while t.link != None:
                p = t
                t = t.link
            print(f"Element deleted: {t.data}")
            if p == None:
                del self.head
                self.head = None
            else:
                p.link = None
                del t

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
    choice = int(input("\n1.TO INSERT AT END\n2.TO DELETE FROM END\n3.TO DISPLAY THE LINKED LIST\n4.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        obj.delete_from_end()
    elif choice == 3:
        obj.display()
    elif choice == 4:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
