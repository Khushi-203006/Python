#WAP to perform following task

print ("choice 1 - palindrome")
print ("choice 2 - count words in string")
print ("choice 3 - count substring")
print ("choice 4 - count words starting with a vowel")

ch= int(input("enter choice: - "))

if ch==1:
    #WAP to check palindrome
        string = input("enter a word: ")
        length = len(string)
        first = 0
        last = length -1 
        status = 1
        while(first<last):
            if(string[first]==string[last]):
                first=first+1
                last=last-1
            else:
               status = 0
               break
        if(status):
            print("It is a palindrome ")
        else:
            print("It is not a palindrome ")

if ch==2:
         #wap to count words
        sent=input("enter a sentence:-  ")
        count=len(sent.split())
        print("no of words="+ str(count))

elif ch==3:
        #WAP to count substring
        str1 = input("enter a sentence:- ")
        substring= input("enter substring:- ")

        count = (str1.count(substring))
        print ("no of subsrting:-", count)

elif ch==4:
        #WAP to display the occurrence of words starting with a vowel
        str= input("enter a sentence: - ")
    
        count=0
        word=str.split()
        for i in word:
            if i[0] in "aeiouAEIOU":
                count+=1
        print ("no of word starting with vowel are:- ", count , end=' ')














