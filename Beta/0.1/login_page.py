from tkinter import *
from tkinter import messagebox
import firebase_login_handler
import common_passwords_extractor

# WINDOW SETTINGS
wn = Tk()

wn.resizable(width=False, height=False)


# COMMANDS

# GET LOGIN DETAILS
def get_login_info():
    global password_entry

    # GETTING VALUES OF PASSWORD AND USERNAME
    password = password_entry.get()
    email = email_entry.get()

    # LOGGING IN
    login_result = firebase_login_handler.login(email,password)

    # CHECKING IF IT LOGGED IN
    if login_result == 1:
        messagebox.showinfo(title="Info Message", message="Login Successful")
    else:
        messagebox.showerror(title="Error 401", message="Invalid password or email")


def send_sign_up_info():
    # GETTING VALUES OF PASSWORD AND USERNAME
    password = password_entry.get()
    email = email_entry.get()


    # CHECK IF EMAIL AND PASSWORD ARE THE SAME
    if email == password:
        messagebox.showerror(title="Error 402", message="Password and Email cannot be the same")
    else:
        # CHECKING IF THE PASSWORD IS IN A COMMON PASSWORD LIST
        print(common_passwords_extractor.common_passwords)
        if password in common_passwords_extractor.common_passwords:
            messagebox.showerror(title="Error 403", message="Password Found in common password list")

        else:
            # SENDING USERNAME AND PASSWORD TO FB
            signup_result = firebase_login_handler.sign_up(email, password)

            # CHECKING IF ACCOUNT CREATED
            if signup_result == 1:
                # SHOWING A POP UP
                messagebox.showinfo(title="Info Message", message="Account successfully created")
            else:
                messagebox.showerror(title="Error 400", message=f"Account with email {email} already exists.")




# UI

# TITLE
title23 = Label(wn, text="LOGIN/SIGN UP PAGE")
title23.grid(column=1, row=0)

# USERNAME
# LABEL
email_label = Label(wn, text="Email: ")
email_label.grid(column=0, row=1)

# ENTRY
email_entry = Entry(wn)
email_entry.grid(column=1, row=1)

# PASSWORD
# LABEL
password_label = Label(wn, text="Password: ")
password_label.grid(column=0, row=2)

# ENTRY
password_entry = Entry(wn, show="*")
password_entry.grid(column=1, row=2)

# LOGIN BUTTON
login_btn = Button(wn, text="Login", command=get_login_info)
login_btn.grid(column=1, row=3)

# LOGIN BUTTON
sign_up_btn = Button(wn, text="Sign Up", command=send_sign_up_info)
sign_up_btn.grid(column=1, row=4)

wn.mainloop()
