#WAP to calculate the percentage of marks obtained.

English = float (input("Enter English marks out of 50 :"))
Computer = float (input("Enter Computer marks out of 50:"))
Maths = float (input("Enter Maths marks out of 50:"))
Chemistry = float (input("Enter Chemistry marks out of 50:"))
Physics = float (input("Enter Physics marks out of 50:"))

Total = English + Computer + Maths + Chemistry + Physics
Percentage = Total / 250 * 100

print ("Total marks:" , str(Total) + " out of 250" )
print ("Percentage:" , Percentage)
