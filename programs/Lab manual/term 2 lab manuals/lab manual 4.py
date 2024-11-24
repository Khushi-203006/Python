#WAP to shift the negative integers to right and the positive integers to left
num = int(input("enter range: "))
a = []
for i in range(num):
    n = int(input("enter element: "))
    a.append(n)
print("original list: ", a)
a.sort(reverse = True)
print(a)
        
