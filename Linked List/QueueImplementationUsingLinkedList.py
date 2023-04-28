from NodeStructure import Node
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):                   #Insertion at end
        if self.front == None:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.link = Node(value)
            self.rear = self.rear.link

    def dequeue(self):                          #Deletion from beginning
        if self.front == None:
            print("The queue doesn't exist...")
        else:
            print(f"Element deleted: {self.front.data}")
            loc = self.front.link
            del self.front
            self.front = loc

    def isEmpty(self):
        if self.front == None:
            print("Queue underflow")
        else:
            print("Queue is not empty")

    def getFront(self):
        if self.front == None:
            print("Queue Underflow")
        else:
            print(f"Element at the front of the queue is {self.front.data}")

    def display(self):
        st = ""
        if self.front == None:
            print("Queue underflow")
        else:
            t = self.front
            while t != None:
                st += str(t.data) + " "
                t = t.link
            print(f"The queue is:\n{st}")


while True:
    choice = int(input("\n1.CREATE QUEUE\n2.DELETE QUEUE\n3.ENQUEUE\n4.DEQUEUE\n5.FRONT ELEMENT\n6.DISPLAY ENTIRE QUEUE\n7.QUEUE EMPTY OR NOT\n8.EXIT\n"))
    if choice == 1:
        obj = LinkedQueue()
    elif choice == 2:
        del obj
        print("Queue deleted")
    elif choice == 3:
        val = int(input("Enter the value:\n"))
        obj.enqueue(val)
    elif choice == 4:
        obj.dequeue()
    elif choice == 5:
        obj.getFront()
    elif choice == 6:
        obj.display()
    elif choice == 7:
        obj.isEmpty()
    elif choice == 8:
        break
    else:
        print("Wrong choice. Try again....")
