#wap to calculate area
print("""
<--Menu-->
1.Circle
2.Sqaure
3.Rectangle
4.Triangle
""")

ch = int(input("Enter choice: "))
if(ch==1):
    r = int(input("Enter radius: "))
    print("Area of circle: ", 3.14*r*r)
elif(ch==2):
    a = int(input("Enter side: "))
    print("Area of sqaure: ", a*a)
elif(ch==3):
    l = int(input("Enter lenght: "))
    b = int(input("Enter breadth: "))
    print("Area of rectangle: ", l*b)
elif(ch==4):
    h = int(input("Enter height: "))
    b = int(input("Enter base: "))
    print("Area of triangle: ",0.5*h*b)
else:
    print("Wrong choice")
