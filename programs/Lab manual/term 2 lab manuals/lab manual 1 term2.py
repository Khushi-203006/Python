#WAP that returns the largest and the smallest even number in the list
num = int(input("Enter range: "))
a = []
for i in range (num):
    n = int(input("enter element: "))
    a.append(n)
print ("original list: " , a)
even_list = []
for i in range (num):
    if a[i] % 2==0:
        even_list.append(a[i])
    else:
        pass
print ("even number list: " , even_list)
num = len(even_list)
if (num > 0):
    max = even_list[0]
    for i  in range (num):
        if (even_list[i] > max):
            max = even_list[i]
    print ("maximum number: " , max)
    min = even_list[0]
    for i  in range (num):
        if (even_list[i] <min):
            min = even_list[i]
    print ("minimum number: " , min)
else:
    print ("No even element")
