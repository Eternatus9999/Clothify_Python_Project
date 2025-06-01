from customtkinter import *
from tkinter import ttk , messagebox

from datetime import date

import DatabaseConnector

class AddOrder:

    def __init__(self, root):

        order_id = StringVar(value = "OR"+str(int(DatabaseConnector.getOrderId()[0].split("OR")[1]) + 1))

        self.total = 0

        method = ["Cash", "Debit", "Credit"]

        self.cart = []

        self.items = DatabaseConnector.viewProduct()

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        self.orderId = CTkEntry(master=frame, textvariable=order_id, width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, state= 'readonly')
        self.customerName = CTkEntry(master=frame, placeholder_text="Customer Name", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.paymentMethod = CTkComboBox(master=frame, values=method, width=200, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40, state= 'readonly')
        self.paymentMethod.set("Cash")

        self.totalLabel = CTkLabel(master=frame, text=("Total: "+str(self.total)), width=200, height=50, text_color="#000000", font=("Arial", 30))
        add_order_button = CTkButton(master=frame, width=20, height=50, text="Place Order", font=("Arial", 28, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40, command = self.placeOrder)

        add_to_cart = CTkButton(master=frame, width=20, height=50, text="Add to Cart", font=("Arial", 28, 'bold'), fg_color="#3742FA", text_color="#000000", corner_radius=40, command = self.add)

        view_cart = CTkButton(master=frame, width=200, height=50, text="View Cart", font=("Arial", 28, 'bold'), fg_color="#FFA502", text_color="#000000", corner_radius=40, command = self.viewcart)

        self.qty = CTkEntry(master=frame, placeholder_text="Quantity", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)

        itemview = CTkFrame(master=frame, width=700, height=400, fg_color="#FFFFFF")

        self.searchitem = CTkEntry(master=itemview, placeholder_text="Search Item", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)

        self.searchitem.bind("<KeyRelease>", self.search)

        self.itemtable = ttk.Treeview(itemview, columns=("ID", "Name", "Size", "Quantity", "Price"), show='headings', height=15)

        self.itemtable.heading("ID", text="ID", anchor=CENTER)
        self.itemtable.heading("Name", text="Name", anchor=CENTER)
        self.itemtable.heading("Size", text="Size", anchor=CENTER)
        self.itemtable.heading("Quantity", text="Quantity", anchor=CENTER)
        self.itemtable.heading("Price", text="Price", anchor=CENTER)

        self.itemtable.column("ID", width=100, anchor=CENTER)
        self.itemtable.column("Name", width=200, anchor=CENTER)
        self.itemtable.column("Size", width=100, anchor=CENTER)
        self.itemtable.column("Quantity", width=150, anchor=CENTER)
        self.itemtable.column("Price", width=150, anchor=CENTER)

        for item in self.items:
            self.itemtable.insert("", "end", values=item)

        self.itemtable.place(relx=0.5, rely=0.595, anchor=CENTER)
        self.searchitem.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.orderId.place(relx=0.2, rely=0.1, anchor=CENTER)
        self.customerName.place(relx=0.42, rely=0.1, anchor=CENTER)
        self.paymentMethod.place(relx=0.64, rely=0.1, anchor=CENTER)

        itemview.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.totalLabel.place(relx=0.15, rely=0.9, anchor=CENTER)
        add_order_button.place(relx=0.82, rely=0.9, anchor=CENTER)

        add_to_cart.place(relx=0.88, rely=0.3, anchor=CENTER)
        view_cart.place(relx=0.88, rely=0.4, anchor=CENTER)

        self.qty.place(relx=0.88, rely=0.5, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def viewcart(self):
        import View_Cart
        View_Cart.ViewCart(self.total,self.cart)

    def search(self, event):
        print(self.searchitem.get())

    def add(self):
        selected = self.itemtable.item(self.itemtable.selection(),"values")
        if(selected == ""): 
            messagebox.showerror("Error", "Select an Item")
        else:
            if(self.qty.get() == ""):
                messagebox.showerror("Error", "Enter Quantity")
            else:
                self.cart.append((selected[0], selected[1], int(self.qty.get()), selected[4]))
                self.total += int(selected[4]) * int(self.qty.get())
                self.qty.delete(0, END)
                self.totalLabel.configure(text=("Total: "+str(self.total)))

    def placeOrder(self):
        DatabaseConnector.insertOrder(self.orderId.get(), self.customerName.get(), self.paymentMethod.get(), self.total, date.today())
        self.total = 0
        self.customerName.delete(0, END)
        self.qty.delete(0, END)
        self.totalLabel.configure(text=("Total: "+str(self.total)))
        self.editTable()
        self.cart = []
        DatabaseConnector.updateAllProducts(self.items)

    def editTable(self):
        for i in range(len(self.cart)):
            for item in self.items:
                if(self.cart[i][0] == item[0]):
                    tempitem = list(item)
                    tempitem[3] -= self.cart[i][2]
                    self.items[self.items.index(item)] = tuple(tempitem)
                    break
        self.itemtable.delete(*self.itemtable.get_children())
        for item in self.items:
            self.itemtable.insert("", "end", values=item)
            
