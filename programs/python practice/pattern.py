'''
wap to print pattern
1
12
123
1234
12345

n=int(input("Enter number: "))
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
'''
wap to print pattern
1
22
333
4444
55555

n=int(input("Enter number: "))
for i in range(n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
'''
wap to print pattern
12345
2345
345
45
5
n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end= " ");
    print()
'''
'''
wap to print pattern
12345
1234
123
12
1

n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end= " ");
    print()
'''
'''
wap to print pattern
55555
4444
333
22
1

n=int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
'''
'''
----*
---**
--***
-****
*****
'''
n=int(input("Enter number: "))
for i in range(n-1,0,-1):
    for j in range(i,n-1
