#WAP to calculate percentage of marks
sub1 = int(input("enter marks out of 30:"))
sub2 = int(input("enter marks out of 30:"))
sub3 = int(input("enter marks out of 30:"))

percentage = sub1 + sub2 + sub3 / 90 * 100

print ("percentage: ", percentage)

if percentage >= 35:
    print("pass")
else:
    print ("fail")

