#wap to print the digit's lenght
digit = int(input("Enter number:- "))
count =0
while(digit!=0):
    rem = digit%10
    count+=1
    digit=digit//10
print("Number conatins  ",count," digits.")
    
