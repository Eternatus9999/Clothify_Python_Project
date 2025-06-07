from customtkinter import *
from tkinter import messagebox

import DatabaseConnector

class UpdateProduct:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        self.suppliers = self.Convert(DatabaseConnector.getSupplierIds())

        sizes = ["XXL","XXL","XL","L","M","S","XS"]

        self.products = self.Convert(DatabaseConnector.getProductIds())

        category = ["Gents", "Ladies", "Kids"]

        title = CTkLabel(master=frame, text="Update Product", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        self.productId = CTkComboBox(master=frame, values=self.products, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40)
        self.productName = CTkEntry(master=frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productSize = CTkComboBox(master=frame, values=sizes, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        self.productSupplier = CTkComboBox(master=frame, values=self.suppliers, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        self.productQty = CTkEntry(master=frame, placeholder_text="Quantity", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productPrice = CTkEntry(master=frame, placeholder_text="Price", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productCategory = CTkComboBox(master=frame, values=category, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')

        self.productCategory.set("Category")

        self.productSize.set("Size")

        self.productSupplier.set("Supplier")

        self.productId.set("ID")

        search = CTkButton(master=frame, width=100, text="Search", font=("Arial", 30, 'bold'), fg_color="#3742FA", text_color="#000000", corner_radius=40, command=self.search)

        add = CTkButton(master=frame, width=200, text="Update", font=("Arial", 40, 'bold'), fg_color="#FFA502", text_color="#000000", corner_radius=40, command=self.updateProduct)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.productId.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.productName.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.productSize.place(relx=0.5, rely=0.46, anchor=CENTER)
        self.productSupplier.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.productQty.place(relx=0.5, rely=0.62, anchor=CENTER)
        self.productPrice.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.productCategory.place(relx=0.5, rely=0.78, anchor=CENTER)

        add.place(relx=0.5, rely=0.9, anchor=CENTER)
        search.place(relx=0.75, rely=0.3, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def search(self):
        product = DatabaseConnector.getProduct(self.productId.get())
        self.productName.delete(0, END)
        self.productQty.delete(0, END)
        self.productPrice.delete(0, END)

        self.productName.insert(0, product[1])  
        self.productSize.set(product[2])
        self.productSupplier.set(product[6])
        self.productQty.insert(0, product[3])
        self.productPrice.insert(0, product[4])
        self.productCategory.set(product[5])

    def updateProduct(self):
        DatabaseConnector.updateProduct(self.productId.get(), self.productName.get(), self.productSize.get(), self.productQty.get(), self.productPrice.get(), self.productCategory.get(), self.productSupplier.get())
        messagebox.showinfo("Success", "Product updated successfully")
        self.productName.delete(0, END)
        self.productQty.delete(0, END)
        self.productPrice.delete(0, END)
        self.productSize.set("Size")
        self.productSupplier.set("Supplier")
        self.productCategory.set("Category")

    def Convert(self, list1): 
        list2 = [] 
        for x in list1: 
            list2.append(x[0]) 
        return list2
