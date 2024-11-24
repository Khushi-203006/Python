#WAP to input marks in 3 subjects; compute average and then calculate grade

Subject1 = float(input("Enter marks of Subject 1 out of 50:"))
Subject2 = float(input("Enter marks of Subject 2 out of 50:"))
Subject3 = float(input("Enter marks of Subject 3 out of 50:"))

Total = Subject1 + Subject2 + Subject3
Average = (Subject1 + Subject2 + Subject3) / 3

print ("Total marks:" , Total)
print ("Average marks:" , Average)

Percentage= Total / 150 * 100
print ("Percentage:" , Percentage)
if Percentage >= 80:
    print ("Grade A")
elif Percentage >= 70 and Percentage<=79:
    print("Grade B")
elif Percentage >=60 and Percentage<= 69:
    print ("Grade C")
elif Percentage >=50 and Percentage<= 59:
    print ("Grade D")
elif Percentage >=40 and Percentage<= 49:
    print ("Grade E")
else :
    print ("Grade R")    

