#WAP a program to swap value 1 space back
a = []
num= int(input("Enter number of elements you want in list: "))
for i in range(num):
        n = int(input("eneter element: "))
        a.append(n)
print(a)
b = a[num-1]
for i in range(1, num):
    a[i+1]=a[i]
a[num+1] = b
print(a)
