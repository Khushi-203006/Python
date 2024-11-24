num = int(input("enter range: "))
a = []
for i in range (num):
    n = int(input("enter elements: "))
    a.append(n)
print(a)
max = a[0]
for i in range(num):
    if (a[i] > max):
        max = a[i]

print ("largest value: " , max)
    
    
