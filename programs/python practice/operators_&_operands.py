print("""
operators in python are of 7 types-
1) Arithmetic operators(+,-,*,//,**,/,%)
2) Comparison operators(<,>,==,!=,<=,>=)
3) Logical operators(and,or,not)
4) Assignment operators(=,+=,-=,*=...)
5) Identity operators(is , not is)
6) Membership operators(in, not in)
7) Bitwise operators (&,|,^,<<,>>)
""")
print("<---------ARITHEMATIC----------->")
a=int(input("Enter number a:- "))
b=int(input("Enter number b:- "))
print("+-> ",a+b)
print("--> ",a-b)
print("*-> ",a*b)
print("//->",a//b)
print("**->",a**b)
print("/-> ",a/b)
print("%-> ",a%b)
print("<---------COMPARISON----------->")
m=int(input("Enter number m:- "))
n=int(input("Enter number n:- "))
print("< =>",m<n)
print("> =>",m>n)
print("<= =>",m<=n)
print(">= =>",m>=n)
print("== =>",m==n)
print("!= =>",m!=n)
print("<---------LOGICAL----------->")
m=int(input("Enter number m:- "))
n=int(input("Enter number n:- "))
print("AND:- ",(m<n and n>m))
print("OR:- ",(m==n or n==m))
print("NOT in and:- ",not(m and n))
print("NOT in or:- ",not(m or n))
print("<---------ASSIGNMENT----------->")
m=int(input("Enter number m:- "))
m+=20
print("+= --> ",m)
m-=10
print("-= --> ",m)
m*=2
print("*= --> ",m)
m/=10
print("/= --> ",m)
print("<---------IDENTITY----------->")
x=[1,2,3,4,5,6]
y=x
z=[1]
print("Is:- ",x is y)
print("Not is:- ",z is not y)
print("<---------MEMBERSHIP----------->")
x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6,'x']
string = "xyz"
print("In:- ",1 in x)
print("Not in:- ",10 not in x)
print('x' in y)
print("<---------BITWISE----------->")
print("And:- ",((7>3)&(2>3)))
print("Or:- ",((7>3) | (3<7)))
print("Not:- ",not(7>3))
print(">>:- ",20>>2)
print("<<:- ",20<<2)










