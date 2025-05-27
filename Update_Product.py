from customtkinter import *

class UpdateProduct:
    def __init__(self,root):

        def add():
            index = index + 1

        def search():
            index = index + 1

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        index = 0 

        suppliers = ["Supplier"]

        products = ["ID"]

        category = ["Mens", "Womens", "Kids"]

        title = CTkLabel(master=frame, text="Update Product", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        productId = CTkComboBox(master=frame, values=products, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40)
        productName = CTkEntry(master=frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productSize = CTkEntry(master=frame, placeholder_text="Size", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productSupplier = CTkComboBox(master=frame, values=suppliers, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        productQty = CTkEntry(master=frame, placeholder_text="Quantity", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productPrice = CTkEntry(master=frame, placeholder_text="Price", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productCategory = CTkComboBox(master=frame, values=category, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')

        productCategory.set("Mens")

        productSupplier.set("Supplier")

        productId.set("ID")

        search = CTkButton(master=frame, width=100, text="Search", font=("Arial", 30, 'bold'), fg_color="#3742FA", text_color="#000000", corner_radius=40, command=search)

        add = CTkButton(master=frame, width=200, text="Update", font=("Arial", 40, 'bold'), fg_color="#FFA502", text_color="#000000", corner_radius=40, command=add)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        productId.place(relx=0.5, rely=0.3, anchor=CENTER)
        productName.place(relx=0.5, rely=0.38, anchor=CENTER)
        productSize.place(relx=0.5, rely=0.46, anchor=CENTER)
        productSupplier.place(relx=0.5, rely=0.54, anchor=CENTER)
        productQty.place(relx=0.5, rely=0.62, anchor=CENTER)
        productPrice.place(relx=0.5, rely=0.7, anchor=CENTER)
        productCategory.place(relx=0.5, rely=0.78, anchor=CENTER)

        add.place(relx=0.5, rely=0.9, anchor=CENTER)
        search.place(relx=0.75, rely=0.3, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
