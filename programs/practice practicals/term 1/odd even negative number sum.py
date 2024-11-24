oddsum = 0
evensum=0
negativesum = 0

while (1==1):
    n=int(input("enter number:"))
    if n==0:
        break
    if n<0:
        negativesum = negativesum + n
    else : 
        if n%2==0:
            evensum = evensum + n
        else :
            oddsum = oddsum + n

print ("sum of negative number: ", negativesum)
print("sum of even number: ", evensum)
print("sum of odd number: ", oddsum)


      
