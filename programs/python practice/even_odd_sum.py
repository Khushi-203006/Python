#WAP to print sum of all even and odd numbers
even_sum=0
odd_sum=0
i=50
'''
for i in range(1,51):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("Even sum=",even_sum, "Odd sum=",odd_sum)
'''
while(i!=0):
    if(i%2==0):
        even_sum+=i
        i-=1
    else:
        odd_sum+=i
        i-=1
print("Even sum=",even_sum, "Odd sum=",odd_sum)
