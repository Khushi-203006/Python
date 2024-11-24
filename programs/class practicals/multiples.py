#WAP to display the multiples of any positive integer
n=int(input("Enter a number:"))
many=int(input("How many multiples?"))
i=1
while i<=many:
    print(n*i)
    i+=1
'''
for i in range(1,many+1):
    print(n*i)
'''
