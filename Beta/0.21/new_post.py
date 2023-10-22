from tkinter import *
from tkinter import messagebox
import firebase_newpost_handler

def new_post_win():
    # SETTING UP WINDOW AND SETTING
    top = Toplevel()
    top.resizable(width=False, height=False)

    # COMMANDS

    # SENDING POST DATA
    def send_post_data():
        # GETTING MESSAGE
        msg = post_entry.get()

        # SENDING POST TO FIREBASE
        send_post_result = firebase_newpost_handler.send_post(msg)

        # CHECK IF POST SENT
        if send_post_result == 1:
            messagebox.showinfo(title="Info Message", message="Post successfully sent")
        else:
            messagebox.showerror(title="Error 404", message="Message not sent")

    # TITLE
    title = Label(top, text="New Post", font=("Arial", 25))
    title.grid(column=0, row=0)

    # POST TEXT
    post_text_lb = Label(top, text="Text: ", font=("Arial", 12))
    post_text_lb.grid(column=0, row=1)

    # POST ENTRY
    post_entry = Entry(top, font=("Arial", 12))
    post_entry.grid(column=1, row=1)

    # SEND POST BTN
    send_post_btn = Button(top, text="Send", font=("Arial", 12), command=send_post_data)
    send_post_btn.grid(column=0, row=2)

    top.mainloop()