from tkinter import *
from tkinter import messagebox
import firebase_login_handler
import common_passwords_extractor
import home_page
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# WINDOW SETTINGS
wn = Tk()

wn.resizable(width=False, height=False)


# COMMANDS

# ======================================================================================================

# GET LOGIN DETAILS
def get_login_info():
    global password_entry

    # GETTING VALUES OF PASSWORD AND USERNAME
    password = password_entry.get()
    email = email_entry.get()

    # LOGGING IN
    login_result = firebase_login_handler.login(email, password)

    # CHECKING IF IT LOGGED IN
    if login_result == 1:
        messagebox.showinfo(title="Info Message", message="Login Successful")
        # OPENING HOME PAGE
        home_page.home_page_screen()
    else:
        messagebox.showerror(title="Error 401", message="Invalid password or email")


# =========================S=I=G=N==U=P==F=U=N=C=T=I=O=N================================================
# SIGN UP FUNCTION
def send_sign_up_info():
    # GETTING VALUES OF PASSWORD AND USERNAME
    password = password_entry.get()
    email = email_entry.get()

    # CHECK IF EMAIL AND PASSWORD ARE THE SAME
    if email == password:
        messagebox.showerror(title="Error 402", message="Password and Email cannot be the same")
    else:
        # CHECK IF PASSWORD IS LESS THAN 6 LETTER
        if len(password) < 6:
            messagebox.showerror(title="Error 403", message="Password must be at least 6 letter")
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


# ======================================================================================================


# UI
# The UI section of the file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\login_page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


wn.geometry("265x291")
wn.configure(bg="#FFFFFF")

canvas = Canvas(
    wn,
    bg="#FFFFFF",
    height=291,
    width=265,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    265.0,
    67.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    20.0,
    0.0,
    anchor="nw",
    text="LOGIN/SIGN UP",
    fill="#000000",
    font=("Karantina Regular", 40 * -1)
)

# ======EMAIL=ENTRY=&=TEXT======

# EMAIL TEXT
canvas.create_text(
    26.0,
    85.0,
    anchor="nw",
    text="EMAIL",
    fill="#000000",
    font=("Karantina Regular", 24 * -1)
)

# EMAIL ENTRY
email_entry_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    107.0,
    120.5,
    image=email_entry_image
)
email_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
email_entry.place(
    x=31.5,
    y=109.0,
    width=151.0,
    height=21.0
)

# ======PASSWORD=ENTRY======


# PASSWORD TEXT
canvas.create_text(
    26.0,
    157.0,
    anchor="nw",
    text="PASSWORD",
    fill="#000000",
    font=("Karantina Regular", 24 * -1)
)

# PASSWORD ENTRY
password_entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
password_entry_bg_2 = canvas.create_image(
    107.0,
    192.5,
    image=password_entry_image_2
)
password_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
password_entry.place(
    x=31.5,
    y=181.0,
    width=151.0,
    height=21.0
)

# ======LOGIN=BUTTON======

login_btn_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
login_btn = Button(
    image=login_btn_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_login_info,
    relief="flat"
)
login_btn.place(
    x=20.0,
    y=224.0,
    width=60.0,
    height=22.0
)

# ======SIGNUP=BUTTON======

sign_up_btn_image = PhotoImage(
    file=relative_to_assets("button_2.png"))
sign_up_btn = Button(
    image=sign_up_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=send_sign_up_info,
    relief="flat"
)
sign_up_btn.place(
    x=98.0,
    y=224.0,
    width=60.0,
    height=22.0
)

# SETTINGS AND MAINLOOP

wn.resizable(False, False)
wn.mainloop()

