#Write a program that checks in the range 1……100

for i in range (1,101):
    if i % 3==0:
        print("Fizz")
    
    elif i % 5 ==0:
        print("Buzz")

    elif i % 15 ==0:
        print ("FizzBuzz")

    else :
        print(i)
        

    

