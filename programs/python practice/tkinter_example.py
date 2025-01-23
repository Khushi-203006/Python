from tkinter import *
root = Tk()
root.geometry('500x500')
root.minsize(500,500)
root.maxsize(500,500)

#l1 = Label(text='''This is GUI program''',
#         bg='skyblue',fg='red',
#          font='conicsams 20 bold',
#          pady=100, borderwidth=100, relief=GROOVE)
#l1.pack()

l2=Label(text='First number:')
l2.grid(row=0,column=0)
#l2.pack()---->No need to use pack when grid is used
l3=Label(text='Last number: ')
l3.grid(row=1,column=0)
l4=Label(text='Result:')
l4.grid(row=2,column=0)
inp1=Entry(width=50,borderwidth=5,relief=GROOVE)
inp1.grid(row=0,column=1)
inp2=Entry(width=50,borderwidth=5,relief=GROOVE)
inp2.grid(row=1,column=1)
inp3=Entry(width=50,borderwidth=5,relief=GROOVE)
inp3.grid(row=2,column=1)
btn = Button(text="Click Here")
btn.grid(row=3,column=1)

root.mainloop()
