from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import ttkthemes
from tkinter import ttk

def login():
    if userentry.get()=='' or passentry.get()=='':
        messagebox.showerror('Error', 'Entry Feild Should not be Empty')
    elif userentry.get()=='Amaan' and passentry.get()=='amaan@123':
        messagebox.showinfo('Login Successfull','Welcome To The Dashboard')
        window.destroy()
        import Dashboard
    else:
        messagebox.showwarning('Invalid','Username or Password does not match')
        


# Creating Window 
window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('radiance')
window.title("Student Management Sysyem")
window.geometry('1280x700+0+0')

#Adding Background Image 
bgimage=ImageTk.PhotoImage(file='bg1.jpg')
bglable=Label(window,image=bgimage,bg='white')
bglable.place(x=0,y=0)

#Creating Frame in window
LoginFrame= Frame(window,bg='white')
LoginFrame.place(x=400,y=160)

# Frame Logo
logoimage=ImageTk.PhotoImage(file='logomain.png')
logolable = Label(LoginFrame,image=logoimage,bg='white')
logolable.grid(row=0,column=0,columnspan=2)

#Username 
userimg=PhotoImage(file='user.png')
userlable = Label(LoginFrame,image=userimg,text='Username',font=('times new roman',20,'bold'),compound=LEFT,bg='white')
userlable.grid(row=1,column=0,padx=10,pady=20)

#User Entry
userentry = Entry(LoginFrame,font=('times new roman',20,'bold'))
userentry.grid(row=1,column=1)

#pass Entry
passentry = Entry(LoginFrame,font=('times new roman',20,'bold'))
passentry.grid(row=2,column=1)

#Password
passwordimg = PhotoImage(file='locked.png')
passwordlable=Label(LoginFrame,image=passwordimg,text='Password',font=('times new roman',20,'bold'),compound=LEFT,bg='white')
passwordlable.grid(row=2,column=0)

#Login Button
Loginbutton = ttk.Button(LoginFrame,text='Login',width=15,command=login,cursor='hand2')
Loginbutton.grid(row=3, column=1,pady=20)

#Window on a loop 
window.mainloop()