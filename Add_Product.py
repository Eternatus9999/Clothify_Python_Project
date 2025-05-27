from customtkinter import *

class AddProduct:
    def __init__(self,root):

        def add():
            index = index + 1

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        index = 0 

        title = CTkLabel(master=frame, text="Add Product", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        productId = CTkEntry(master=frame, placeholder_text="ID", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productName = CTkEntry(master=frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productSize = CTkEntry(master=frame, placeholder_text="Size", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productSupplier = CTkEntry(master=frame, placeholder_text="Supplier", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productQty = CTkEntry(master=frame, placeholder_text="Quantity", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productPrice = CTkEntry(master=frame, placeholder_text="Price", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        productCategory = CTkEntry(master=frame, placeholder_text="Category", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)

        add = CTkButton(master=frame, width=200, text="ADD", font=("Arial", 28, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40, command=add)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        productId.place(relx=0.5, rely=0.3, anchor=CENTER)
        productName.place(relx=0.5, rely=0.38, anchor=CENTER)
        productSize.place(relx=0.5, rely=0.46, anchor=CENTER)
        productSupplier.place(relx=0.5, rely=0.54, anchor=CENTER)
        productQty.place(relx=0.5, rely=0.62, anchor=CENTER)
        productPrice.place(relx=0.5, rely=0.7, anchor=CENTER)
        productCategory.place(relx=0.5, rely=0.78, anchor=CENTER)

        add.place(relx=0.5, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
