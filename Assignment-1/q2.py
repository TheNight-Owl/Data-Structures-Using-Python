def linear_s(l, n, ns):
    for i in range(n):
        if l[i]==ns:
            return i
    return -1

def del_ele(l, n, ns):
    pos=linear_s(l, n, ns)
    if pos==-1:
        print("Element not found in the list...")
    else:
        for i in range(pos, n-1):
            l[i]=l[i+1]
        n-=1
        if n<=0:
            print("List is now underflow..empty list..")
        else:
            print("Array after deletion:")
            display_array(l, n)

def display_array(l, n):
    for i in range(n):
        print(l[i], end=" ")
    print("\n")

size=int(input("Enter the size of the array:\n"))
l=[None]*size
n=size
print(f"Enter {n} elements in the array:")
for i in range(n):
    l[i]=int(input())
print("The array:")
display_array(l, n)
ns=int(input("Enter the element to delete:\n"))
del_ele(l, n, ns)