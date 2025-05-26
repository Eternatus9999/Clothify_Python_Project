from customtkinter import *

class AddOrder:
    def __init__(self, root):
        
        total = "Total : "

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        orderId = CTkEntry(master=frame, placeholder_text="OrderID", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        customerName = CTkEntry(master=frame, placeholder_text="Customer Name", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        paymentMethod = CTkEntry(master=frame, placeholder_text="Payment Method", width=200, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)

        totalLabel = CTkLabel(master=frame, text=total, width=200, height=50, text_color="#000000", font=("Arial", 30))

        add_order_button = CTkButton(master=frame, width=20, height=30, text="Add Order", font=("Arial", 28, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40)

        itemview = CTkFrame(master=frame, width=800, height=400, fg_color="#FFFFFF")

        orderId.place(relx=0.2, rely=0.1, anchor=CENTER)
        customerName.place(relx=0.42, rely=0.1, anchor=CENTER)
        paymentMethod.place(relx=0.64, rely=0.1, anchor=CENTER)

        itemview.place(relx=0.5, rely=0.5, anchor=CENTER)
        totalLabel.place(relx=0.15, rely=0.9, anchor=CENTER)
        add_order_button.place(relx=0.82, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)