from customtkinter import *

class AddOrder:
    def __init__(self,root):

        def add():
            index = index + 1

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#FFFFFF")

        index = 0 

        label = CTkLabel(master=frame, text=index, font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        button = CTkButton(master=frame, width=20, height=30, text="Click me", font=("Arial", 28, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command=add)

        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        button.place(relx=0.5, rely=0.6, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)