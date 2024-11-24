#WAP to check for a perfect number
n=int(input("Enter a number:"))
sum1=0
'''
i=1
while i<=n-1:
    if n%i == 0:
        sum1+=i
    i+=1
'''
for i in range(1,n):
    if n%i==0:
        sum1+=i
print("Sum of the factors of",n,"=",sum1)



if sum1==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
