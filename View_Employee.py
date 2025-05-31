from customtkinter import *
from tkinter import ttk

class ViewEmployee:
    def __init__(self,root):

        self.employees = []

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="View Employee", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        delete_button = CTkButton(master=frame, width=20, height=30, text="DELETE", font=("Arial", 30, 'bold'), fg_color="#FF0000", text_color="#000000", corner_radius=40, command=self.delete)

        self.table = ttk.Treeview(frame, height=20, columns=("ID", "Name", "Email", "Address", "Contact"), show="headings")

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Email", text="Email")
        self.table.heading("Address", text="Address")
        self.table.heading("Contact", text="Contact")

        for employee in self.employees:
            self.table.insert("", "end", values=employee)
        
        self.table.place(relx=0.5, rely=0.5, anchor=CENTER)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        delete_button.place(relx=0.8, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def delete(self):
            selected_item = self.table.selection()
            for item in selected_item:
                self.table.delete(item)
