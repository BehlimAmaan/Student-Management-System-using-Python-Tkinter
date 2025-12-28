from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox
import pymysql

def clock():
    date = time.strftime('%d-%M-%Y')
    Ctime = time.strftime('%H:%M:%S')
    datelable.config(text=f'Date:{date}') 
    timelable.config(text=f'Time:{Ctime}')
    # datelable.after(1000,clock)
    timelable.after(300,clock)

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

#Database connection 
def db_connect():
    def connect():
        global mycursor,conn
        try:
            conn = pymysql.connect(host='localhost', user='root', password='Ammar@1240')
            mycursor=conn.cursor()
            messagebox.showinfo('Succes','Database connection is successful',parent=dbroot)
        except:
            messagebox.showerror('Error','Invalid Credentials',parent=dbroot)
        dbroot.destroy()
        try:
            query = 'Create Database student_management_system'
            mycursor.execute(query)
            query = 'use student_management_system'
            mycursor.execute(query)
            query = '''
            CREATE TABLE IF NOT EXISTS student (
                Id INT NOT NULL PRIMARY KEY,
                Name VARCHAR(100) NOT NULL,
                Mobile VARCHAR(10),
                Mail varchar(100),
                Address VARCHAR(100),
                Gender VARCHAR(10),
                DOB VARCHAR(20) NOT NULL,
                Date VARCHAR(20),
                Time VARCHAR(20)
            )
            '''
            mycursor.execute(query)
        except:
            query ='use student_management_system'
            mycursor.execute(query)
            query =''
        AddButton.config(state=NORMAL)
        SerButton.config(state=NORMAL)
        delButton.config(state=NORMAL)
        upButton.config(state=NORMAL)
        shButton.config(state=NORMAL)
        ExButton.config(state=NORMAL)
        ExiButton.config(state=NORMAL)

    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('500x300+730+230')
    dbroot.title('Database Connection')
    dbroot.resizable(0,0)
    # Tags 
    hostlable = Label(dbroot,text='  Host Name:',font=('arial',20,'bold'))
    userlable = Label(dbroot,text='  User Name:',font=('arial',20,'bold'))
    passwordlable = Label(dbroot,text='  Password:',font=('arial',20,'bold'))

    hostlable.grid(row=0,column=0,pady=20)
    userlable.grid(row=1,column=0,pady=20)
    passwordlable.grid(row=2,column=0,pady=20)

    # Entry feild
    hostentry = Entry(dbroot,font=('times new roman',20,'bold'),width=15,bd=2)
    userentry = Entry(dbroot,font=('times new roman',20,'bold'),width=15,bd=2)
    passentry = Entry(dbroot,font=('times new roman',20,'bold'),width=15,bd=2)

    hostentry.grid(row=0,column=1,padx=40,pady=20)
    userentry.grid(row=1,column=1,padx=40,pady=20)
    passentry.grid(row=2,column=1,padx=40,pady=20)

    #Connect Button
    conn = ttk.Button(dbroot,text='Connect',command=connect,width=20,cursor='hand2')
    conn.grid(row=3,columnspan= 2,pady=10)

#Add student
def add():
    def addtodb():
        currentdate = time.strftime('%d-%M-%Y')
        currenttime = time.strftime('%H:%M:%S')
        if identry.get()=='' or nameentry.get()=='' or mobileentry.get()=='' or mailentry.get()==''or genderentry.get()=='' or Addressentry.get()=='' or dobentry.get()=='' :
            messagebox.showerror('Empty','No Feild should be Empty',parent=addwindow)
        else:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(identry.get(),nameentry.get(),mobileentry.get(),mailentry.get(),Addressentry.get(),genderentry.get(),dobentry.get(),currentdate,currenttime))
        conn.commit()
        result = messagebox.askyesno('Confirm','Data added Succesfully Do You want to clear form',parent=addwindow)
        if result:
            identry.delete(0,END)
            nameentry.delete(0,END)
            mobileentry.delete(0,END)
            mailentry.delete(0,END)
            Addressentry.delete(0,END)
            genderentry.delete(0,END)
            dobentry.delete(0,END)
        else:
            pass
        query = 'select *from student'
        mycursor.execute(query)
        Student_Table.delete(*Student_Table.get_children())
        fetcheddata = mycursor.fetchall()
        for data in fetcheddata:
            listdata = list(data)
            Student_Table.insert('',END,values=listdata)
    addwindow = Toplevel()
    addwindow.grab_set()
    addwindow.resizable(0,0)
    addwindow.title('Add Student')

    #ID
    idlable = Label(addwindow,text='Id',font=('times new roman',20,'bold'))
    idlable.grid(row=0,column=0,sticky=W)
    identry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    identry.grid(row=0,column=1,padx=40,pady=20)

    #Name
    namelable = Label(addwindow,text='Name',font=('times new roman',20,'bold'))
    namelable.grid(row=1,column=0,sticky=W)
    nameentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    nameentry.grid(row=1,column=1,padx=40,pady=20)

    #Mobile
    mobilelable = Label(addwindow,text='Phone',font=('times new roman',20,'bold'))
    mobilelable.grid(row=2,column=0,sticky=W)
    mobileentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    mobileentry.grid(row=2,column=1,padx=40,pady=20)

    #Mail
    maillable = Label(addwindow,text='E-Mail',font=('times new roman',20,'bold'))
    maillable.grid(row=3,column=0,sticky=W)
    mailentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    mailentry.grid(row=3,column=1,padx=40,pady=20)

    #Address
    Addresslable = Label(addwindow,text='Address',font=('times new roman',20,'bold'))
    Addresslable.grid(row=4,column=0,sticky=W)
    Addressentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    Addressentry.grid(row=4,column=1,padx=40,pady=20)

    #Gender
    Genderlable = Label(addwindow,text='Gender',font=('times new roman',20,'bold'))
    Genderlable.grid(row=5,column=0,sticky=W)
    genderentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    genderentry.grid(row=5,column=1,padx=40,pady=20)

    #DOB
    doblable = Label(addwindow,text='D.O.B',font=('times new roman',20,'bold'))
    doblable.grid(row=6,column=0,sticky=W)
    dobentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    dobentry.grid(row=6,column=1,padx=40,pady=20)

    #Add Student button
    studebutton = ttk.Button(addwindow,text='Add Student',width=20,cursor='hand2',command=addtodb)
    studebutton.grid(row=7, columnspan=2, pady=20)

#Search  Student
def search():
    def search_student():
        query= 'select *from student where Id=%s or Name=%s or Mobile=%s or Mail=%s or Gender=%s or DOB=%s'
        mycursor.execute(query,(identry.get(),nameentry.get(),mobileentry.get(),mailentry.get(),genderentry.get(),dobentry.get()))
        Student_Table.delete(*Student_Table.get_children())
        fetcheddata = mycursor.fetchall()
        for data in fetcheddata:
            Student_Table.insert('',END, values=data)
    addwindow = Toplevel()
    addwindow.title('Search Student')
    #ID
    idlable = Label(addwindow,text='Id',font=('times new roman',20,'bold'))
    idlable.grid(row=0,column=0,sticky=W)
    identry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    identry.grid(row=0,column=1,padx=40,pady=20)

    #Name
    namelable = Label(addwindow,text='Name',font=('times new roman',20,'bold'))
    namelable.grid(row=1,column=0,sticky=W)
    nameentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    nameentry.grid(row=1,column=1,padx=40,pady=20)

    #Mobile
    mobilelable = Label(addwindow,text='Phone',font=('times new roman',20,'bold'))
    mobilelable.grid(row=2,column=0,sticky=W)
    mobileentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    mobileentry.grid(row=2,column=1,padx=40,pady=20)

    #Mail
    maillable = Label(addwindow,text='E-Mail',font=('times new roman',20,'bold'))
    maillable.grid(row=3,column=0,sticky=W)
    mailentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    mailentry.grid(row=3,column=1,padx=40,pady=20)

    #Gender
    Genderlable = Label(addwindow,text='Gender',font=('times new roman',20,'bold'))
    Genderlable.grid(row=5,column=0,sticky=W)
    genderentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    genderentry.grid(row=5,column=1,padx=40,pady=20)

    #DOB
    doblable = Label(addwindow,text='D.O.B',font=('times new roman',20,'bold'))
    doblable.grid(row=6,column=0,sticky=W)
    dobentry = Entry(addwindow,font=('times new roman',20,'bold'),width=25,bd=2)
    dobentry.grid(row=6,column=1,padx=40,pady=20)

    #Search Student button
    studebutton = ttk.Button(addwindow,text='Search Student',width=20,cursor='hand2',command=search_student)
    studebutton.grid(row=7, columnspan=2, pady=20)

#Delete Student
def del_student():
    indexing = Student_Table.focus()
    print(indexing)
    content =Student_Table.item(indexing)
    content_id=content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    conn.commit()
    messagebox.showinfo('Success',f'id {content_id} Deleted successfully')
    query = 'select *from student'
    mycursor.execute(query)
    Student_Table.delete(*Student_Table.get_children())
    fetchdata = mycursor.fetchall()
    for data in fetchdata:
        Student_Table.insert('',END,values=data)

# Show Student
def show():
    query = 'select *from student'
    mycursor.execute(query)
    Student_Table.delete(*Student_Table.get_children())
    fetchdata = mycursor.fetchall()
    for data in fetchdata:
        Student_Table.insert('',END,values=data)


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
dbbutton = ttk.Button(text='Connect to Database',command=db_connect,cursor='hand2')
dbbutton.place(x=1050,y=0)

#Left Frame
Leftframe = Frame(root)
Leftframe.place(x=50,y=80,width=300,height=600)

# Left frame Buttons
logo= ImageTk.PhotoImage(file='graduates.png')
logolable = Label(Leftframe,image=logo)
logolable.grid(row=0,column=0)

#Buttons
AddButton = ttk.Button(Leftframe,text='Add Student',width=20,cursor='hand2',state=DISABLED,command=add)
SerButton = ttk.Button(Leftframe,text='Search Student',width=20,cursor='hand2',state=DISABLED,command=search)
delButton = ttk.Button(Leftframe,text='Delete Student',width=20,cursor='hand2',state=DISABLED,command=del_student)
upButton = ttk.Button(Leftframe,text='Update Student',width=20,cursor='hand2',state=DISABLED)
shButton = ttk.Button(Leftframe,text='Show Student',width=20,cursor='hand2',state=DISABLED,command=show)
ExButton = ttk.Button(Leftframe,text='Export Data',width=20,cursor='hand2',state=DISABLED)
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