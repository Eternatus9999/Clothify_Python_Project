from customtkinter import *
from tkinter import ttk

import DatabaseConnector

class ViewOrder:
    def __init__(self,root):

        self.orders = DatabaseConnector.viewOrder()

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="View Order", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        delete_button = CTkButton(master=frame, width=20, height=30, text="DELETE", font=("Arial", 30, 'bold'), fg_color="#FF0000", text_color="#000000", corner_radius=40, command=self.delete)

        self.table = ttk.Treeview(frame, height=20, columns=("ID", "Customer Name", "Payment Method", "Price", "Date"), show="headings")

        self.table.heading("ID", text="ID")
        self.table.heading("Customer Name", text="Customer Name")
        self.table.heading("Payment Method", text="Payment Method")
        self.table.heading("Price", text="Price")
        self.table.heading("Date", text="Date")

        self.table.column("ID", anchor=CENTER)
        self.table.column("Customer Name", anchor=CENTER)
        self.table.column("Payment Method", anchor=CENTER)
        self.table.column("Price", anchor=CENTER)
        self.table.column("Date", anchor=CENTER)

        for order in self.orders:
            self.table.insert("", "end", values=order)
        
        self.table.place(relx=0.5, rely=0.5, anchor=CENTER)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        delete_button.place(relx=0.8, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def delete(self):
            selected_item = self.table.selection()
            for item in selected_item:
                DatabaseConnector.deleteOrder(self.table.item(item)['values'][0])
                self.table.delete(item)
