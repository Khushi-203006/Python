#WAP to perform following tasks
str= input("enter a word: ")
#word in sequesnce
for i in range (len(str)):
    print (str[i])
    
#word in reverse orders
for i in range (-1 , -len(str)-1 ,-1):
    print (str[i])

#reverse order
new = str[-1: :-1]
print(new)

#count of variable
letter = input("enter a letter: ")
count=0
for i in str:
    if i==letter:
        count+=1
        print(count, "letter")
    

