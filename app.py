from tkinter import *
from tkinter.cores import *
from tkinter import messagebox

window = Tk()
window.title ('Bem-Vindo')
window.geometry('800x600')
window.resizable(width=False, height=False)
window.iconbitmap('pointer_sign_location_direction_arrow_right_icon_258765.ico')
users = {'admin': 'admin'}
def user_sign_up (*args):
    typed_user = e_name.get()
    typed_password = e_password.get()
    
    if typed_user in users.keys():
        messagebox.showerror(title="Error", message="Username unavalable")
    else:
        users[typed_user] = typed_password
        messagebox.showinfo(title="Bem Vindo", message="Signed up successfully")

def user_sign_in(*args):
    typed_user = e_name.get()
    typed_password = e_password.get()
    
    if typed_user in users.keys():
        password = users[typed_user]
        if typed_password == password:
            messagebox.showinfo(title="Bem Vindo", message="Loged In")
        else:
            messagebox.showerror(title="Error", message="Wrong user or password")
    else:
        messagebox.showerror(title="Error", message="Wrong user or password")


up_frame = Frame(
    window,
    width=800,
    height=150,
    bg=cor1,
    relief='flat'
)
up_frame.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

down_frame = Frame(
    window,
    width=800,
    height=450,
    bg=cor1,
    relief='flat'
)
down_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


l_name = Label(
    up_frame,
    text="LOGIN",
    font=('Ivy 20'),
    bg=cor1,
    fg=cor4
)
l_line = Label(
    up_frame,
    text='',
    width=800,
    font=('Ivy 5'),
    bg=cor2,
    fg=cor4
)
l_user = Label(
    down_frame,
    text='User *',
    font='Ivy 14',
    bg=cor1,
    fg=cor4
)

e_name = Entry(
    down_frame,
    width=25,
    justify='left',
    font=("",13),
    highlightthickness=1,
    relief='solid'
)

l_password = Label(
    down_frame,
    text='Password *',
    font='Ivy 14',
    bg=cor1,
    fg=cor4
)

e_password = Entry(
    down_frame,
    width=25,
    show='*',
    justify='left',
    font=("",13),
    highlightthickness=1,
    relief='solid'
)

b_login = Button(
    down_frame,
    text="Login",
    width=39,
    height=2,
    font=('Ivy 8 bold'),
    bg=cor2,
    fg=cor1,
    relief=RAISED,
    command=user_sign_in
)

b_sign_up = Button(
    down_frame,
    text="Sign Up",
    width=10,
    height=1,
    font=('Ivy 8 bold'),
    bg=cor1,
    fg='blue',
    relief='flat',
    command=user_sign_up
)
window.bind("<Return>", user_sign_in)

l_name.place(x=30,y=20)
l_line.place(x=0, y=65)
l_user.place(x=35, y=20)
e_name.place(x=35, y=60)
l_password.place(x=35, y=120)
e_password.place(x=35, y=160)
b_login.place(x=15, y= 250)
b_sign_up.place(x=117, y= 295)


if __name__ == '__main__':
    window.mainloop()