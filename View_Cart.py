from customtkinter import *

from tkinter import ttk

class ViewCart:
    def __init__(self,total,cart):

        root = CTk()

        root.title("Clothify")

        root.geometry("1000x680+700+300")

        root.config(bg="#000000")

        title = CTkLabel(master=root, text="View Cart", font=("Arial", 80, 'bold'), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        totalLabel = CTkLabel(master=root, text=total, width=200, height=50, text_color="#FFFFFF", fg_color="#000000", font=("Arial", 30))

        table = ttk.Treeview(root, height=20, columns=("ID", "Name", "Quantity", "Price"), show="headings")

        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Quantity", text="Quantity")
        table.heading("Price", text="Price")

        for item in cart:
            table.insert("", "end", values=item)

        table.place(relx=0.5, rely=0.5, anchor=CENTER)
        totalLabel.place(relx=0.15, rely=0.9, anchor=CENTER)
        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        root.mainloop()
