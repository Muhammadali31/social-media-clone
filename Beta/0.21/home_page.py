from tkinter import *
import new_post

def home_page_screen():
    # SETTING UP WINDOW AND SETTINGS FOR IT
    top = Toplevel()
    top.resizable(height=False, width=False)

    # FUNCTIONS

    # NEW POST
    def new_post_win():
        new_post.new_post_win()

    # TITLE
    title = Label(top, text="MySocialSphere", font=("Arial", 25))
    title.grid(column=1,row=0)


    # POST BUTTON
    post_btn = Button(top, text="New Post", font=("Arial", "12"), command=new_post_win)
    post_btn.grid(column=0, row=2)

    top.mainloop()