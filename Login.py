from customtkinter import *

class Login:
    def __init__(self, master):
        self.master = master
        root = CTk()

        root.title("Clothify")

        root.geometry("600x400")

        root.resizable(False, False)

        root.config(bg="#000000")

        login_button = CTkButton(master=root,width=200, height=50, text="Login", font=("Arial", 20), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")

        back_button = CTkButton(master=root,width=20, height=30, text="←", font=("Arial", 20), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray")

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        email = CTkEntry(master=root, placeholder_text="Email", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")

        password = CTkEntry(master=root, placeholder_text="Password", show="*", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")

        title.place(relx=0.5, rely=0.1, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.3, anchor=CENTER)
        email.place(relx=0.5, rely=0.4, anchor=CENTER)
        password.place(relx=0.5, rely=0.6, anchor=CENTER)
        login_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        root.mainloop()