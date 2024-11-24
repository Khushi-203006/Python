#WAP to perform linear search using list
a = []
num= int(input("Enter number of elements you want in list: "))
for i in range(num):
        n = int(input("eneter element: "))
        a.append(n)
print(a)
search = int(input("Enter element you want to search: "))
for i in range(num):
    if a[i]==search:
        print("Position of" , search , "is" , i+1)
        break
else:
    print("Not found")
        
