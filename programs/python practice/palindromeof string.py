s=input("Enter string: ")
b=""
s=s.lower()
original=s
for i in s:
    b=i+b
if(original==b):
    print("Plaindrome")
else:
    print("Not apalindrome")


# def palindrome(string):
#     string=string.lower()
#     return string== string[::-1]

# s=input("Enter string:- ")
# if(palindrome(s)):
#     print("It is palindrom")
# else:
#     print("Its not palindrome")