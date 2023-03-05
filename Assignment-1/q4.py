def cpy_list(l, n):
    nw_l=[None]*n
    for i in range(n):
        nw_l[i]=l[i]
    return nw_l

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
print("The array is: ")
display_array(l, n)
cpy=cpy_list(l, n)
print("Copied list: ")
display_array(cpy, n)