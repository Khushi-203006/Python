#wap to check palindrome integer
# n=int(input("Enter number: "))
# rev=0
# org=n
# while(n!=0):
#     rem=n%10
#     rev= rev*10+rem
#     n//=10
# if(rev==org):
#     print("Its palindrome")
# else:
#     print("Not palinfrome")


# def pali(string):
#     string = string.lower()
#     return string[::-1]

# string = str(input("Enter string: "))
# org=string
# if(pali(string)==org):
#     print("Its palindrome")
# else:
#     print("Its not")

string = str(input("Enter string: "))
b=""
string = string.lower()
for i in string:
    b = i + b
if(b==string):
    print("Palindrome")
else:
    print("Not palindrome")