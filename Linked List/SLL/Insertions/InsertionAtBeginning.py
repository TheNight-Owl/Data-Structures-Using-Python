from NodeStructure import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.link = temp

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
    choice = int(input("\n1.TO INSERT AT BEGINNING\n2.TO DISPLAY THE LINKED LIST\n3.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_beginning(val)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
