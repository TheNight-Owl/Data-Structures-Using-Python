def reverse_l(l, n):
    for i in range(0, n//2):
        t=l[i]
        l[i]=l[n-i-1]
        l[n-i-1]=t

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
print("The array before reversing:")
display_array(l, n)
reverse_l(l, n)
print("Array after reversal: ")
display_array(l, n)