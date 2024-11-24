#WAP to display the even numbers from the input given by the user.

ch='Y'
while ch in 'Yy':
    n=int(input("enter an integer:"))
    if n%2 == 0:
        print(n,"is an even number")
    ch=input("Do you want to continue entering integers(Y/N)?")

