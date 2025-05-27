from customtkinter import *

class MainPage:
    def __init__(self):
        def login():
            import Login
            root.destroy()
            Login.Login()
        
        root = CTk()

        root.title("Clothify")

        root.geometry("600x400+700+300")	

        root.resizable(False, False)

        root.config(bg="#000000")

        login_button = CTkButton(master=root, width=200, height=50, text="Login", font=("Arial", 20), fg_color="#FFFFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command=login)   

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        title.place(relx=0.5, rely=0.3, anchor=CENTER)
        login_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        root.mainloop()
