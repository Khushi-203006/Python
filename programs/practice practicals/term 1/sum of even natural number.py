#WAP to find and print the SUM of first N even natural numbers

num = int(input("Enter a number: "))

i=1
iLimit=num*2

sum=0
while (i<=iLimit):
    if i%2==0:
        sum += i
        
    i+=1


        
print ("The result is", sum)    
