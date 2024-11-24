#WAP to first n prime numbers
num= int(input("enter the number: "))
c = 2
while num!=0:
    for i in range(2,c):
        if c % 1==0:
            break
    else:
        print(c,end = ' ' )
        num-=1

    c +=1


