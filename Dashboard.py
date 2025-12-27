from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
import time
import ttkthemes
from tkinter import ttk

def clock():
    date = time.strftime('%d-%M-%Y')
    Ctime = time.strftime('%H:%M:%S')
    datelable.config(text=f'Date:{date}') 
    timelable.config(text=f'Time:{Ctime}')
    datelable.after(1000,clock)
    timelable.after(1000,clock)

count = 0
text = ''

def slider():
    global count,text
    if count==len(s):
        count = 0
        text = ''
    text =text+s[count]
    count+=1
    sliderlable.config(text=text)
    sliderlable.after(200,slider)

#GUI part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.title('Student Managment System')
root.geometry('1280x720+0+0')


#Date and Time 
dateimg = ImageTk.PhotoImage(file = 'Date.png')
timeimg = ImageTk.PhotoImage(file = 'clock.png')

datelable = Label(root,image=dateimg,font=('times new roman',20,'bold'),compound=LEFT)
timelable =Label(root,image=timeimg,font=('times new roman',20,'bold'),compound=LEFT)
clock()
datelable.grid(row=0,column=0)
timelable.grid(row=1,column=0)

#Slider
s= 'Student Management System'
sliderlable = Label(root,font=('times new roman',30,'bold','italic'),width=30)
sliderlable.grid(row=0,column=3)
slider()

# DB Button
dbbutton = ttk.Button(text='Connect to Database',cursor='hand2')
dbbutton.place(x=1050,y=0)

#Left Frame
Leftframe = Frame(root)
Leftframe.place(x=50,y=80,width=300,height=600)

# Left frame Buttons
logo= ImageTk.PhotoImage(file='graduates.png')
logolable = Label(Leftframe,image=logo)
logolable.grid(row=0,column=0)

#Buttons
AddButton = ttk.Button(Leftframe,text='Add Student',width=20,cursor='hand2')
SerButton = ttk.Button(Leftframe,text='Search Student',width=20,cursor='hand2')
delButton = ttk.Button(Leftframe,text='Delete Student',width=20,cursor='hand2')
upButton = ttk.Button(Leftframe,text='Update Student',width=20,cursor='hand2')
shButton = ttk.Button(Leftframe,text='Show Student',width=20,cursor='hand2')
ExButton = ttk.Button(Leftframe,text='Export Data',width=20,cursor='hand2')
ExiButton = ttk.Button(Leftframe,text='Eixt',width=20,cursor='hand2')

#Button placing
AddButton.grid(row=1,column=0,pady=20)
SerButton.grid(row=2,column=0,pady=20)
delButton.grid(row=3,column=0,pady=20)
upButton.grid(row=4,column=0,pady=20)
shButton.grid(row=5,column=0,pady=20)
ExButton.grid(row=6,column=0,pady=20)
ExiButton.grid(row=7,column=0,pady=20)

# Right Frame

rightframe = Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

#Scroll bar
scrollBarX =Scrollbar(rightframe,orient=HORIZONTAL)
scrollBarY =Scrollbar(rightframe,orient=VERTICAL)



#treeview
Student_Table = ttk.Treeview(rightframe,columns=('Id','Full Name','Mobile No.','E-Mail','Address','Gender','D.O.B','Added Date','Added Time'),xscrollcommand=scrollBarX.set)

scrollBarX.config(command=Student_Table.xview)
scrollBarY.config(command=Student_Table.yview)
scrollBarX.pack(fill=X,side=BOTTOM)
scrollBarY.pack(fill=Y,side=RIGHT)

Student_Table.pack(fill=BOTH,expand=1)

Student_Table.heading('Id',text='Id')
Student_Table.heading('Full Name',text='Full Name')
Student_Table.heading('Mobile No.',text='Mobile No.')
Student_Table.heading('E-Mail',text='E-Mail')
Student_Table.heading('Address',text='Address')
Student_Table.heading('Gender',text='Gender')
Student_Table.heading('D.O.B',text='D.O.B')
Student_Table.heading('Added Date',text='Added Date')
Student_Table.heading('Added Time',text='Added Time')

Student_Table.config(show='headings')


root.mainloop()