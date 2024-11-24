a=int(input("Enter number:- "))
rev=0
while a!=0:
    num=a%10
    rev=(rev*10)+num
    a//=10
print("reverse= ",rev)

# count=1
# n=int(input())
# while(count!=n+1):
#     print(count)
#     count+=1

s=input()
a=[]
for i in s:
    if i.isupper():
        a.append(i)
print(a)