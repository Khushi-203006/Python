# def rem(s,k):
#     lenght=len(s)
#     if(lenght<=k):
#         return s
#     else:
#         return s[0:k]+s[k+1:]


# s=input("")
# k=int(input(""))
# print(rem(s,k))

def search(a,n,k):
    count=0
    for i in a:
        if (i==n):
            count+=1
    if(count==k):
        return True
    else:
        return False


a=[1,2,3,4,4,3]
n=2
k=1
print(search(a,n,k))