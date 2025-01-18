a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
op=str(input("Enter string: "))
if(op== "+"):
    print("Sum = ",a+b)
elif(op=="-"):
    print("Diff= ",a-b)
elif(op=="*"):
    print("Product: ",a*b)
elif(op=="/"):
    print("Quotient: ",a/b)
elif(op=="%"):
    print("Remainder: ",a%b)
else:
    print("Invalid operator: ")
