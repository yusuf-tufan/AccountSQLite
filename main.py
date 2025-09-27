import tkinter
from tkinter import *
import sqlite3
from tkinter import messagebox
import hashlib


#This is used before creating a table.
#cursor.execute("""DROP TABLE IF EXISTS ACCOUNTS""")
#cursor.execute("""CREATE TABLE ACCOUNTS
#(name text,surname text,username text,password text)
#""")


#encrypt password with hashlib
def password_hashl(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Create Account
def create_account():

    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()


    name=enter_name.get()
    surname=enter_surname.get()
    username0=username2.get()
    password0=password2.get()
    cursor.execute(f"""SELECT 1 from ACCOUNTS WHERE username='{username0}'""")
    user=cursor.fetchone()
    if len(name)==0 or len(surname)==0:
        messagebox.showinfo(message='Please enter all informations',title='Warning')
    elif len(username0)==0 or len(password0)==0:
        messagebox.showinfo(message='Please enter all informations', title='Warning')
    else:
        password0=password_hashl(password0)
        if user:
            messagebox.showinfo(message='This user already exists',title='Error')
        else:
            try:
                cursor.execute(f"""INSERT INTO ACCOUNTS VALUES ('{name}','{surname}','{username0}','{password0}') """)
                conn.commit()
                messagebox.showinfo(message='User created', title='message')
                btn_signUp.config(state='disabled')
            except sqlite3.IntegrityError:
                messagebox.showinfo(message='This user already exists',title='Error')
    conn.close()

#Login Account
def login():
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    user_username = username.get()
    user_password=password.get()
    user_password = password_hashl(user_password)
    cursor.execute(f"""SELECT 1 from ACCOUNTS WHERE username='{user_username}' AND password='{user_password}'""")
    user=cursor.fetchone()
    if len(user_username)==0 or len(user_password)==0:
        messagebox.showinfo(message='Please enter your username and password.',title='Warning')
    else:
        if user :
            lbl_result.config(text='Logged In',font=('Verdana',10,'bold'),fg='red')
            lbl_result.grid(row=8, column=1, pady=(5, 5))
            btn_login.config(state='disabled')
        else:
            messagebox.showinfo(message='Wrong username or password!',title='Wrong')

    conn.close()

#window transitions
def home_page():
    window.destroy()
    window1.deiconify()

#window of sign up
def signUp():
    global window,enter_name,enter_surname,username2,password2,lbl_signup_result,btn_signUp

    def password_see():
        if password2.cget('show') == '*':
            password2.config(show='')
            password_show_hide2.config(image=img_btn_hide)
        else:
            password2.config(show='*'),
            password_show_hide2.config(image=img_btn_show)
    window1.withdraw()
    window=tkinter.Toplevel()
    window.config(bg='light blue')
    window.title('Sign Up Page')
    window.geometry("300x400")
    window.resizable(False, False)


    lbl_name = Label(window,text='Name:')
    lbl_name.config(bg='light blue')
    lbl_name.grid(row=0, column=0, padx=(50, 0), pady=(5, 5))

    enter_name = Entry(window,width=15,font=('Arial',9,'bold'))
    enter_name.configure()
    enter_name.grid(row=0, column=1)

    enter_name.focus_set()

    lbl_surname = Label(window,text='Surname:',bg='light blue')
    lbl_surname.grid(row=2, column=0, padx=(50, 0))

    enter_surname = Entry(window,width=15,font=('Arial',9,'bold'))
    enter_surname.grid(row=2, column=1)

    lbl_username2 = Label(window,text='Username:',bg='light blue')
    lbl_username2.grid(row=3, column=0, padx=(50, 0), pady=(5, 5))

    username2 = Entry(window,width=15,font=('Arial',9,'bold'))
    username2.configure()
    username2.grid(row=3, column=1)

    lbl_password2 = Label(window,text='Password:',bg='light blue')
    lbl_password2.grid(row=4, column=0, padx=(50, 0))

    img_btn_show = PhotoImage(file='images/show.png')
    img_btn_show = img_btn_show.subsample(7)
    img_btn_hide = PhotoImage(file='images/hide.png')
    img_btn_hide = img_btn_hide.subsample(7)

    passw_var2=StringVar()
    password2 = Entry(window,width=15,textvariable=passw_var2,show='*',font=('Arial',9,'bold'))
    password2.grid(row=4, column=1)

    password_show_hide2 = Button(window,image=img_btn_show, command=password_see)
    password_show_hide2.grid(row=4, column=4, padx=(3, 0))

    btn_signUp = Button(window,text='  Sign Up  ', width=11,command=create_account)
    btn_signUp.grid(row=5, column=1, pady=(5, 5))

    btn_home = Button(window,text='  Login Page  ', width=11,command=home_page)
    btn_home.grid(row=6, column=1, pady=(5, 5))

#password show and hide
def show_hide():
    if password.cget('show')=='*':
        password.config(show='')
        password_show_hide.config(image=img_btn_hide)
    else:
        password.config(show='*'),
        password_show_hide.config(image=img_btn_show)

def delete_account():

    delete_username=username.get()
    delete_passw=password.get()
    delete_passw=password_hashl(delete_passw)

    yes_no=messagebox.askyesno('Approval',f"Delete user {delete_username}? ")
    if not yes_no:
        return

    conn=sqlite3.connect('accounts.db')
    cursor=conn.cursor()
    cursor.execute(f"""DELETE FROM ACCOUNTS WHERE username='{delete_username}' AND password='{delete_passw}'""")
    conn.commit()
    if cursor.rowcount>0:
        messagebox.showinfo(message='Account Deleted',title='Info')
    else:
        messagebox.showinfo(message='Account Not Found',title='Info')

    cursor.close()


#window of main
window1=Tk()
window1.title('Account App')
window1.geometry("300x400")
window1.config(bg='light blue')
window1.resizable(False,False)

lbl_username=Label(text='Username:')
lbl_username.config(bg='light blue')
lbl_username.grid(row=0,column=0,padx=(50,0),pady=(5,5))

username=Entry(width=15)
username.config(font=('Arial',9,'bold'))
username.grid(row=0,column=1)

username.focus_set()

lbl_password=Label(text='Password:')
lbl_password.config(bg='light blue')
lbl_password.grid(row=2,column=0,padx=(50,0))

passw_var=StringVar()
password=Entry(width=15,textvariable=passw_var,show='*',font=('Arial',9,'bold'))
password.grid(row=2,column=1)

btn_login=Button(text='  Login  ',width=11,command=login)
btn_login.grid(row=3,column=1,pady=(5,5))

btn_signup=Button(text='  Sign Up  ',width=11,command=signUp)
btn_signup.grid(row=4,column=1,pady=(5,5))

img_btn_show=PhotoImage(file='images/show.png')
img_btn_show=img_btn_show.subsample(7)
img_btn_hide=PhotoImage(file='images/hide.png')
img_btn_hide=img_btn_hide.subsample(7)

password_show_hide=Button(image=img_btn_show,command=show_hide)
password_show_hide.grid(row=2,column=3,padx=(3,0))

lbl_result=Label(text='')

delete_btn=Button(text='DELETE ACCOUNT',bg='red',command=delete_account)
delete_btn.grid(row=8,column=1,pady=(60,0))


window1.mainloop()