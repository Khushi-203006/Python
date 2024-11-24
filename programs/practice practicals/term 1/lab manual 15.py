#WAP to perform all task
original= input("enter string: ")
Reverse= ' '
for i in range(len(original) -1, -1, -1):
    Reverse= Reverse+original[i]
if original==Reverse:
    print("it is a palindrome")
else:
    print("it is a palindrome")


