# Represent a polynomial using an array
class Polynomial:
    def __init__(self, coefficient, exponent):
        self.coefficient=coefficient
        self.exponent=exponent

def create_polynomial():
    size=int(input("Enter the no. of terms in the polynomial:\n"))
    l=[None]*size
    print("Enter the polynomial")
    for i in range(size):
        coef=int(input(f"Enter the coefficient of term {i+1}:\n"))
        exp=int(input(f"Enter the exponent of term {i+1}:\n"))
        l[i]=Polynomial(coef, exp)
    display_polynomial(l, size)

def display_polynomial(arr, n):
    st=""
    for i in range(n):
        if i==n-1:
            st+=str(arr[i].coefficient)+"x^"+str(arr[i].exponent)
        else:
            st+=str(arr[i].coefficient)+"x^"+str(arr[i].exponent)+"+"
    print(st.replace(" ", ""))

create_polynomial()