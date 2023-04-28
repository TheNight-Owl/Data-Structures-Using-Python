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
                t = t.link
        if k == 0:
            print("Sorry the given value not found. Element cannot be inserted")
        else:
            loc = Node(value)
            loc.link = t.link
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
    choice = int(input("\n1.TO INSERT AT END\n2.TO INSERT AFTER A SPECIFIC VALUE\n3.TO DISPLAY THE LINKED LIST\n4.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        el = int(input("Enter the value after which you want to insert\n"))
        val = int(input("Enter the value\n"))
        obj.insert_after_specific_value(el, val)
    elif choice == 3:
        obj.display()
    elif choice == 4:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
