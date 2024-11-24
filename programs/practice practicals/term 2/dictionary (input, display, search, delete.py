# WAP to create ,search and delete store product
a= {}
while True:
    name = input("\nenter product Id: ")
    if name == ".":
        break
    else:
        product = input ("enter product name: ")
        price = input ("eneter price (in rupees): ")
        a[name] = (product,price)
print(a)

search = input("enter product id of product which you are searching: ")
if search in a:
    print ("found")
    print(search,a[search])
else:
    print("not found")

delete = input("eneter product id of product you want to delete: ")
if delete in a:
    print("found: ")
    print(a.pop(delete))
else:
    print("not found: ")
print(name)
print (a)
        
            
        
    
