"""
=> If condition statement
=> If-else statement
=> If-elif-else statement
=> Nested statement
=> Short hand if and if-else statement
"""
print("<-------If condition--------->")
mark= int(input("Enter marks:- "))
if(mark>89):
    print("Scholar")

print("<-------If-else condition--------->")
mark= int(input("Enter marks:- "))
if(mark>89):
    print("Scholar")
else:
    print("Not scholar")

print("<-------If-elif-else condition--------->")
mark= int(input("Enter marks:- "))
if(mark>89):
    print("Scholar")
elif(mark>=50 and mark<=89):
    print("Average")
else:
    print("Not scholar")

print("<----------Nested condition----------->")
a=int(input("Enter number a:- "))
b=int(input("Enter number b:- "))
c=int(input("Enter number c:- "))
if(a>b):
    if(a>c):
        print("A is greater")
    else:
        print("C is greater")
else:
    if(b>c):
        print("B is greater")
    else:
        print("C is greater")

print("<-------hand if condition--------->")
mark= int(input("Enter marks:- "))
if (mark>89): print("Scholar")

print("<-------hand if-else condition--------->")
mark= int(input("Enter marks:- "))
print("Scholar") if (mark>=90) else print("Not scholar")





















