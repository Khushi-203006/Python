'''
Dictionary all to write in form of key and value
->Dictionary are enclosed inside curly brackets{}.
->Keys and values are separated by colon.
->Every key value pair is separated by a colon.
'''
'''
empo_data={"name":"john","age":24,"gender":"male"}
print(empo_data)
print("Age value: ",empo_data["age"])
print("Gender value: ",empo_data["gender"])

'''
stud={"name":"john","class":"6th","roll.no":23}
'''
for x in stud:
    print(x)
for x in stud:
    print(stud[x])
for x in stud.values():
    print (x)
for x,y in stud.items():
    print(x,"-",y)
'''
'''
x= stud.get("name")
print(x)

a=stud.items()
print (a)

b=stud.keys()
print(b)

c=stud.values()
print(c)

d=stud.copy()
print(d)

e=stud.setdefault("rollno",24)
print(e)

print(stud)

f = stud.pop("rollno")
print(f)

print(stud)
print("----------------------------------------------")
stud={"name":"john","class":"6th","roll.no":23}
stud_2 = {"name":"nancy","class":"6th","roll.no":24}

stud.update(stud_2)
print("new dictionary:- ",stud)

g = stud.popitem()
print(g)
print(stud)

print(stud_2)
print(stud_2.clear())
'''
'''
print("Nested dictionary")

emp = {1:{"name":"John","age":24},
       2:{"name":"Lisa","age":25}}
print(emp)

print(emp[2]["age"]) 
'''
'''
a = {"a":12,"b":23,"c":6,"d":91,"e":45}
a=sorted(a.values())
print(a)
'''
'''
a={}
for i in range(1,16):
    a[i]=i*i
print(a)
'''
'''
a = {"a":12,"b":23,"c":6,"d":91,"e":45}
product = 1
for i in a:
    product*= a[i]
print(product)
'''
a = {12:"a",56:"b",23:"c",48:"d",91:"e"}
a = sorted(a.keys())
print(a)






















