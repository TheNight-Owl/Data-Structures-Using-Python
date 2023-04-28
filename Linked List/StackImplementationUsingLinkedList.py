from NodeStructure import Node
class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top == None:
            self.top = Node(value)
        else:
            temp = self.top
            self.top = Node(value)
            self.top.link = temp
        print("Element pushed successfully")

    def pop(self):
        if self.top == None:
            print("Stack Underflow")
        else:
            print(f"Element popped: {self.top.data}")
            loc = self.top.link
            del self.top
            self.top = loc

    def isEmpty(self):
        if self.top == None:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def length_of_the_stack(self):
        s = 0
        t = self.top
        while t != None:
            s += 1
            t = t.link
        print(f"The length of the stack is: {s}")

    def getTop(self):
        if self.top == None:
            print("Stack Underflow")
        else:
            print(f"Element at the top of the stack is {self.top.data}")

    def display(self):
        st = ""
        if self.top == None:
            print("The Linked List is empty")
        else:
            t = self.top
            while t != None:
                st += str(t.data) + " "
                t = t.link
            print(f"The Stack is:\n{st}")


while True:
    choice = int(input("\n1.CREATE STACK\n2.DELETE STACK\n3.PUSH\n4.POP\n5.DISPLAY TOP ELEMENT\n6.DISPLAY ENTIRE STACK\n7.LENGTH OF THE STACK\n8.STACK EMPTY OR NOT\n9.EXIT\n"))
    if choice == 1:
        obj = LinkedStack()
    elif choice == 2:
        del obj
    elif choice == 3:
        val = int(input("Enter the value:\n"))
        obj.push(val)
    elif choice == 4:
        obj.pop()
    elif choice == 5:
        obj.getTop()
    elif choice == 6:
        obj.display()
    elif choice == 7:
        obj.length_of_the_stack()
    elif choice == 8:
        obj.isEmpty()
    elif choice == 9:
        break
    else:
        print("Wrong choice. Try again....")
