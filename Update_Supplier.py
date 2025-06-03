from customtkinter import *
from tkinter import messagebox

import DatabaseConnector

class UpdateSupplier:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="Update Supplier", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        self.suppliers= self.Convert(DatabaseConnector.getSupplierIds())

        self.supplierId = CTkComboBox(master = frame, values=self.suppliers, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color="#00FFFF", font=("Arial", 20), corner_radius=40)
        self.supplierName = CTkEntry(master = frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.supplierCompany = CTkEntry(master = frame, placeholder_text="Company", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.supplierContact = CTkEntry(master = frame, placeholder_text="Contact", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        
        self.supplierId.set("ID")

        add_order_button = CTkButton(master=frame, width=20, height=30, text="UPDATE", font=("Arial", 40, 'bold'), fg_color="#FFA502", text_color="#000000", corner_radius=40, command = self.updateSupplier)
        
        search = CTkButton(master=frame, width=20, height=30, text="Search", font=("Arial", 30, 'bold'), fg_color="#3742FA", text_color="#000000", corner_radius=40, command = self.search)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.supplierId.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.supplierName.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.supplierCompany.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.supplierContact.place(relx=0.5, rely=0.6, anchor=CENTER)

        search.place(relx=0.75, rely=0.3, anchor=CENTER)

        add_order_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def search(self):
        supplier = DatabaseConnector.getSupplier(self.supplierId.get())
        self.supplierName.delete(0, END)
        self.supplierCompany.delete(0, END)
        self.supplierContact.delete(0, END)

        self.supplierName.insert(0, supplier[1])
        self.supplierCompany.insert(0, supplier[2])
        self.supplierContact.insert(0, supplier[3])
    
    def updateSupplier(self):
        DatabaseConnector.updateSupplier(self.supplierId.get(),self.supplierName.get(),self.supplierCompany.get(),self.supplierContact.get())
        messagebox.shoeinfo("Success", "Supplier updated successfully")
        self.supplierName.delete(0, END)
        self.supplierCompany.delete(0, END)
        self.supplierContact.delete(0, END)
        self.supplierId.set("ID")

    def Convert(self, list1): 
        list2 = [] 
        for x in list1: 
            list2.append(x[0]) 
        return list2