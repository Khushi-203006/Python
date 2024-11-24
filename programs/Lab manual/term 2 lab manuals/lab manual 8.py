#WAP to input countries and their capital and currency and also search particular country
a = {}
while True:
    country = input("\ncountry name: ")
    if country == '.':
        break
    else:
        capital = input("capital name: ")
        currency = input("currency name: ")
        a[country] = (capital,currency)
        print(a)
    
print("country name\tcapital name\tcurrencey")
for i in a:
    print(i, "\t\t", a[i][0], "\t\t", a[i][1])
print()

search= input("enter country name you are searching for: ")
if search in a:
       print("record found")
       print(search, a[search])
else:
       print("not found")
