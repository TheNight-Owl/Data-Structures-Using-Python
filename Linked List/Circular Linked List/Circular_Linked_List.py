from NodeStructure import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.lastnode = None

    def insert_at_end(self, value):
        if self.head == None:
            self.head = Node(value)
            self.head.link = self.head
            self.lastnode = self.head
        else:
            loc = Node(value)
            loc.link = self.head
            self.lastnode.link = loc
            self.lastnode = loc

    def insert_at_beginning(self, value):
        if self.head == None:
            self.head = Node(value)
            self.head.link = self.head
            self.lastnode = self.head
        else:
            temp = self.head
            self.head = Node(value)
            self.head.link = temp
            self.lastnode.link = self.head

    def insert_after_value(self, element, value):
        if self.head == None:
            print("The Circular Linked List doesn't exist...")
        else:
            t = self.head
            p = None
            k = 0
            while p != self.lastnode:
                p = t
                if p.data == element:
                    k = 1
                    break
                t = t.link
            if k == 0:
                print("Element could not be inserted as value hadn't been found")
            else:
                loc = Node(value)
                loc.link = t.link
                if t.link == self.head:
                    self.lastnode = loc
                t.link = loc

    def insert_at_position(self):
        position = int(input("Enter the position at which you want to insert\n"))
        t = self.head
        p = None
        c = 0
        while p != self.lastnode:
            p = t
            c += 1
            t = t.link
        if position < 1 or position > c + 1:
            print("Invalid position.")
        else:
            value = int(input("Enter the value that you want to insert\n"))
            if position == 1:
                if self.head == None:
                    self.head = Node(value)
                    self.head.link = self.head
                    self.lastnode = self.head
                else:
                    temp = self.head
                    self.head = Node(value)
                    self.head.link = temp
                    self.lastnode.link = self.head
            else:
                t = self.head
                i = 1
                while i < position - 1:
                    i += 1
                    t = t.link
                loc = Node(value)
                loc.link = t.link
                if t.link == self.head:
                    self.lastnode = loc
                t.link = loc

    def delete_from_end(self):
        if self.head == None:
            print("The Circular Linked List doesn't exist...")
        else:
            t = self.head
            p = None
            while t.link != self.head:
                p = t
                t = t.link
            print(f"Element deleted: {t.data}")
            if p == None:
                del self.head
                self.head = None
                self.lastnode = None
            else:
                p.link = t.link
                self.lastnode = p
                del t

    def delete_from_beginning(self):
        if self.head == None:
            print("The Circular Linked List doesn't exist...")
        else:
            print(f"Element deleted: {self.head.data}")
            if self.head.link == self.head:
                del self.head
                self.head = None
                self.lastnode = None
            else:
                loc = self.head.link
                del self.head
                self.head = loc
                self.lastnode.link = self.head

    def delete_specific_value(self):
        if self.head == None:
            print("The  Circular Linked list is empty")
        else:
            value = int(input("Enter the value you want to delete:\n"))
            if self.head.data == value:
                print(f"Element {self.head.data} deleted")
                if self.head.link == self.head:
                    del self.head
                    self.head = None
                    self.lastnode = None
                else:
                    loc = self.head.link
                    del self.head
                    self.head = loc
                    self.lastnode.link = self.head
            else:
                t = self.head
                p = None
                k = 0
                while p != self.lastnode:
                    if t.data == value:
                        k = 1
                        break
                    p = t
                    t = t.link
                if k == 0:
                    print("Value not found in the given list")
                else:
                    print(f"Element {t.data} deleted")
                    p.link = t.link
                    if t.link == self.head:
                        self.lastnode = p
                    del t

    def delete_from_position(self):
        c = 0
        if self.head == None:
            print("The Circular Linked List is empty")
        else:
            position = int(input("Enter the position from where you want to delete\n"))
            t = self.head
            p = None
            while p != self.lastnode:
                p = t
                c += 1
                t = t.link
            if position < 1 or position > c:
                print("Invalid position.")
            else:
                if position == 1:
                    print(f"Element {self.head.data} deleted")
                    if self.head.link == self.head:
                        del self.head
                        self.head = None
                        self.lastnode = None
                    else:
                        loc = self.head.link
                        del self.head
                        self.head = loc
                        self.lastnode.link = self.head
                else:
                    i = 1
                    while i < position - 1:
                        i += 1
                        t = t.link
                    print(f"Element deleted: {t.link.data}")
                    loc = t.link.link
                    del t.link
                    t.link = loc
                    if t.link == self.head:
                        self.lastnode = t

    def display(self):
        st = ""
        if self.head == None:
            print("The Circular Linked List is empty")
        else:
            t = self.head
            p = None
            while p != self.lastnode:
                p = t
                st += str(t.data) + " "
                t = t.link
            print(f"The Circular Linked List is:\n{st}")

obj = LinkedList()
while True:
    choice = int(input("\n1.TO INSERT AT END\n2.TO INSERT AT BEGINNING\n3.TO INSERT AFTER GIVEN ELEMENT\n4.TO INSERT AT GIVEN POSITION\n5.TO DELETE FROM END\n6.TO DELETE FROM BEGINNING\n7.TO DELETE A GIVEN VALUE\n8.TO DELETE FROM GIVEN POSITION\n9.TO DISPLAY THE CIRCULAR LINKED LIST\n10.TO EXIT...\n"))
    if choice == 1:
        val = int(input("Enter the value\n"))
        obj.insert_at_end(val)
    elif choice == 2:
        val = int(input("Enter the value\n"))
        obj.insert_at_beginning(val)
    elif choice == 3:
        el = int(input("Enter the element after which you want to insert\n"))
        v = int(input("Enter the value that you want to insert\n"))
        obj.insert_after_value(el, v)
    elif choice == 4:
        obj.insert_at_position()
    elif choice == 5:
        obj.delete_from_end()
    elif choice == 6:
        obj.delete_from_beginning()
    elif choice == 7:
        obj.delete_specific_value()
    elif choice == 8:
        obj.delete_from_position()
    elif choice == 9:
        obj.display()
    elif choice == 10:
        break
    else:
        print("WRONG CHOICE. PLEASE TRY AGAIN...")
