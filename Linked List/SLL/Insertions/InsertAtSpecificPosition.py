from NodeStructure import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_specific_position(self, position):
        s = 0
        t = self.head
        while t != None:
            s += 1
            t = t.link
        if position < 1 or position > s + 1:
            print("Invalid Position")
        else:
            value = int(input("Enter the value\n"))
            if position == 1:
                loc = Node(value)
                loc.link = self.head
                self.head = loc
            else:
                t = self.head
                i = 1
                while i < position - 1:
                    i += 1
                    t = t.link
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
    choice = int(input("\n1.TO INSERT AFTER A SPECIFIC POSITION\n2.TO DISPLAY THE LINKED LIST\n3.TO EXIT...\n"))
    if choice == 1:
        pos = int(input("Enter the position at which you want to insert\n"))
        obj.insert_after_specific_position(pos)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
