#WAP a program to swap value 1 space forward
a = []
num= int(input("Enter number of elements you want in list: "))
for i in range(num):
        n = int(input("enter element: "))
        a.append(n)
print(a)
key = a[num-1]
for i in range(num-2 , -1, -1):
    a[i+1] = a[i]
a[0]= key
print("new list: ", a)
