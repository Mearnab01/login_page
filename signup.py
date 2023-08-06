#Create Sign Up Page
import platform
from tkinter import *
from tkinter import messagebox
import subprocess

def open_signin_page():
    subprocess.Popen(['python', 'signin.py'])

def on_enter_username(event):
    if user.get() == 'Username':
        user.delete(0, END)
        user.config(fg='black')

def on_leave_username(event):
    if user.get() == '':
        user.insert(0, 'Username')
        user.config(fg='gray')

def on_enter_password(event):
    if code.get() == 'Password':
        code.delete(0, END)
        code.config(show='*', fg='black')

def on_leave_password(event):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show='', fg='gray')
        
def on_enter_confirm_password(event):
    if confirm_code.get() == 'Confirm Password':
        confirm_code.delete(0, END)
        confirm_code.config(fg='black')

def on_leave_confirm_password(event):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')
        confirm_code.config(show='', fg='gray')

def sign_up_button_clicked():
    if user.get() == 'Username' or code.get() == 'Password' or confirm_code.get() == 'Confirm Password':
        messagebox.showerror('Error', 'Please fill in all fields.')
    elif code.get() != confirm_code.get():
        messagebox.showerror('Error', 'Passwords do not match.')
    else:
        messagebox.showinfo('Success', 'Your account has been created.')

root = Tk()
root.title("Sign Up Page")
root.geometry('925x500+300+200')
root.config(bg='#fff')
root.resizable(False, False)

def set_favicon(window, icon_path):
    if platform.system() == 'Windows':
        window.iconbitmap(icon_path)
favicon_path = ''
set_favicon(root, favicon_path)

img = PhotoImage(file='signup.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=107)
#---------------------------------------------------------------------
code = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=177)
#---------------------------------------------------------------------
confirm_code = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=210)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter_confirm_password)
confirm_code.bind('<FocusOut>', on_leave_confirm_password)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=237)
#-----------------------------------------------------------------------
Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0,command=sign_up_button_clicked).place(x=35, y=264)

label = Label(frame, text="Already have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=330)

sign_up = Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=open_signin_page)
sign_up.place(x=215, y=330)

root.mainloop()
