from customtkinter import *
from tkinter import ttk, messagebox

import DatabaseConnector

class ViewProduct:
    def __init__(self,root):

        self.products = DatabaseConnector.viewProduct()

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="View Product", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        delete_button = CTkButton(master=frame, width=20, height=30, text="DELETE", font=("Arial", 30, 'bold'), fg_color="#FF0000", text_color="#000000", corner_radius=40, command=self.delete)

        self.table = ttk.Treeview(frame, height=20, columns=("ID", "Name", "Size", "Quantity", "Price", "Category", "Supplier"), show="headings")

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Size", text="Size")
        self.table.heading("Quantity", text="Quantity")
        self.table.heading("Price", text="Price")
        self.table.heading("Category", text="Category")
        self.table.heading("Supplier", text="Supplier")

        self.table.column("ID",width=100, anchor=CENTER)
        self.table.column("Name",width=100, anchor=CENTER)
        self.table.column("Size",width=100, anchor=CENTER)
        self.table.column("Quantity",width=100, anchor=CENTER)
        self.table.column("Price",width=100, anchor=CENTER)
        self.table.column("Category",width=100, anchor=CENTER)
        self.table.column("Supplier",width=100, anchor=CENTER)

        for product in self.products:
            self.table.insert("", "end", values=product)
        
        self.table.place(relx=0.5, rely=0.5, anchor=CENTER)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        delete_button.place(relx=0.8, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def delete(self):
        selected_item = self.table.selection()
        for item in selected_item:
            DatabaseConnector.deleteProduct(self.table.item(item)['values'][0])
            self.table.delete(item)
        messagebox.showinfo("Success", "Product deleted successfully")
