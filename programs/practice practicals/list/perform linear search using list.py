#WAP to perform linear search using list
num = int(input("enter range: "))
a=[]
value = 0
for i in range(num):
    n = int(input("enter element: "))
    a.append(n)
print (a)
find = int(input("eneter element you want to search: "))
for i in range (num):
    if a[i] == find:
        print(find, "is at" , i+1 ,"postion" )
        value = 1
        break
if value == 0:
    print("not found")
        
        
