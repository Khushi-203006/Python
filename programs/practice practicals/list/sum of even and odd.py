num = int(input("enter the range: "))
a = []
for i in range (num):
    n = int(input("enter an element: "))
    a.append(n)
print ("list: " , a)
evensum = 0
oddsum = 0
for j in a:
    if j%2==0:
        evensum = evensum + j
    else:
        oddsum = oddsum + j

print ("sum of even num: " , evensum)
print ("sum of odd num: " , oddsum)
