def count_display(l, n):
    c,s=0,0
    for i in range(n):
        if l[i]%2!=0:
            c+=1
            s+=l[i]
    print(f"There are {c} odd no.s in the list and sum of odd no.s are: {s}")

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
count_display(l, n)