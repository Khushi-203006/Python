#WAP to display the factors of a positive integer
n=int(input("Enter a positive integer:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
'''
i=1
while i<=n:
    if n%i == 0:
        print(i)
    i+=1
'''
