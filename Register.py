from customtkinter import *

class Register:

    def back():
            root.destroy()
            import Main_Page
            Main_Page.MainPage()
    def __init__(self, master):
        self.master = master
        root = CTk()

        root.title("Clothify")

        root.geometry("800x600")

        root.eval('tk::PlaceWindow . center')

        root.resizable(False, False)

        root.config(bg="#000000")

        back_button = CTkButton(master=root,width=20, height=30, text="←", font=("Arial", 20), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=self.back)

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        email = CTkEntry(master=root, placeholder_text="Email", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")

        password = CTkEntry(master=root, placeholder_text="Password", show="*", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")
        
        name = CTkEntry(master=root, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")
        
        address = CTkEntry(master=root, placeholder_text="Address", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")
        
        phone = CTkEntry(master=root, placeholder_text="Phone", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")
        
        repassword = CTkEntry(master=root, placeholder_text="Re-Password", show="*", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")
        
        register_button = CTkButton(master=root,width=200, height=50, text="Register", font=("Arial", 20), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")

        title.place(relx=0.5, rely=0.1, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.3, anchor=CENTER)
        name.place(relx=0.5, rely=0.3, anchor=CENTER)
        phone.place(relx=0.5, rely=0.4, anchor=CENTER)
        email.place(relx=0.5, rely=0.5, anchor=CENTER)
        address.place(relx=0.5, rely=0.6, anchor=CENTER)
        repassword.place(relx=0.5, rely=0.7, anchor=CENTER)
        password.place(relx=0.5, rely=0.8, anchor=CENTER)
        register_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        root.mainloop()