# Represent a polynomial using an array
class Polynomial:
    def __init__(self, coefficient, exponent):
        self.coefficient=coefficient
        self.exponent=exponent

def create_polynomial(l, size):
    
    print("Enter the polynomial")
    for i in range(size):
        coef=int(input(f"Enter the coefficient of term {i+1}:\n"))
        exp=int(input(f"Enter the exponent of term {i+1}:\n"))
        l[i]=Polynomial(coef, exp)

def add_polynomial(l1, l2, t1, t2, result):
    # ti and t2 are the no. of term in polynomial l1 and l2
    # result is the result of additon of the polynomials
    
    i,j,k=0,0,0
    while i<t1 and j<t2:
        if l1[i].exponent==l2[j].exponent:
            result[k]=Polynomial((l1[i].coefficient+l2[j].coefficient), l1[i].exponent)
            i+=1
            j+=1
        elif l1[i].exponent>l2[j].exponent:
            result[k]=Polynomial(l1[i].coefficient, l1[i].exponent)
            i+=1
        elif l1[i].exponent<l2[j].exponent:
            result[k]=Polynomial(l2[j].coefficient, l2[j].exponent)
            j+=1
        k+=1
    while i<t1:
        result[k]=Polynomial(l1[i].coefficient, l1[i].exponent)
        i+=1
        k+=1
    while j<t2:
        result[k]=Polynomial(l2[j].coefficient, l2[j].exponent)
        j+=1
        k+=1
    return k

def display_polynomial(arr, n):
    st=""
    for i in range(n):
        if i==n-1:
            st+=str(arr[i].coefficient)+"x^"+str(arr[i].exponent)
        else:
            st+=str(arr[i].coefficient)+"x^"+str(arr[i].exponent)+"+"
    print(st.replace(" ", ""))


size1=int(input("Enter the no. of terms in the 1st polynomial:\n"))
p1=[None]*size1
create_polynomial(p1, size1)
print("The 1st polynomial is: ")
display_polynomial(p1, size1)
size2=int(input("Enter the no. of terms in the 2nd polynomial:\n"))
p2=[None]*size2
create_polynomial(p2, size2)
print("The 2nd polynomial is: ")
display_polynomial(p2, size2)
result=[None]*(size1+size2)
res_terms=add_polynomial(p1,p2, size1, size2, result)
print("The sum of polynomials: ")
print(type(result))
print(res_terms)
display_polynomial(result, res_terms)