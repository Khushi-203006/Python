#WAP to print the fibonacci sequence
n = int(input("enter number of terms: "))
F1=0
F2=1

for i  in range (0,n):
    print(F1,F2, end= " ")
    next = F1+F2
    F1 = F2
    F2= next
    





