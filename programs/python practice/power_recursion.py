def power(base,expo):
    while(expo==0):
        return 1
    return base * power(base,expo-1)

base=int(input("Enter number: "))
expo=int(input("Enter power= "))
sol=power(base,expo)
print("Answer of ",base,"^",expo,"is= ",sol)


# def power(base,expo):
#     if(expo==0):
#         return 1
#     return base * power(base,expo-1)

# base=int(input("Enter number: "))
# expo=int(input("Enter power= "))
# sol=power(base,expo)
# print("Answer of ",base,"^",expo,"is= ",sol)

# def power(base, expo):
#     # Base case: any number raised to the power of 0 is 1
#     if expo == 0:
#         return 1
#     # Recursive case
#     return base * power(base, expo - 1)

# # Input from user
# base = int(input("Enter number: "))
# expo = int(input("Enter power: "))
# sol = power(base, expo)
# print("Answer of", base, "^", expo, "is =", sol)