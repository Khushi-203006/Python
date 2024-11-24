num = int(input("enter the range: "))
a = []
for i in range (num):
    n = int(input("enter an element: "))
    a.append(n)
print (a)
sum=0
for i in a:
    sum = sum+i
print("sum of elemnst in list: " , sum)
    
