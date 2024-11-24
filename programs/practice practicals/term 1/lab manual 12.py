# WAP to display the number of vowels, consonants, uppercase, lowercase characters in string
string = input("Enter a line- ")

vowel=consonant=uppercase=lowercase=0

vowel_list= ['a','e','i','o','u','A','E','I','O','U']

for i in string:
    if i in vowel_list:
        vowel+=1
    if i not in vowel_list:
        consonant+=1
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1

print ("Number of Vowels- ",vowel )
print ("Number of Consonents- ", consonant)
print("Number of Uppercase letter- ",uppercase)
print("Number of lowercase letter- ",lowercase)



















