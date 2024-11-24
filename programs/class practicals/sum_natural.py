#WAP to find the sum of the natural numbers till 'n'
#WAP to find the sum of the squares of the natural numbers till 'n'
n=int(input("Enter a positive integer:"))
sum1=0
#while loop
i=1
while i<=n:
    sum1=sum1+i
    i+=1
print("Sum of the natural numbers=",sum1)

sum1=0
for j in range(1,n+1):
    sum1+=j
print("Sum of the natural numbers=",sum1)
