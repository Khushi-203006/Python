# '''
# <-------------LIST------------->
# 1) written in square brackets []
# 2) values are seperated by comma(,)
# 3) mutable means once created can be changed
# 4) multiple data types can be written

# fruit=["apple","mango","banana",12,14,45.22]
# print(fruit)
# print(type(fruit))
# print("-------------------------")
# a=["Ironman","Thor","Captain America","Hulk"]
# print(a[2])
# print(a[-2])
# print(a[1:3])
# print(a[0:4])
# print(a[:2])
# print(a[::3])
# print(a[::-1])
# print("-------------------------")
# for i in range(len(a)):
#     print(a[i])
# print("-------------------------")
# for i in a:
#     print(i)
# print("-------------------------")
# i=0
# while(i<len(a)):
#     print(a[i])
#     i+=1
# print("-------------------------")
# [print (i) for i in a]
# print("-------------------------")
# '''
# '''
# print("List function")
# 1. len
# 2. count
# 3. append
# 4. Insert
# 5. Remove
# 6. Pop
# 7. Copy
# 8. Index
# 9. Extend
# 10.Reverse
# 11.Sort
# 12.Clear
# '''
# '''
# a=["Ironman","Thor","Captain America","Hulk","Thor","Ironman"]
# print(a)
# print(len(a))
# print("------------------------------")
# print(a.count("Thor"))
# print(a.count("Hulk"))
# print("------------------------------")
# a.append("Thor")
# print(a)
# a.append("Spiderman")
# print(a)
# print("------------------------------")
# a.insert(1,"Spiderman")
# print(a)
# print("------------------------------")
# a.remove("Thor")
# print(a)
# print("------------------------------")
# print(a.pop(4))
# print (a)
# print("------------------------------")
# b=[]
# print(b)
# b=a.copy()
# print(b)
# print("------------------------------")
# print(a.index("Thor"))
# print("------------------------------")
# c= ["Thor","Captain america"]
# a.extend(c)
# print(a)
# print("------------------------------")
# a.reverse()
# print (a)
# print("------------------------------")
# a.sort()
# print(a)
# print("------------------------------")
# a.clear()
# print(a)
# '''
# '''
# print("List comprehension")
# l1=[]
# for i in range(10):
#     n=int(input("Enter number: "))
#     l1.append(n)
# l2=[i in l1]
# l3=[i for i in l1 if i>45]
# print("L1= ",l1)
# print("L2= ",l2)
# print("L3= ",l3)
# '''
# a=["Rose","Rachel","Monica","Joe"]
# print("Original list= ",a)
# #WAP to swap first and fourth element
# temp = a[0]
# a[0] = a[3]
# a[3] = temp
# print (a)
# a[1],a[2]=a[2],a[1]
# print(a)
# #WAP to add new value at 2nd position
# a.insert(2,"Jake")
# print(a)
# #WAP to delete value from 3rd position
# a.pop(3)
# print(a)
# print("----------------------------------")
# b=[1,2,60,22]
# print("Original list= ",b)
# #WAP a program to multiply all numbers in list
# mul=1
# for i in b:
#     mul*=i
# print("Multiplication = ",mul)
# #WAP to get the largest element of list
# max_num = b[0]
# for i in range(len(b)):
#     if(max_num<b[i]):
#         max_num=b[i]
# print("Maximum number is ",max_num)
# #WAP to get smallest element of list
# min_num = b[0]
# for i in range(len(b)):
#     if(min_num>b[i]):
#         min_num=b[i]
# print("Minimum number is ",min_num)


l1=[1,2,3,4]
l2=[2,3,4]
print(l1+l2)





















