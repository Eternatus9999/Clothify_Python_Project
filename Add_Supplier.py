from customtkinter import *
from tkinter import messagebox

import DatabaseConnector

class AddSupplier:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        supplier_id = StringVar(value="SP"+ str(DatabaseConnector.getSupplierId()+1))

        title = CTkLabel(master=frame, text="Add Supplier", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        self.supplierId = CTkEntry(master = frame, textvariable = supplier_id, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, state = "readonly")
        self.supplierName = CTkEntry(master = frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.supplierCompany = CTkEntry(master = frame, placeholder_text="Company", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.supplierContact = CTkEntry(master = frame, placeholder_text="Contact", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        
        add_order_button = CTkButton(master=frame, width=20, height=30, text="ADD", font=("Arial", 40, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40, command = self.addSupplier)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.supplierId.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.supplierName.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.supplierCompany.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.supplierContact.place(relx=0.5, rely=0.6, anchor=CENTER)

        add_order_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def addSupplier(self):
        if(self.supplierName.get() == "" or self.supplierCompany.get() == "" or self.supplierContact.get() == ""):
            messagebox.showerror("Error", "Please fill all the details")
        else:
            DatabaseConnector.insertSupplier(self.supplierId.get(), self.supplierName.get(), self.supplierCompany.get(), self.supplierContact.get())
            messagebox.showinfo("Success", "Supplier added successfully")
            self.supplierName.delete(0, END)
            self.supplierCompany.delete(0, END)
            self.supplierContact.delete(0, END)
            self.supplierId.set("SP"+str(DatabaseConnector.getSupplierId()+1))