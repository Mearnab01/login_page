from tkinter import *
from tkinter import messagebox
import subprocess

def open_signup_page():
    subprocess.Popen(['python', 'signup.py'])
    #print("open signup")

root = Tk()
root.title("Sign In Page")
root.geometry('925x500+300+200')
root.config(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file='signin.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='HELLO',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("Try Agian","Invalid Name or Password")

#-------------------------------------------------------
def on_enter_username(event):
    if user.get() == 'Username':
        user.delete(0, END)
        user.config(fg='black')

def on_leave_username(event):
    if user.get() == '':
        user.insert(0, 'Username')
        user.config(fg='gray')

user = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=107)
#-------------------------------------------------------

def on_enter_password(event):
    if code.get() == 'Password':
        code.delete(0, END)
        code.config(show='*', fg='black')

def on_leave_password(event):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show='', fg='gray')

code = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=177)
#--------------------------------------------------------------------------
Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0,command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=open_signup_page)
sign_up.place(x=215, y=270)

root.mainloop()
