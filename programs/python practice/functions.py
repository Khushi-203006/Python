'''
Functions are s set of code , which once created, they
can be used throughout the program.
Function help break our program into smaller parts and
helps it look more rganized and manageable.
Functions are of 2 type:-
- Define the fucntions
- Call the functions

'''
'''
def hello(str):
    print ("Hello",str)
s=str(input("Enter string: "))
hello(s)
'''
'''
def sum(x,y):----------> Parameters
    return x+y
x=int(input("Enter number: "))
y=int(input("Enter number: "))
print("Sum:-",sum(x,y))-----> Arguments

PARAMETERS-> A parameter is a variable defined in the
function's defination. Its acts as a placeholder for
the value that will be passed when the function is
called.
ARGUMENTS-> An argument is the actual value passed to
the fucntion when it is called.It replaces the
parameter during the function's execution.

def add(a,b):-----> parameters
    return a+b
print(add(2,3))-----> arguments
'''
'''
def hello(*name):
    print("Hello, my name is", name[5])
hello("john","lisa","peter")
'''
'''
return-> use to exit a function and return the value
of the function
recursion-> used athematical and programming concept.
recursion means a function can call itself, giving us
a benefit of looping through data in order to get
result.
'''
'''
def hello():
    print("hello")
    return hello()
print(hello())
#error
'''
'''
#WAP to print factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n *fact(n-1)
n=int(input("Enter number: "))
print("Factorial of",n,"is",fact(n))
'''
'''
advantage of recursion:-
-they make code look clean
-comaplex task can be broken down into small sub-parts
-sequesnces generation becomes easier
disadvantage of recursion:-
-takes lot of memory
-logic becomes hard to follow
'''
'''
--------LAMBDA FUNCTION-------
-short period of time
-numerous arguments
-have one expression only
'''
'''
#a = lambda b:b*5
#print(a(4))

x = lambda a,b,c:(a+b)*c
print(x(3,4,5))
'''
'''
-----LOCAL AND GLOBAL VARIABLE-----
local- restricted to only one block of code and connot
       be changed throughout the program
Global- not restricted to one block of code and can be
        changed throughout the program
'''
'''
LOCAL VARIABLE
x = 24
print("First variable x is",x)
def hello():
    x=25
    return x
print(hello())
print(x)
'''
'''
GLOBAL VARIABLE
x = 24
print("First variable x is",x)
def hello():
    global x
    x=25
    return x
print(hello())
print(x)
'''
'''
#waf to find maximum of 3 numbers in python
def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=int(input("Enter 1st number:- "))
b=int(input("Enter 2nd number:- "))
c=int(input("Enter 3rd number:- "))
print("Maximum number among the numbers are",max(a,b,c))
'''
'''
#waf to create and print a list where the values are
#square of number 1 and n
def create_list(n):
    l=[]
    for i in range(1,n+1):
        l.append(i**2)
    return l
num = int(input("Enter number: "))
print(create_list(num))
'''
'''
#waf that takes a number as a parameter and check if
#the number is prime or not

def prime(n):
    count=0
    for i in range(1,n+1):
        if (n%i==0):
            count+=1
    if(count==2):
        return 1
    else:
        return 0
num=int(input("Enter number:- "))
result = prime(num)
if result==1:
    print("Prime number")
else:
    print("Not Prime number")
'''
'''
#waf to sum all the number in list
def sum_of_list(l):
    sum=0
    for i in l:
       sum+=i
    return sum

l=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    n=int(input("Enter element: "))
    l.append(n)
print(l)
print("Sum of elements is list: ",sum_of_list(l))
'''
'''
#wap to solve the fabonacii sequences
def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabo(n-1)+ fabo(n-2)

n=int(input("Enter number: "))
for i in range(n):
    print(fabo(i),end=" ")
'''
'''
----MODULES----
contain set of fucntion you want to include in your
program
-Datetime
-Random
-Math
'''
'''
import datetime

x=datetime.datetime.now()
print(x)
x=datetime.datetime.date
print (x)

x=datetime.datetime(1997,10,14)
print(x.strftime("%b"))
x=datetime.datetime(1997,10,14)
print(x.strftime("%a"))
'''
'''
import random
x = random.randint(1,10) #randint- any int b/w 1 to 10
print(x)

l=["heads","tails"]
x = random.choice(l)
print(x)
'''
'''
import math
x=max(13,24,11)#same for min
print(x)

a=pow(2,4)
print(a)

b=math.sqrt(49)
print(b)

c=abs(-12*3)
print(c)

d=math.ceil(2.4)
print(d)

e=math.floor(3.3)
print(e)
'''
'''
import demo_file as d
a=d.add(3,4)
print(a)

b=d.emp["Name"]
print(b)
'''
