from customtkinter import *
from tkinter import ttk, messagebox

import DatabaseConnector

class ViewSupplier:
    def __init__(self,root):

        self.suppliers = DatabaseConnector.viewSupplier()

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="View Supplier", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        delete_button = CTkButton(master=frame, width=20, height=30, text="DELETE", font=("Arial", 30, 'bold'), fg_color="#FF0000", text_color="#000000", corner_radius=40, command=self.delete)

        self.table = ttk.Treeview(frame, height=20, columns=("ID", "Name", "Company", "Contact"), show="headings")

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Company", text="Email")
        self.table.heading("Contact", text="Contact")

        self.table.column("ID", anchor=CENTER)
        self.table.column("Name", anchor=CENTER)
        self.table.column("Company", anchor=CENTER)
        self.table.column("Contact", anchor=CENTER)

        for supplier in self.suppliers:
            self.table.insert("", "end", values=supplier)
        
        self.table.place(relx=0.5, rely=0.5, anchor=CENTER)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        delete_button.place(relx=0.8, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def delete(self):
        selected_item = self.table.selection()
        for item in selected_item:
            DatabaseConnector.deleteSupplier(self.table.item(item)['values'][0])
            self.table.delete(item)
        messagebox.showinfo("Success", "Supplier deleted successfully")
