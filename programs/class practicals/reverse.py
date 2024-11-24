#WAP to reverse a given positive integer
#WAP to check for a palindrome number
n=int(input("Enter an integer:"))
n1=n
rev=0
while n>0:
    rem = n%10
    rev = rev * 10 + rem
    n = n//10

print("The reversed no=",rev)
if rev==n1:
    print("It's a plaindrome number")
else:
    print("It's not a plaindrome number")
