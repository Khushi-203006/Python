#WAP to twice the odd numbers and half the even numbers of a given list
odd_list = []
even_list = []
num = int(input("enter the range: "))
a=[]
for i in range (num):
    n = int(input("enter element: "))
    a.append(n)
print (a)
for i in a:
    if i%2==0:
        m = i//2
        even_list.append(m)
    else:
        p = i*2
        odd_list.append(p)

print ("twice of odd number in list:" ,odd_list)
print ("half of even number in list:" ,even_list)





