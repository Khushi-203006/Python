def power(base,expo):
    sol=1
    for i in range(1,expo+1):
        sol*=base
    return sol

base=int(input("Enter number: "))
expo=int(input("Enter power= "))
sol=power(base,expo)
print("Answer of ",base,"^",expo,"is= ",sol)


        