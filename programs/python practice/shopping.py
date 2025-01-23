while True:
    name = str(input("Enter customer name:- "))
    total=0
    while True:
        price = int(input("Enter price= "))
        quantity = int(input("Enter quantity= "))
        total+=price*quantity
        repeat = input("Do you want to add more items? (Yes/No)")
        if(repeat == "no" or repeat == "No"):
            break
    print("*"*40)
    print("Name:- ",name)
    print("Total price:- ",total)
    print("*"*40)
    cust = input("Do you want to move on next customer? (Yes/No)")
    if(cust=="no" or cust=="No"):
        break
