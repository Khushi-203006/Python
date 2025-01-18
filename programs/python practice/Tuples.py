'''
Tuples are collection of ordered and un-mutable data.
-> For tuples no brackets are mandatory.
-> By choice one can use paranthese.
-> The value inside a tuple cannot be changed.
-> Multiple datatypes can be written inside a tuples.
'''
'''
a="apple","mango","banana"
b=("apple","mango","banana")
print(a,type(a))
print(b,type(b))
print("---------------------------------------")
print("Slicing in tuple")
a= ("Oneplus","Vivo","Redmi","Samsung","Nokia")
print(a[1:3])
print(a[:])
print(a[::-1])
print(a[::2])
print("---------------------------------------")
print("Iteration in tuple")
for i in a:
    print(i)
print("---------------------------------------")
for i in range(len(a)):
    print(a[i])
print("---------------------------------------")
i=0
while(i<len(a)):
    print (a[i])
    i+=1
print("---------------------------------------")
'''
'''
print("Conversion of tuples and tuples function")
a= ("Oneplus","Vivo","Redmi")
print("Before conversion: ",type(a))

a=list(a)
print("After conversion: ",type(a))
a.append("Vivo")
print(a)
a=tuple(a)
print("After conversion: ",type(a))
print(a)
print(a.count("Redmi"))
print(a.index("Vivo"))
print(len(a))
'''





















