#WAP to compute simple interest and compound interest.

Principle = float(input("Enter Principle :  "))
Rate = float(input("Enter Rate :  "))
Time = float(input("Enter Time :  "))

SimpleIntrest = (Principle * Rate * Time) / 100
CompoundIntrest = Principle * (1 + (Rate/ 100 )) ** Time

print( "Simple Intrest" , SimpleIntrest)
print( "Compound Intrest" , CompoundIntrest)
