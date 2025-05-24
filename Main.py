from customtkinter import *

class Main:
    def __init__(self):
        root = CTk()

        root.title("Clothify")

        root.geometry("600x400")	

        root.eval('tk::PlaceWindow . center')

        root.resizable(False, False)

        root.config(bg="#000000")


        def login():
            root.destroy()
            import Login
            Login.Login(root)


        register_button = CTkButton(master=root,width=200, height=50, text="Register", font=("Arial", 20), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        login_button = CTkButton(master=root, width=200, height=50, text="Login", font=("Arial", 20), fg_color="#FFFFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command=login)   

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        register_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        title.place(relx=0.5, rely=0.3, anchor=CENTER)
        login_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        root.mainloop()

Main()