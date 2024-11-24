import area_of_circle
import circumference_of_circle
import perimeter_of_rectangle
import area_of_rectangle
choice = 0

ch= "y"
print ("MENU:- ")
print ("1. Area of Circle")
print ("2. Circumference of Circle")
print ("3. Perimeter of Rectangle")
print ("4. Area of Rectangle")
print ("5. Quit")
ch = int(input("Enter your choice: "))
while True:
    if (ch==1):
        radius = int(input("Enter radius: "))
        print ("Area of Circle is" , area_of_circle.area(radius))
        break
    elif (ch==2):
        radius = int(input("Enter radius: "))
        print ("Circumference of Circle is" , circumference_of_circle.circumference(radius))
        break
    elif (ch==3):
        length =int(input("Enter length: "))
        width = int(input("Enter width: "))
        print ("Perimeter of Rectangle is" , perimeter_of_rectangle.perimeter(width,length))
        break
    elif (ch==4):
        length =int(input("Enter length: "))
        width = int(input("Enter width: "))
        print ("Area of Rectangle is" , area_of_rectangle.area(width,length))
        break
    elif (ch==5):
        print ("exit the program")
        break
    else:
        print ("invalid choice")
        break
