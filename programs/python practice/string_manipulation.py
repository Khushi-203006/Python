print("""
1. lenght
2. count
3. upper
4. lower
5. index
6. capitalize
7. casefold
8. find
9. format
10.center
11.isalnum--------------
12.isalpha              |
13.isdecimal            |  
14.isdigit              |
15.isnumeric            |----> value return will be true or false
16.islower              | 
17.isupper              |  
18.isspace              |
19.istitle--------------
20.endwith
21.startswith
22.swapcase
23.strip
24.split
25.ljust
26.rjust
27.replace
28.rindex
29.rfind
""")
a="hello World"
print(type(a))
print(a)
print("--------------------------------")
#1
print("lenght= ",len(a))
print("--------------------------------")
#2
print("count of l= ",a.count("l"))
print("--------------------------------")
#3
print("upper= ",a.upper())
print("--------------------------------")
#4
print("Lower= ",a.lower())
print("--------------------------------")
#5
print("Index of l= ",a.index('l'))
print("Index of o= ",a.index('o'))
print("Index of d= ",a.index('d'))
print("--------------------------------")
#6
print("Capitilized= ",a.capitalize())
print("--------------------------------")
#7
print("Casefold= ",a.casefold()) 
print("--------------------------------")
#8
print("Find l = ",a.find('l'))
print("--------------------------------")
#9
b="My computer want to say {}"
print(b.format(a))
print("--------------------------------")
#10
print(a.center(20))
print(b.center(30,'*'))
c= "HELLO1234"
d= "1.234"
e= " "
f= "hello"
g= "@"
print("--------------------------------")
#11--> if all characters are alphanumeric
print(c,c.isalnum())
print(d,d.isalnum())
print(e,e.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())
print("--------------------------------")
#12--> if all characters are alphabets
print(c,c.isalpha())
print(d,d.isalpha())
print(e,e.isalpha())
print(f,f.isalpha())
print(g,g.isalpha())
print("--------------------------------")
#13 and 14--> if all characters in decimal---> is same as isnumeric
print(c,c.isdecimal())
print(d,d.isdecimal())
print(e,e.isdecimal())
print(f,f.isdecimal())
print(g,g.isdecimal())
h="123456"
print(h,h.isdecimal())
print("--------------------------------")
#15--> if all characters are digits
print(c,c.isdigit())
print(d,d.isdigit())
print(e,e.isdigit())
print(f,f.isdigit())
print(g,g.isdigit())
print(h,h.isdigit())
print("--------------------------------")
#16--> if all characters are lower
i= "HELLO"
print(c,c.islower())
print(d,d.islower())
print(e,e.islower())
print(f,f.islower())
print(g,g.islower())
print(i,i.islower())
print("--------------------------------")
#17--> if all characters are upper
print(c,c.isupper())
print(d,d.isupper())
print(e,e.isupper())
print(f,f.isupper())
print(g,g.isupper())
print(i,i.isupper())
print("--------------------------------")
#18--> if all characters are space
print(c,c.isspace())
print(d,d.isspace())
print(e,e.isspace())
print(f,f.isspace())
print(g,g.isspace())
print(i,i.isspace())
print("--------------------------------")
#19--> if all characters are title
j="Hello 123"
k= "HELLO Everyone"
print(c,c.istitle())
print(d,d.istitle())
print(e,e.istitle())
print(f,f.istitle())
print(g,g.istitle())
print(i,i.istitle())
print(j,j.istitle())
print(k,k.istitle())
print("--------------------------------")
#20--> returns true if it ends withgiven string
l = "Harry Potter"
print(l.endswith('r'))
print(l.endswith('P'))
print(l.endswith('t',6,9))
print("--------------------------------")
#21--> returns trueif it starts with given string
print(l.startswith("H"))
print(l.startswith("P"))
print(l.startswith("P",6,9))
print("--------------------------------")
#22--> lowercase becomes uppercase and vice versa
print(l.swapcase())
#23--> returns trimmed version
m = "     Harry Potter     "
n = "     ****Harry Potter .... "
print(m)
print(m.strip())
print(n)
print(n.strip("*,"))
print("--------------------------------")
#24--> split character with commas
o="#OOFD#BRB#OMW#TB"
p="Hello.my name is khushi.I am 18 years old."
print(o.split("#"))
print(o.split())
print(p.split("."))
print(p.split())
print("--------------------------------")
#25--> return left justification of string
print(l.ljust(20,"*"),"is my favoraite character")
print(l.ljust(20),"is my favoraite character")
print("--------------------------------")
#26--> return right justification of string
print("My favoraite character is",l.rjust(20))
print("My favoraite character is",l.rjust(20,"'"))
print("--------------------------------")
#27--> retrun a sting where a specific value is relaced
q="There are 4 best friend in harry potter."
print(q)
print(q.replace("4","3"))
print("--------------------------------")
#28-->  search the string and provide the index
print(q.rindex("friend"))
#print(q.rindex("friends"))---> will give error
print("--------------------------------")
#29--> find string return the index
print(q.rfind("potter")) 










