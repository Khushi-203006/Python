# WAP to check whether the number is a perfect number or not.

number = int(input("enter any number:"))
sum = 0
for i in range(1,number):
    if (number % i ==0):
        sum = sum + i
if (sum==number):
    print ("%d is a perfect number" %number)
else :
    print ("%d is not a perfect number" % number)
