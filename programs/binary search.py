import pickle
import insert
import search
while True:
    print("1 for inserting data")
    print("2 for searching data")
    ch= int(input("choose from menu: "))
    if ch==1:
        insert()
    elif ch==2:
        search()
    elif ch==0:
        break

def insert():
    rollno = int(input("Enter roll no: "))
    name = input("Enter Name: ")
    marks = int(input("Enter marks: "))
    stud = {"Roll no":rollno ,"Name":name, "Marks":marks}
    file = open("E:/khushi/student.dat.txt","ab")
    pickle.dump(stud,f)
    f.close()


def search():
    f = open("E:/khushi/student.dat.txt","rb")
    flag=0
    while True:
        try:
            stud = pickle.load(f)
            if stud["Roll no"] == r:
                print("Roll no", stud["Roll no"])
                print("Name", stud["Name"])
                print("Marks", marks["Marks"])
                flag=1
        except EOFError:
            break
    if flag == 0:
        print("no record")
    f.close()


    
        
            
        

                      
    
