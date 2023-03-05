def insert_val(a, pos, n):
    value=int(input("Enter the value:\n"))
    for i in range(n, pos-1, -1):
        a[i]=a[i-1]
    a[pos]=value
    n+=1
    return n

def check_pos(a, pos, size, n):
    if pos<0 or pos>=size:
        print("Invalid position")
    elif size==n:
        print("Item cannot be inserted as the array is full")
    else:
        n=insert_val(a, pos, n)
        print("Array after inserting element:")
        display_array(a, n)


def display_array(a, n):
    for i in range(n):
        print(a[i], end=" ")
    print("\n")

size=int(input("Enter the size of the array:\n"))
a=[None]*size
n=int(input(f"Enter no. of elements you want to insert:\n"))
assert n<=size
print(f"Enter {n} elements in the array:")
for i in range(n):
    a[i]=int(input())
print("Array before insertion:")
display_array(a, n)
pos=int(input("Enter the position where you want to insert an element\n"))
check_pos(a, pos, size, n)
