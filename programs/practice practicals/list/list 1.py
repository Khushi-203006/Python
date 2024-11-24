num = int(input("enter the range: "))
a = []
for i in range (num):
    n = int(input("enter an element: "))
    a.append(n)
print (a)
evensum = 0
oddsum = 0
for i in a:
    if i%2==0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i

print ("sum of even num: " , evensum)
print ("sum of odd num: " , oddsum)
