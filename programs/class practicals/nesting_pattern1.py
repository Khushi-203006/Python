'''
for i in range(1,6):
    #x=i
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n')

n=int(input("Enter an integer:"))
for i in range(n,0,-1):
    #x=i
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n')
'''
n=int(input("Enter a number:"))


for i in range(0, n):
    num = 65
    for j in range(0, i+1):
        ch = chr(num)
        print(ch, end=" ")
        num = num + 1
    print("\r")



    
