#WAP to display median, mean and range
a= []
n= int(input("How many elements you want: "))
for i in range(n):
    num = int(input("Enter element: "))
    a.append(num)
print("original list: ",a)
a.sort()
print("new list: ",a)

c= len(a)
if c%2 != 0:
    med = c//2
    print(a[med] , "is median")
else:
    x = a[c//2]
    y = a[(c//2)-1]
    s = x+y
    med_2 = s/2
    print (med_2, 'is median')

count1 = 0
for i in a:
    count= a.count(i)
    if count>count1:
        count1 = count
        value = i
print("Mode is: ", value)
maxi = a[0]
mini = a[0]
for i in a:
    if i>maxi:
        maxi = i
for j in a:
    if j<mini:
        mini = j
range1 = maxi - mini
print("range is" , range1)



