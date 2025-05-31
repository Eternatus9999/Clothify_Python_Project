from customtkinter import *

class AddProduct:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        index = 0 

        self.suppliers = ["Supplier"]

        category = ["Mens", "Womens", "Kids"]

        sizes = ["XXL","XXL","XL","L","M","S","XS"]

        title = CTkLabel(master=frame, text="Add Product", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        self.productId = CTkEntry(master=frame, placeholder_text="ID", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productName = CTkEntry(master=frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productSize = CTkComboBox(master=frame, values=sizes, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        self.productSupplier = CTkComboBox(master=frame, values=self.suppliers, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        self.productQty = CTkEntry(master=frame, placeholder_text="Quantity", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productPrice = CTkEntry(master=frame, placeholder_text="Price", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.productCategory = CTkComboBox(master=frame, values=category, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')

        self.productCategory.set("Mens")
        self.productSize.set("XXL")
        self.productSupplier.set("Supplier")

        add = CTkButton(master=frame, width=200, text="ADD", font=("Arial", 40, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40, command=self.addProduct)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.productId.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.productName.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.productSize.place(relx=0.5, rely=0.46, anchor=CENTER)
        self.productSupplier.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.productQty.place(relx=0.5, rely=0.62, anchor=CENTER)
        self.productPrice.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.productCategory.place(relx=0.5, rely=0.78, anchor=CENTER)

        add.place(relx=0.5, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def addProduct(self):
        print(self.productId.get(), self.productName.get(), self.productSize.get(), self.productSupplier.get(), self.productQty.get(), self.productPrice.get(), self.productCategory.get())
