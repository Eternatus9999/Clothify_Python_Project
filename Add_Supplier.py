from customtkinter import *

class AddSupplier:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="Add Supplier", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        supplierId = CTkEntry(master = frame, placeholder_text="ID", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        supplierName = CTkEntry(master = frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        supplierCompany = CTkEntry(master = frame, placeholder_text="Company", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        supplierContact = CTkEntry(master = frame, placeholder_text="Contact", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        
        add_order_button = CTkButton(master=frame, width=20, height=30, text="Add Supplier", font=("Arial", 40, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        supplierId.place(relx=0.5, rely=0.3, anchor=CENTER)
        supplierName.place(relx=0.5, rely=0.4, anchor=CENTER)
        supplierCompany.place(relx=0.5, rely=0.5, anchor=CENTER)
        supplierContact.place(relx=0.5, rely=0.6, anchor=CENTER)

        add_order_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)