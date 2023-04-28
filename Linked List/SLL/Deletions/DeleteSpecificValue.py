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

    def delete_specific_value(self):
        if self.head == None:
            print("The linked list is empty")
        else:
            value = int(input("Enter the value you want to delete:\n"))
            if self.head.data == value:
                loc = self.head.link
                print(f"Element {self.head.data} deleted")
                del self.head
                self.head = loc
            else:
                t = self.head
                p = None
                while t != None and t.data != value:
                    p = t
                    t = t.link
                if p.link == None:
                    print("Value not found in the given list")
                else:
                    print(f"Element {t.data} deleted")
                    p.link = t.link
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
    choice = int(input("\n1.TO INSERT AT END\n2.TO DELETE A PARTICULAR VALUE\n3.TO DISPLAY THE LINKED LIST\n4.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        obj.delete_specific_value()
    elif choice == 3:
        obj.display()
    elif choice == 4:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
