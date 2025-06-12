from customtkinter import *
from tkinter import messagebox

import DatabaseConnector

class MainPage:
    def __init__(self):
        
        self.root = CTk()

        self.root.title("Clothify")

        self.root.geometry("600x400+700+300")

        self.root.iconbitmap("Images/Logo.ico")

        self.root.resizable(False, False)

        self.root.config(bg="#000000")

        title = CTkLabel(master=self.root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")
        
        self.txtUser = CTkEntry(master=self.root, placeholder_text="UserId", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")
        self.txtPassword = CTkEntry(master=self.root, placeholder_text="Password", show="*", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, bg_color="#000000")

        login_button = CTkButton(master=self.root,width=200, height=50, text="Login", font=("Arial", 20), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command=self.login)
        
        title.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.txtUser.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.txtPassword.place(relx=0.5, rely=0.6, anchor=CENTER)
        login_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.root.mainloop()

    def login(self):
            userid = self.txtUser.get()
            password = self.txtPassword.get()
            if(userid == "admin" and password == "admin"):
                self.root.destroy()
                import Admin
                Admin.Admin()
            elif(self.isEmployee(userid, password)):
                self.root.destroy()
                import Chashier
                Chashier.Cashier()
            else:
                self.txtUser.delete(0, END)
                self.txtPassword.delete(0, END)
                messagebox.showerror("Error", "Invalid Email or Password")

    def isEmployee(self, userid, password):
        employees = DatabaseConnector.viewEmployee()
        for employee in employees:
            if(employee[0] == userid and employee[5] == password):
                return True
        return False
