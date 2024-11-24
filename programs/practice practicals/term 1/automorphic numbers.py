#WAP to check if it is automorphic or not

n = int(input("Enter value:  "))

squr = n**2

if n % 10 == squr % 10:
    print ("it is an automorpic number")

else:
    print ("it is not an automorpic number")
