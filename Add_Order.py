from customtkinter import *
from tkinter import ttk

class AddOrder:
    def __init__(self, root):

        def search(self):
            print(searchitem.get())

        def viewcart():
            import View_Cart
            View_Cart.ViewCart(total,cart)
        
        total = "Total : "

        method = ["Cash", "Debit", "Credit"]

        cart = []

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        orderId = CTkEntry(master=frame, placeholder_text="OrderID", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        customerName = CTkEntry(master=frame, placeholder_text="Customer Name", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        paymentMethod = CTkComboBox(master=frame, values=method, width=200, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        paymentMethod.set("Cash")

        totalLabel = CTkLabel(master=frame, text=total, width=200, height=50, text_color="#000000", font=("Arial", 30))

        add_order_button = CTkButton(master=frame, width=20, height=50, text="Place Order", font=("Arial", 28, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40)

        add_to_cart = CTkButton(master=frame, width=20, height=50, text="Add to Cart", font=("Arial", 28, 'bold'), fg_color="#3742FA", text_color="#000000", corner_radius=40)

        view_cart = CTkButton(master=frame, width=200, height=50, text="View Cart", font=("Arial", 28, 'bold'), fg_color="#FFA502", text_color="#000000", corner_radius=40, command = viewcart)

        qty = CTkEntry(master=frame, placeholder_text="Quantity", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)

        itemview = CTkFrame(master=frame, width=700, height=400, fg_color="#FFFFFF")

        searchitem = CTkEntry(master=itemview, placeholder_text="Search Item", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)

        searchitem.bind("<KeyRelease>", search)

        itemtable = ttk.Treeview(itemview, columns=("ID", "Name", "Quantity", "Price"), show='headings', height=15)

        itemtable.heading("ID", text="ID")
        itemtable.heading("Name", text="Name")
        itemtable.heading("Quantity", text="Quantity")
        itemtable.heading("Price", text="Price")

        itemtable.place(relx=0.5, rely=0.595, anchor=CENTER)
        searchitem.place(relx=0.5, rely=0.1, anchor=CENTER)

        orderId.place(relx=0.2, rely=0.1, anchor=CENTER)
        customerName.place(relx=0.42, rely=0.1, anchor=CENTER)
        paymentMethod.place(relx=0.64, rely=0.1, anchor=CENTER)

        itemview.place(relx=0.4, rely=0.5, anchor=CENTER)
        totalLabel.place(relx=0.15, rely=0.9, anchor=CENTER)
        add_order_button.place(relx=0.82, rely=0.9, anchor=CENTER)

        add_to_cart.place(relx=0.88, rely=0.3, anchor=CENTER)
        view_cart.place(relx=0.88, rely=0.4, anchor=CENTER)

        qty.place(relx=0.88, rely=0.5, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)